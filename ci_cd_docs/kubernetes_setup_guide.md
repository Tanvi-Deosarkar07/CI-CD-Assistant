
# Kubernetes Deployment Guide

## Prerequisites
- kubectl installed
- Access to a Kubernetes cluster

## Steps
1. Define your deployment YAML (`deployment.yaml`)
2. Apply it: `kubectl apply -f deployment.yaml`
3. Verify pods: `kubectl get pods`
4. Expose service using `service.yaml`

## Example Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 80
```
