from typing import Optional
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import BaseMessage
from langchain.tools import Tool
from langchain.vectorstores import Qdrant
from app.services.vector_db import get_vector_db
from app.config import settings

class RAGService:
    """Service for RAG agent functionality"""
    
    def __init__(self, message_history: Optional[BaseMessage] = None):
        self.message_history = message_history
        self.vector_db = get_vector_db()
        
        # Initialize tools
        self.tools = [
            Tool(
                name="document_search",
                func=self.search_documents,
                description="Search uploaded documents for relevant information"
            )
        ]
        
        # Initialize agent
        self.agent = create_tool_calling_agent(
            llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
            tools=self.tools,
            prompt=self._create_prompt()
        )
        
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            memory=self.message_history
        )
    
    async def query(self, question: str, tools_enabled: bool = True) -> dict:
        """Execute a query against the RAG agent"""
        if not tools_enabled:
            return {"response": await self.agent_executor.arun(input=question)}
        
        result = await self.agent_executor.ainvoke({"input": question})
        return {
            "response": result["output"],
            "intermediate_steps": result.get("intermediate_steps", [])
        }
    
    def search_documents(self, query: str) -> str:
        """Search documents in vector DB"""
        docs = self.vector_db.similarity_search(query, k=3)
        return "\n\n".join([doc.page_content for doc in docs])
    
    def _create_prompt(self):
        """Create the agent prompt template"""
        # Implementation omitted for brevity
        pass