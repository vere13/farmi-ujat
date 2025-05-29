FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará Flet (puede ser 8550 u otro)
EXPOSE 8550

# Ejecuta tu sistema
CMD ["python", "main.py"]
