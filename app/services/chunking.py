from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter, SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings

class ChunkingService:
    """Service for handling different text chunking strategies"""
    
    def __init__(self, strategy: str = "recursive"):
        self.strategy = strategy
        self.embedder = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        ) if strategy == "semantic" else None
        
    def chunk_text(self, text: str) -> List[str]:
        if self.strategy == "recursive":
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separators=["\n\n", "\n", " ", ""]
            )
            return splitter.split_text(text)
        elif self.strategy == "semantic":
            splitter = SemanticChunker(embeddings=self.embedder)
            return splitter.split_text(text)
        else:
            raise ValueError(f"Unsupported chunking strategy: {self.strategy}")