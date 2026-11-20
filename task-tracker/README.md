# Personal Task Tracker

A simple containerized task tracker application built and operated with Docker, GitHub Actions, and Kubernetes.

## Team Roles
* **App / Content:** [Teammate Name]
* **Container / Integration:** [Teammate Name]
* **CI/CD:** [Teammate Name]
* **Kubernetes / Operations:** [Teammate Name]

## Quick Start (Local)
```bash
# Run locally with Docker Compose
docker compose up --build
```

## Kubernetes Deployment
```bash
# Create local cluster and apply manifests
kind create cluster --name task-tracker
kubectl apply -f k8s/
```
