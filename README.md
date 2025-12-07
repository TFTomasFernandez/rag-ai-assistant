📚 RAG Challenge — AI Assistant with Cohere
🧠 Overview

This project implements a Retrieval-Augmented Generation (RAG) assistant using Cohere's cloud models for embeddings and language generation, combined with a local vector database (ChromaDB) for efficient semantic search over documents.

The assistant reads and understands PDF documents and allows users to ask natural language questions through a web interface, returning precise answers based strictly on the document content.

Everything runs inside Docker for portability and simple deployment.

-------------------------------------------------------------------------------------------

🚀 Features

✅ Multilingual support (English, Spanish, Portuguese)

✅ Cohere-powered embeddings (cloud, lightweight)

✅ Command-R language model via Cohere

✅ Vector search with ChromaDB

✅ Context-based answering (no hallucinations)

✅ Language enforcement (answers follow user language)

✅ Emoji summarization

✅ Single-sentence answers

✅ Dockerized system (no local Python install needed)

✅ Simple web interface

✅ Fully portable

------------------------------------------------------------------------------------------

🏗 Architecture

User (Browser UI)
        |
        v
FastAPI (API Layer)
        |
        v
ChromaDB (Vector Storage) ← Cohere Embeddings
        |
        v
Cohere LLM (Command-R)

-----------------------------------------------------------------------------------------

📂 Project Structure
.
├── app.py                 # FastAPI backend
├── query.py               # RAG logic + Cohere integration
├── ingest.py              # Document processing + embedding
├── config.py              # Paths and constants
├── docker-compose.yml     # Docker orchestration
├── Dockerfile             # Container definition
├── requirements.txt       # Python dependencies
├── ui.html                # Web interface
├── README.md              # This file
│
├── data/                  # PDF documents folder
│   └── stories.pdf
│
└── vectordb/              # ChromaDB persistent database

------------------------------------------------------------------------------------------

✅ Requirements (User)

Only one requirement:

🐳 Docker Desktop installed

Download here:
https://www.docker.com/products/docker-desktop/

Ensure WSL2 is enabled and restart after installation if asked.

--------------------------------------------------------------------------------------------

⚙ Installation & Execution

* Step 1 — Clone or copy the project folder

This includes all files and the vectordb directory.

Create a file named ".env" in the folder main:

COHERE_API_KEY=YOUR_API_KEY_HERE


* Step 2 — Run the system

From inside the project folder:

docker compose up --build

Wait for:

Uvicorn running on http://0.0.0.0:8000

* Step 3 — Open the assistant

Open your browser:

👉 http://localhost:8000

--------------------------------------------------------------------------------------------

🧪 Usage

Enter your name

Ask a question about the documents

Receive a contextual answer

Examples:

✅ English:

What is the name of the magical flower?

✅ Spanish:

¿Cómo se llama la flor mágica?

✅ Portuguese:

Como se chama a flor mágica?

------------------------------------------------------------------------------------------

🛑 Stop the System

To shut everything down:

Press:

CTRL + C

------------------------------------------------------------------------------------------

🧼 Reset Vector Database (Optional)

To re-index documents:

Delete folder:

vectordb/


Then run:

docker compose up --build

------------------------------------------------------------------------------------------

💡 Technical Stack

FastAPI

Cohere (embeddings + LLM)

ChromaDB

LangChain

Docker

Python 3.10

------------------------------------------------------------------------------------------

📌 Author

Tomás Fernández
AI Engineer & Data Scientist

Specialized in:

AI Agents

RAG systems

Cloud ML

NLP

MLOps
