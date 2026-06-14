FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Garante privilégios mínimos rodando com usuário comum (não-root)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

ENV FLASK_APP=run.py
CMD ["python", "run.py"]