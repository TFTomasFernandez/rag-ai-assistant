from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from query import get_rag_chain

app = FastAPI(
    title="RAG Challenge API",
    version="1.0",
    description="RAG con ChromaDB y Cohere"
)

rag = get_rag_chain()  

class QueryRequest(BaseModel):
    user_name: str
    question: str

class QueryResponse(BaseModel):
    answer: str


@app.get("/")
def ui():
    return FileResponse("ui.html")


@app.get("/health")
def health():
    return {"status": "ok", "rag": "running"}


@app.post("/query", response_model=QueryResponse)
def query_rag(payload: QueryRequest):
    try:
        answer = rag(payload.question)
    except Exception as e:
        answer = f"Ocurrió un error interno al procesar la consulta: {str(e)} ⚠️"
    return {"answer": answer}



