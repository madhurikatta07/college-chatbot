#!/bin/bash
set -e

echo "🚀 Building College Chatbot for production..."

# Version tagging
VERSION=$(date +%Y%m%d-%H%M%S)
IMAGE_NAME="madhuri007/college-chatbot-backend"

# Build backend
docker build -t ${IMAGE_NAME}:latest -t ${IMAGE_NAME}:${VERSION} .

# Login to Docker Hub
echo "🔐 Logging in..."
docker login

# Push images
echo "📤 Pushing to Docker Hub..."
docker push ${IMAGE_NAME}:latest
docker push ${IMAGE_NAME}:${VERSION}

echo "✅ Deployed: ${IMAGE_NAME}:${VERSION}"

# Optional: Deploy to cloud
# ssh user@server "docker pull ${IMAGE_NAME}:latest && docker-compose up -d"
