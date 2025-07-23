"""
index_documents.py

Este script construye un índice vectorial FAISS a partir de descripciones de productos en texto plano.
Usa embeddings semánticos generados por un modelo de HuggingFace (all-MiniLM-L6-v2) para permitir
la recuperación de documentos relevantes en una arquitectura RAG.

Pasos que realiza:
1. Carga archivos .txt desde el directorio `data/products/`.
2. Genera embeddings de cada documento.
3. Crea un vectorstore FAISS.
4. Guarda el índice serializado en `index/vector_store.pkl`.

Uso:
    python index_documents.py

Requiere:
    - Los paquetes: langchain-community, sentence-transformers, faiss-cpu.
    - Archivos .txt en el directorio `data/products/`.
"""

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from pathlib import Path
import pickle

# 1. Cargar documentos desde archivos .txt en el directorio data/products/
docs = []
for file in Path("data/products").glob("*.txt"):
    # Usa TextLoader para convertir cada archivo en un objeto Document
    docs.extend(TextLoader(file).load())

# 2. Crear embeddings con modelo de HuggingFace (pequeño, rápido y preciso)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. Construir un vectorstore FAISS a partir de los documentos embebidos
vectorstore = FAISS.from_documents(docs, embeddings)

# 4. Guardar el índice generado para su uso en tiempo de consulta
with open("index/vector_store.pkl", "wb") as f:
    pickle.dump(vectorstore, f)
