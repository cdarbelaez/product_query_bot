import pickle
import os

# Ruta del índice vectorial embebido generado por index_documents.py
index_path = "index/vector_store.pkl"

# Verifica si el índice existe; si no, lanza una excepción con mensaje claro
if not os.path.exists(index_path):
    raise FileNotFoundError(
        "¡El archivo vector_store.pkl no fue encontrado! "
        "Ejecuta primero index_documents.py para generar el índice."
    )

# Carga el vectorstore previamente embebido (FAISS)
with open(index_path, "rb") as f:
    vectorstore = pickle.load(f)

def retrieve_docs(query: str, k: int = 3):
    """Recupera los documentos más relevantes en base a una consulta textual.

    Usa búsqueda semántica en un índice FAISS previamente generado, retornando
    los `k` documentos más similares al query.

    Args:
        query (str): Texto de la consulta del usuario.
        k (int, optional): Número de documentos a recuperar. Por defecto es 3.

    Returns:
        List[langchain_core.documents.base.Document]: Lista de documentos relevantes, cada uno con `page_content` y `metadata`.

    Raises:
        RuntimeError: Si el vectorstore no está cargado correctamente.

    Example:
        >>> docs = retrieve_docs("¿Cuánto dura la batería del reloj?")
        >>> print(docs[0].page_content)
    """
    return vectorstore.similarity_search(query, k=k)

