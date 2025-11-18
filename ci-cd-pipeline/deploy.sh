#!/bin/bash

echo "Building Docker image..."
docker build -t kjy901006/cd-pipeline:latest .

echo "Pushing Docker image to Docker Hub..."
docker push kjy901006/cd-pipeline:latest

echo "Applying Kubernetes deployment..."
kubectl apply -f ./k8s/deployment.yml

echo "Checking Kubernetes pod status..."
kubectl get pods
