# Product Query Bot via RAG Pipeline

Este microservicio responde consultas sobre productos simulando una interacción conversacional. Utiliza una arquitectura RAG (Retrieval-Augmented Generation) compuesta por agentes independientes, embeddings semánticos y un modelo generativo de lenguaje (Gemini).

## Características

- Recuperación semántica basada en embeddings (HuggingFace MiniLM)
- Respuesta generativa utilizando Gemini 1.5 Flash (Google Generative AI)
- Separación clara entre agentes: Retriever y Responder
- Exposición de API REST vía FastAPI
- Almacenamiento vectorial con FAISS (local)
- Pruebas unitarias básicas
- Contenedor Docker incluido para despliegue rápido
- Variables de entorno configurables vía archivo `.env`

## Arquitectura general

1. El usuario envía una consulta a través del endpoint `/query`.
2. El agente `Retriever` consulta un índice vectorial para recuperar los documentos relevantes.
3. El agente `Responder` genera una respuesta basada únicamente en el contexto recuperado, usando Gemini.
4. Se retorna una respuesta textual simulando un flujo de conversación.

## Requisitos

- Python 3.10+
- Clave API de Google Generative AI (Gemini)
- Archivos `.txt` con contenido de productos en `data/products/`

## Instalación

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Crear un archivo `.env` con tu clave de API:

```
GEMINI_API_KEY=tu_clave_de_api
```

3. Indexar los documentos:

```bash
python index_documents.py
```

4. Ejecutar el servidor:

```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en: `http://localhost:8000/docs`

## Prueba rápida (curl)

```bash
curl -X POST http://localhost:8000/query   -H "Content-Type: application/json"   -d '{"user_id": "usuario1", "query": "¿Cuánta batería tienen los audífonos?"}'
```

## Estructura del proyecto

```
.
├── agents/                 # Agentes independientes (Retriever, Responder)
├── app/                    # Servidor FastAPI
├── data/products/          # Archivos de texto plano con descripciones de productos
├── index/                  # Índice embebido (FAISS serializado)
├── tests/                  # Pruebas unitarias
├── index_documents.py      # Script para generar el índice
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

## Pruebas

```bash
pytest
```

## Docker

```bash
docker build -t rag-bot .
docker run -p 8000:8000 rag-bot
```

## Consideraciones técnicas

- Se usó `sentence-transformers/all-MiniLM-L6-v2` para embeddings por su eficiencia y compatibilidad con FAISS.
- Se integró el modelo `models/gemini-1.5-flash-latest` vía `google-generativeai`, cargado mediante variable de entorno.
- El código sigue principios de modularidad y separación de responsabilidades por agente.
- Se optó por un diseño simple, reproducible y fácilmente extendible.

## Mejoras futuras

- Incorporar un agente de memoria para seguimiento conversacional
- Agregar soporte a múltiples fuentes de datos (PDF, CSV, web)
- Métricas de evaluación de recuperación y generación (precision@k, grounding score)
- Pipeline CI/CD para validación automática