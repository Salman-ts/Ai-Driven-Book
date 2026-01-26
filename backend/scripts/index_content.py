"""
Script to index book content into Qdrant for RAG functionality.
Run this once to populate the vector database.

Usage: python scripts/index_content.py
"""

import asyncio
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.rag import rag_service

# Book content to index
DOCS_DIR = Path(__file__).parent.parent.parent / "docs"

async def read_markdown_files():
    """Read all markdown files from docs directory."""
    files = []
    
    for md_file in DOCS_DIR.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract metadata from path
            parts = md_file.relative_to(DOCS_DIR).parts
            module = parts[0] if len(parts) > 1 else "intro"
            chapter = md_file.stem
            
            files.append({
                "content": content,
                "metadata": {
                    "module": module,
                    "chapter": chapter,
                    "file_path": str(md_file.relative_to(DOCS_DIR)),
                    "source": "ai-book"
                }
            })
            print(f"Read: {md_file.name}")
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    return files

async def index_all_content():
    """Index all book content into Qdrant."""
    print("=" * 50)
    print("AI Book Content Indexer")
    print("=" * 50)
    
    # 1. Initialize collection
    print("\n1. Initializing Qdrant collection...")
    rag_service.init_collection()
    print(f"   Collection: {rag_service.collection_name}")
    
    # 2. Read all markdown files
    print("\n2. Reading markdown files...")
    files = await read_markdown_files()
    print(f"   Found {len(files)} files")
    
    # 3. Index each file
    print("\n3. Indexing content (this may take a few minutes)...")
    for i, file_data in enumerate(files):
        try:
            await rag_service.ingest_file(
                content=file_data["content"],
                metadata=file_data["metadata"]
            )
            print(f"   [{i+1}/{len(files)}] Indexed: {file_data['metadata']['chapter']}")
        except Exception as e:
            print(f"   [{i+1}/{len(files)}] Error: {file_data['metadata']['chapter']} - {e}")
    
    # 4. Verify
    print("\n4. Verifying...")
    collection_info = rag_service.qdrant.get_collection(rag_service.collection_name)
    print(f"   Total vectors: {collection_info.points_count}")
    
    print("\n" + "=" * 50)
    print("Indexing complete!")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(index_all_content())
