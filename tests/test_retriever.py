import sys
import os

# Agrega la raíz del proyecto al path para permitir imports relativos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.retriever_agent import retrieve_docs

def test_retrieval():
    """Test unitario para la función retrieve_docs del agente de recuperación.

    Verifica que:
    1. El índice vectorial exista (requisito previo).
    2. La consulta semántica retorne al menos un documento relevante.

    Raises:
        AssertionError: Si el índice no existe o no se recupera ningún documento.
    """
    assert os.path.exists("index/vector_store.pkl"), "Debes ejecutar index_documents.py antes de correr el test"
    docs = retrieve_docs("¿Cuánto cuesta el producto?")
    assert len(docs) > 0, "No se recuperaron documentos, posible fallo en el índice o embeddings."
