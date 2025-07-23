import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carga variables desde el archivo .env
load_dotenv()

# Configura Gemini con la clave del entorno
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_response(query: str, docs: list) -> str:
    """Genera una respuesta usando Gemini basada en documentos recuperados.

    Args:
        query (str): Pregunta realizada por el usuario.
        docs (list): Lista de objetos Document de LangChain, cada uno con `page_content`.

    Returns:
        str: Respuesta generada por el modelo Gemini, basada únicamente en el contenido contextual entregado.
    """
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""Responde en un tono conversacional y solo usando esta información:
{context}
Pregunta: {query}
Respuesta:"""
    response = model.generate_content(prompt)
    return response.text

