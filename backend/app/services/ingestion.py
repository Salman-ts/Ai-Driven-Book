import frontmatter
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
import hashlib
from typing import List, Dict, Any
from pathlib import Path
import uuid

class IngestionService:
    def __init__(self):
        self.md = MarkdownIt()

    def parse_file(self, file_path: Path) -> List[Dict[str, Any]]:
        """
        Parse a Docusaurus Markdown file.
        Extracts frontmatter and chunks content by H2/H3 headers.
        """
        try:
            post = frontmatter.load(file_path)
            metadata = post.metadata
            content = post.content
            
            # Basic chunking strategy: Split by headers
            # A more robust implementation would use a token-aware splitter
            # For MVP, splitting by double newline is a start, but let's try to be smarter
            # or use the existing RecursiveCharacterTextSplitter if imports allow,
            # but here we implement "Markdown parsing" as requested.
            
            # Let's clean the content first (remove HTML tags if any)
            # soup = BeautifulSoup(self.md.render(content), "html.parser")
            # clean_text = soup.get_text()
            
            # Simple chunking for MVP:
            chunks = []
            raw_chunks = content.split("\n## ") # Split by H2
            
            base_url = f"/docs/{file_path.stem}" # Simplified URL generation
            
            for i, chunk_text in enumerate(raw_chunks):
                if not chunk_text.strip():
                    continue
                    
                # Re-add header marker if lost (except first chunk if it was preamble)
                if i > 0:
                    chunk_text = "## " + chunk_text
                
                # Hash content
                content_hash = hashlib.sha256(chunk_text.encode("utf-8")).hexdigest()
                
                chunks.append({
                    "content": chunk_text,
                    "content_hash": content_hash,
                    "source_url": f"{base_url}#section-{i}",
                    "metadata": {
                        "title": metadata.get("title", file_path.stem),
                        "chunk_index": i
                    }
                })
                
            return chunks
            
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return []

    async def ingest_content(self, source_dir: str, force_reindex: bool = False):
        """
        Orchestrate content ingestion.
        1. Parse all Markdown files in source_dir.
        2. Chunk content.
        3. Embed and Index using RAGService.
        """
        from app.services.rag import rag_service # Lazy import to avoid circular dependency
        
        path = Path(source_dir)
        if not path.exists():
            print(f"Source directory {source_dir} does not exist.")
            return

        if force_reindex:
            # Re-create collection logic would go here
            # rag_service.recreate_collection() # If implemented
            pass

        files = list(path.glob("**/*.md"))
        print(f"Found {len(files)} Markdown files to ingest.")
        
        total_chunks = 0
        for file_path in files:
            print(f"Processing {file_path}...")
            chunks = self.parse_file(file_path)
            
            # Group chunks by file for ingestion to keep context metadata consistent
            # In a real app, we might pass list of chunks directly to rag_service
            # But rag_service.ingest_file takes raw content string currently.
            # Let's adapt: We will use a lower level ingest_chunks in rag_service or 
            # modify ingest_file to accept chunks. 
            # Given current rag_service.ingest_file logic: "chunks = self.chunker.chunk(content, metadata)"
            # It re-chunks. We want to use OUR chunks from IngestionService.
            
            # Update: To avoid rewriting rag_service entirely right now, we will
            # construct a synthetic call or better, add a method `ingest_chunks` to RAGService.
            # For this MVP, let's assume we add `ingest_pre_chunked` to RAGService.
            
            # Since we can't easily modify RAGService in this same step without multiple tool calls,
            # We will assume RAGService has `ingest_batch` that takes text and metadata.
            
            # ACTUALLY, checking rag_service.py: `ingest_file` takes content and metadata.
            # It re-chunks using SemanticChunker.
            # But IngestionService does its own Markdown-aware chunking (T010).
            # We should probably expose `ingest_chunks` in RAGService.
            
            # For now, let's bypass rag_service.chunker by calling client.embed directly here?
            # No, that duplicates logic.
            # Better approach: Modify rag_service to accept pre-chunked data.
            # Since I just updated rag_service, I can't modify it again easily in this turn.
            
            # WORKAROUND: We will iterate our chunks and pass them as "files" to rag_service.ingest_file
            # but that would double-chunk.
            
            # Let's fix this by calling rag_service.client.embed directly here as a temporary measure
            # OR (Cleaner) - Update RAGService to have `ingest_chunks`.
            # I will modify RAGService in the NEXT step.
            
            # For this file, I will write the code assuming `rag_service.ingest_batch(chunks)` exists.
            
            await rag_service.ingest_batch(chunks)
            total_chunks += len(chunks)
            
        print(f"Ingestion complete. Processed {total_chunks} chunks.")

ingestion_service = IngestionService()
