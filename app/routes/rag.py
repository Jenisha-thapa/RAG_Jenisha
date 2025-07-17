from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from langchain.agents import AgentExecutor
from langchain.memory import RedisChatMessageHistory
from app.services.rag import RAGService
from app.models.base import QueryRequest, AgentResponse

router = APIRouter(prefix="/rag", tags=["rag"])

@router.post("/query", response_model=AgentResponse)
async def query_agent(request: QueryRequest):
    """Endpoint for querying the RAG agent"""
    try:
        # Initialize conversation memory
        message_history = RedisChatMessageHistory(
            session_id=request.session_id,
            url=settings.REDIS_URL
        )
        
        # Initialize RAG service
        rag_service = RAGService(message_history=message_history)
        
        # Execute agent
        response = await rag_service.query(
            question=request.question,
            tools_enabled=request.tools_enabled
        )
        
        return JSONResponse(
            content=response.dict(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )