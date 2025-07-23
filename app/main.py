from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.retriever_agent import retrieve_docs
from agents.responder_agent import generate_response

app = FastAPI(title="Product Query Bot", description="Microservicio de respuesta vía RAG usando Gemini", version="1.0")

class QueryInput(BaseModel):
    """Modelo de entrada para la consulta del usuario.

    Attributes:
        user_id (str): Identificador único del usuario que hace la consulta.
        query (str): Pregunta o mensaje enviado por el usuario.
    """
    user_id: str
    query: str

@app.post("/query")
async def query(input: QueryInput):
    """Endpoint que recibe preguntas del usuario y devuelve respuestas generadas.

    Este endpoint:
    1. Valida que la consulta no esté vacía.
    2. Recupera documentos relevantes mediante búsqueda semántica.
    3. Genera una respuesta conversacional usando el modelo Gemini.

    Args:
        input (QueryInput): Objeto con `user_id` y `query`.

    Returns:
        dict: Diccionario con una clave `"answer"` y la respuesta generada.

    Raises:
        HTTPException: Si la consulta está vacía (400).
    """
    if not input.query.strip():
        raise HTTPException(status_code=400, detail="Empty query")

    docs = retrieve_docs(input.query)
    answer = generate_response(input.query, docs)
    return {"answer": answer}

