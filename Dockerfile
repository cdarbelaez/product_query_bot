FROM python:3.10-slim

WORKDIR /app

# Copiamos primero las dependencias para aprovechar cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código, incluyendo .env si se usa
COPY . .

# (opcional) establece la variable si no se usa .env dentro del contenedor
# ENV GEMINI_API_KEY=clave_aquí

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]