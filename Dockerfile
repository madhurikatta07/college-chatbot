FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download NLTK data models needed for NLP processing
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Copy backend application code
COPY backend/ /app/

# Generate model.pkl from intents.json
RUN python train_model.py

EXPOSE 5000

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]