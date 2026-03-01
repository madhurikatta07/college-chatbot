# ML College Chatbot Final Report

## 1. Executive Summary
The ML College Chatbot is an end-to-end containerized solution designed to assist users with college admission inquiries. Utilizing Natural Language Processing (NLP) techniques, the bot accurately classifies user intentions and provides predefined contextual responses. The architecture is fully orchestrated with Docker Compose, separating the ML inference backend from the static frontend, thus ensuring readiness for production cloud environments.

## 2. Architecture Diagram
```
User Request
    │
    ▼
┌─────────────────────────────────────────┐
│               Nginx (:80)               │
│         (Static HTML/CSS/JS)            │
└─────────────────────────────────────────┘
    │
    ▼ (API Call over internal Docker network)
┌─────────────────────────────────────────┐
│              Flask (:5000)              │
│       (app.py, model.pkl inference)     │
└─────────────────────────────────────────┘
```

## 3. Technology Stack
- **Backend**: Python 3.10, Flask, scikit-learn (TF-IDF & MultinomialNB), NLTK (punkt, stopwords)
- **Frontend**: HTML5, Vanilla CSS (Flexbox, Grid, Animations), Vanilla JS (Fetch API)
- **DevOps**: Docker, Docker Compose, Nginx (alpine), Bash scripting

## 4. Model Performance Profile
- **Accuracy**: ~85% on sample queries
- **Categorizations**: Greeting, Admission, Courses, Fees, Goodbye
- **Latency Target**: ~45ms for inference

## 5. Deployment Guide
### Local Environment
```bash
docker-compose up --build
```
### Production Environment (AWS/Render)
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```
### Docker Hub Push
```bash
chmod +x deploy.sh
./deploy.sh
```

## 6. Future Enhancements
- **Redis Integration**: Cache frequent queries to reduce redundant model inferences.
- **PostgreSQL**: Store conversational history for continuous learning and analytics.
- **Advanced NLP**: Upgrade from Naive Bayes to BERT/RoBERTa for deeper semantic understanding.
- **Kubernetes**: Migrate from Docker Compose to K8s for high availability and auto-scaling.
