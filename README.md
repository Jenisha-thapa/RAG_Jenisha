# RAG Backend System

A FastAPI-based backend for document processing and Retrieval-Augmented Generation (RAG) with interview booking capabilities.

## Features

- 📄 **Document Processing**: Upload PDF/TXT files, chunk text, and generate embeddings
- 🧠 **RAG Pipeline**: Query documents using LangChain with vector similarity search
- 📅 **Interview Booking**: Schedule interviews with email confirmations
- 🗄️ **Database Support**: PostgreSQL/SQLite for metadata + Qdrant/Pinecone for vectors

## Tech Stack

| Component           | Technology                |
|---------------------|---------------------------|
| Framework           | FastAPI                   |
| Vector DB           | Qdrant                    |
| Embeddings          | SentenceTransformers      |
| Language Models     | LangChain                 |
| Email               | SMTP (Gmail)              |
| Caching             | Redis                     |

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- [Qdrant](https://qdrant.tech/documentation/quick-start/) running locally or in cloud
- Redis server (for conversation memory)

### 2. Installation
bash
# Clone repository
git clone https://github.com/Jenisha-thapa/RAG_Backend.git
cd RAG_Backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

3. Configuration
Create .env file:

ini
# Database
DATABASE_URL=sqlite:///./rag.db

# Qdrant
VECTOR_DB_URL=http://localhost:6333
VECTOR_DB_API_KEY=

# Email (Gmail example)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=your@gmail.com
EMAIL_PASSWORD=your-app-password

4. Run the Application
bash
uvicorn app.main:app --reload
Access docs at: http://localhost:8000/docs

API Endpoints
Endpoint	Method	Description
/documents/upload	POST	Upload and process documents
/rag/query	POST	Query the RAG system
/booking/schedule	POST	Schedule an interview
Example Requests
Upload Document
bash
curl -X POST -F "file=@sample.pdf" http://localhost:8000/documents/upload
Query RAG System
bash
curl -X POST -H "Content-Type: application/json" \
-d '{"question":"What is PalmMind?"}' \
http://localhost:8000/rag/query
Deployment
Docker
bash
docker-compose up -d
Production
bash
uvicorn app.main:app --host 0.0.0.0 --port 80
Project Structure
text
app/
├── main.py             # FastAPI app
├── routes/             # API endpoints
├── services/           # Business logic
├── models/             # Database models
└── utils/              # Helper functions
License
