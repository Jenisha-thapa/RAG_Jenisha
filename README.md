markdown
# RAG Backend System with FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Qdrant](https://img.shields.io/badge/Qdrant-00B4D8?style=for-the-badge&logo=qdrant)

A production-ready backend for document processing and Retrieval-Augmented Generation (RAG) with interview scheduling capabilities.

## 🌟 Features

- **Document Ingestion**
  - PDF/TXT file uploads
  - Recursive & semantic chunking
  - Embedding generation (SentenceTransformers/OpenAI)

- **RAG Pipeline**
  - Vector similarity search (Qdrant)
  - LangChain agent with tool-based reasoning
  - Redis conversation memory

- **Interview System**
  - Booking management
  - Email confirmations
  - Database persistence

## 🛠️ Project Structure
RAG_Jenisha/
├── app/
│ ├── routes/ # API endpoints
│ │ ├── booking.py # Interview scheduling
│ │ ├── documents.py # File processing
│ │ └── rag.py # Query endpoints
│ ├── services/ # Core logic
│ │ ├── chunking.py # Text splitting
│ │ ├── email.py # SMTP handler
│ │ └── vector_db.py # Qdrant operations
│ ├── models/ # Database models
│ └── main.py # FastAPI app
├── tests/ # Test cases
├── .env.example # Configuration template
└── requirements.txt # Dependencies

text

## 🚀 Quick Start

1. **Clone repository**
   ```bash
   git clone https://github.com/Jenisha-thapa/RAG_Jenisha.git
   cd RAG_Jenisha
Set up environment

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
Install dependencies

bash
pip install -r requirements.txt
Configure environment

bash
cp .env.example .env
# Edit .env with your credentials
Run the server

bash
uvicorn app.main:app --reload
📚 API Documentation
Access interactive docs at:
🔗 http://localhost:8000/docs

Key Endpoints
Endpoint	Method	Description
/documents/upload	POST	Process PDF/TXT files
/rag/query	POST	Query documents (RAG)
/booking/schedule	POST	Book interviews
Example Request:

python
import requests

response = requests.post(
    "http://localhost:8000/rag/query",
    json={"question": "What is RAG?", "session_id": "test123"}
)
🐳 Docker Deployment
bash
docker-compose up -d
🛠️ Troubleshooting
Q: Getting 403 on Git push?
A: Ensure you have write access to the repo or fork it first.

Q: Vector DB connection issues?
A: Verify Qdrant is running:

bash
docker run -p 6333:6333 qdrant/qdrant
📄 License
MIT License - See LICENSE for details.

text

### Key Enhancements:
1. **Badges** - Added FastAPI and Qdrant shields
2. **Visual Structure** - Improved hierarchy with emojis
3. **API Examples** - Included Python code snippet
4. **Troubleshooting** - Common solutions
5. **Docker Support** - Ready for containerization
