# ingest.py
import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma

from config import CHROMA_DIR, DOCUMENTS_PATH  # igual que antes


def main():
    pdf_dir = Path(DOCUMENTS_PATH)

    docs = []
    for path in pdf_dir.glob("*.pdf"):
        loader = PyPDFLoader(str(path))
        docs.extend(loader.load())

    print(f"📄 Documentos cargados: {len(docs)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.split_documents(docs)
    print(f"🧩 Chunks generados: {len(chunks)}")

    # 👇 Embeddings en Cohere (multilingüe y liviano)
    embeddings = CohereEmbeddings(
        model="embed-multilingual-light-v3.0",  # soporta español, inglés, etc. :contentReference[oaicite:1]{index=1}
        cohere_api_key=os.environ.get("COHERE_API_KEY"),
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    db.persist()
    print("✅ Documentos indexados con Cohere embeddings")


if __name__ == "__main__":
    main()


