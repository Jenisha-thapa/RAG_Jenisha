from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from app.services.database import get_db
from app.services.chunking import ChunkingService
from app.services.embedding import EmbeddingService
from app.services.vector_db import VectorDBService
from app.utils.file_processing import process_uploaded_file
from app.models.document import DocumentMetadata

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
async def upload_file(file: UploadFile):
    """Endpoint for uploading and processing documents"""
    try:
        # Process file and extract text
        text, file_info = await process_uploaded_file(file)
        
        # Initialize services
        db = get_db()
        chunker = ChunkingService(strategy="recursive")
        embedder = EmbeddingService(model_name="sentence-transformers/all-mpnet-base-v2")
        vector_db = VectorDBService()
        
        # Chunk text
        chunks = chunker.chunk_text(text)
        
        # Generate embeddings
        embeddings = await embedder.generate_embeddings(chunks)
        
        # Store in vector DB
        vector_db.upsert_embeddings(
            vectors=embeddings,
            metadata=[{"chunk_text": chunk, "file_name": file_info.name} for chunk in chunks]
        )
        
        # Save metadata
        doc_metadata = DocumentMetadata(
            file_name=file_info.name,
            file_size=file_info.size,
            file_type=file_info.type,
            chunking_method="recursive",
            embedding_model="sentence-transformers/all-mpnet-base-v2",
            num_chunks=len(chunks)
        )
        db.add(doc_metadata)
        db.commit()
        
        return JSONResponse(
            content={"message": "File processed successfully", "num_chunks": len(chunks)},
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )