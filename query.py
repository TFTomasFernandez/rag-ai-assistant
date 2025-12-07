import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_cohere.chat_models import ChatCohere
from langdetect import detect

from config import CHROMA_DIR


def get_rag_chain():
    embeddings = CohereEmbeddings(
        model="embed-multilingual-light-v3.0",
        cohere_api_key=os.environ.get("COHERE_API_KEY"),
    )

    db = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )

    # 👉 Prompt SOLO en INGLÉS
    prompt_en = ChatPromptTemplate.from_template("""
You are a helpful assistant.

LANGUAGE:
- You MUST answer ONLY in ENGLISH.
- Do NOT use Spanish or Portuguese.
- Never translate the question, just answer it.

STYLE:
- Answer in exactly ONE sentence.
- Always write in THIRD PERSON.
- Always include 1 or 2 emojis that summarize the answer.
- Use ONLY the information in CONTEXT.
- If the answer is not in the context, say you don't know.

CONTEXT:
{context}

QUESTION:
{question}
""")

    # 👉 Prompt SOLO en ESPAÑOL
    prompt_es = ChatPromptTemplate.from_template("""
Eres un asistente útil.

IDIOMA:
- Debes responder SIEMPRE y SOLAMENTE en ESPAÑOL neutro.
- No uses inglés ni portugués.
- No traduzcas la pregunta, solo respóndela.

ESTILO:
- Responde en exactamente UNA sola oración.
- Escribe siempre en TERCERA persona.
- Incluye siempre 1 o 2 emojis que resuman la respuesta.
- Usa ÚNICAMENTE la información del CONTEXTO.
- Si la respuesta no está en el contexto, di que no lo sabes.

CONTEXTO:
{context}

PREGUNTA:
{question}
""")

    # 👉 Prompt SOLO en PORTUGUÉS
    prompt_pt = ChatPromptTemplate.from_template("""
Você é um assistente útil.

IDIOMA:
- Você deve responder SEMPRE e APENAS em PORTUGUÊS.
- Não use espanhol nem inglês.
- Não traduza a pergunta, apenas responda.

ESTILO:
- Responda em exatamente UMA frase.
- Escreva sempre em TERCEIRA pessoa.
- Inclua sempre 1 ou 2 emojis que resumam a resposta.
- Use SOMENTE as informações do CONTEXTO.
- Se a resposta não estiver no contexto, diga que não sabe.

CONTEXTO:
{context}

PERGUNTA:
{question}
""")

    llm = ChatCohere(
        model="command-r-08-2024",  # o el que estés usando
        temperature=0,
        cohere_api_key=os.environ.get("COHERE_API_KEY"),
    )

    def rag(question: str) -> str:
        # Detectamos idioma de la pregunta
        try:
            lang = detect(question)
        except Exception:
            lang = "en"

        if lang.startswith("es"):
            prompt = prompt_es
            not_found = "La respuesta no está disponible en el documento. 🤷‍♂️"
        elif lang.startswith("pt"):
            prompt = prompt_pt
            not_found = "A resposta não está disponível no documento. 🤷‍♂️"
        else:
            # cualquier otra cosa (incluye inglés)
            prompt = prompt_en
            not_found = "The answer is not available in the document. 🤷‍♂️"

        docs = db.similarity_search(question, k=10)
        if not docs:
            return not_found

        context = "\n\n".join(d.page_content for d in docs)

        chain = prompt | llm
        res = chain.invoke({"context": context, "question": question})
        return res.content

    return rag
