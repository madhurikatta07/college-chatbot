# ML College Chatbot

An end-to-end containerized NLP chatbot designed to assist users with college admission inquiries. This project features a Flask backend for inference and an Nginx frontend for a seamless user experience.

## ✨ Features
- **Intent Classification**: Uses `scikit-learn` (MultinomialNB) to categorize queries.
- **Production Ready**: Backend served via `Gunicorn` and frontend via `Nginx`.
- **Cloud Compatible**: Optimized for deployment on Render and Docker Hub.
- **Responsive UI**: Clean, animated chat interface.

## 🏗️ Architecture
```
User Request
    │
    ▼
┌───────────────────────────┐
│       Nginx (:80)         │ (Static Frontend)
└───────────────────────────┘
    │
    ▼
┌───────────────────────────┐
│     Gunicorn (:5000)      │ (Flask Backend)
└───────────────────────────┘
```

## 🛠️ Technology Stack
- **Backend**: Python 3.10, Flask, Gunicorn, scikit-learn, NLTK
- **Frontend**: HTML5, Vanilla CSS, Vanilla JS
- **DevOps**: Docker, Docker Compose, GitHub Actions, Nginx

## 🚀 Deployment Guide

### Local Development
Run the project locally using Docker Compose:
```bash
docker-compose up --build
```
Access the chatbot at `http://localhost:8080`.

### Production (Docker)
Run the production-optimized stack:
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```
Access the chatbot at `http://localhost`.

### Deployment to Render
1. **Backend**: Create a Web Service on Render using the `Dockerfile`. Ensure the `PORT` environment variable is set (Render handles this automatically).
2. **Frontend**: Create a Static Site on Render, pointing to the `frontend/` directory.

### Docker Hub
Push the backend image:
```bash
docker build -t your-username/college-chatbot-backend:latest .
docker push your-username/college-chatbot-backend:latest
```

## 📈 Model Profile
- **Accuracy**: ~85%
- **Tags**: Greeting, Admission, Courses, Fees, Goodbye
- **Inference Latency**: < 50ms
