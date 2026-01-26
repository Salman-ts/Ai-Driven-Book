from qdrant_client import QdrantClient, models
import cohere
from app.core.config import settings
import uuid
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
import asyncio

class SemanticChunker:
    def __init__(self, chunk_size=1500, overlap=200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""]
        )
    
    def chunk(self, text: str, metadata: dict) -> List[Dict[str, Any]]:
        docs = self.splitter.create_documents([text], metadatas=[metadata])
        chunks = []
        for i, doc in enumerate(docs):
            chunk_meta = doc.metadata.copy()
            chunk_meta.update({"chunk_id": i})
            chunks.append({
                "content": doc.page_content,
                "metadata": chunk_meta
            })
        return chunks

class RAGService:
    def __init__(self):
        self.qdrant = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.client = cohere.ClientV2(api_key=settings.COHERE_API_KEY)
        self.collection_name = "ai_book_chunks_cohere"
        self.vector_size = 1024 # embed-english-v3.0
        self.chunker = SemanticChunker()
        self.embedding_model = "embed-english-v3.0"

    def init_collection(self):
        if not self.qdrant.collection_exists(self.collection_name):
            self.qdrant.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.COSINE
                )
            )
            print(f"Collection {self.collection_name} created.")

    async def get_embedding(self, text: str, input_type: str = "search_query") -> List[float]:
        # Cohere V2 Client API might vary slightly, ensuring correct usage for embedding
        response = self.client.embed(
            texts=[text],
            model=self.embedding_model,
            input_type=input_type,
            embedding_types=["float"]
        )
        return response.embeddings.float[0]

    async def search(self, query: str, limit: int = 5, score_threshold: float = 0.5):
        query_vector = await self.get_embedding(query, input_type="search_query")
        results = self.qdrant.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
            score_threshold=score_threshold,
            with_payload=True
        ).points
        return results

    async def generate_response_grounded(
        self, 
        query: str, 
        selection_context: str = None, 
        selection_only: bool = False,
        limit: int = 5
    ) -> Dict[str, Any]:
        """
        Generate a grounded response using Cohere RAG.
        Supports both global retrieval and selected-text-only modes.
        """
        documents = []
        mode = "global"
        
        # 1. Retrieve Context
        if selection_only and selection_context:
            mode = "selection"
            # Use user selection as the ONLY document
            documents = [{
                "data": {
                    "content": selection_context,
                    "title": "User Selection",
                    "url": "#selection"
                }
            }]
        else:
            # Global Search
            results = await self.search(query, limit=limit)
            for point in results:
                meta = point.payload.get('metadata', {})
                documents.append({
                    "data": {
                        "content": point.payload.get('content'),
                        "title": meta.get('title', 'Unknown Source'),
                        "url": meta.get('url', '')
                    }
                })
        
        # 2. Generate with Cohere
        # If no documents found in global mode, return fallback immediately
        if not documents and not (selection_only and selection_context): # Fallback also for selection_only with empty context
             return {
                "answer": "I cannot answer this based on the provided book content.",
                "sources": [],
                "provenance": {"mode": mode, "latency_ms": 0}
            }

        response = self.client.chat(
            model="command-r-plus-08-2024", # Specify a robust RAG model
            messages=[{"role": "user", "content": query}],
            documents=documents,
            temperature=0.3
        )
        
        # 3. Format Response
        answer = response.message.content[0].text
        sources = []
        
        if response.message.citations:
            for cit in response.message.citations:
                # Map citations back to our source documents
                # Cohere citations return indices of 'documents' list used
                for doc_idx in cit.document_ids:
                    # doc_idx is like "doc_0", "doc_1"
                    try:
                        idx = int(doc_idx.split('_')[1])
                        if 0 <= idx < len(documents):
                            src_doc = documents[idx]["data"]
                            sources.append({
                                "title": src_doc.get("title"),
                                "url": src_doc.get("url"),
                                "score": 1.0, # Placeholder, Cohere doesn't give per-citation relevance score easily here
                                "snippet": cit.text 
                            })
                    except:
                        continue
                        
        # Deduplicate sources
        unique_sources = []
        seen = set()
        for s in sources:
            k = s['url']
            if k not in seen:
                seen.add(k)
                unique_sources.append(s)

        return {
            "answer": answer,
            "sources": unique_sources,
            "provenance": {
                "mode": mode,
                "latency_ms": 0 # TODO: Measure
            }
        }

    async def ingest_file(self, content: str, metadata: dict):
        chunks = self.chunker.chunk(content, metadata)
        await self.ingest_batch(chunks)

    async def ingest_batch(self, chunks: List[Dict[str, Any]]):
        """
        Ingest a batch of pre-chunked data.
        """
        texts = [c["content"] for c in chunks]
        if not texts:
            return

        # Batch embed (Cohere handles batches well)
        response = self.client.embed(
            texts=texts,
            model=self.embedding_model,
            input_type="search_document",
            embedding_types=["float"]
        )
        vectors = response.embeddings.float
        
        points = [
            models.PointStruct(id=str(uuid.uuid4()), vector=vec, payload={"content": c["content"], "metadata": c["metadata"]})
            for vec, c in zip(vectors, chunks)
        ]
        
        if points:
            self.qdrant.upload_points(collection_name=self.collection_name, points=points)
            print(f"Ingested {len(points)} chunks.")

rag_service = RAGService()
