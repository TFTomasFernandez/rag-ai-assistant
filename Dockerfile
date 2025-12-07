FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos dependencias
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto
COPY . .

# Puerto que exponemos
EXPOSE 8000

# Comando para levantar la API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
