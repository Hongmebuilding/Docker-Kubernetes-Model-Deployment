#!/bin/bash


# 변수 설정
DEPLOYMENTS=("nginx-deployment.yaml" "web-deployment.yaml")
SERVICES=("nginx-service.yaml" "web-service.yaml")


# Kubernetes 리소스 삭제 (기존 리소스가 있다면)
echo "Deleting existing resources..."
for deployment in "${DEPLOYMENTS[@]}"; do
    kubectl delete -f $deployment --ignore-not-found
done


for service in "${SERVICES[@]}"; do
    kubectl delete -f $service --ignore-not-found
done


# Kubernetes 리소스 생성
echo "Applying new resources..."
for deployment in "${DEPLOYMENTS[@]}"; do
    kubectl apply -f $deployment
done


for service in "${SERVICES[@]}"; do
    kubectl apply -f $service
done


echo "Deployment completed successfully!"


