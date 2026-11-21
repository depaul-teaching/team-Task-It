# Personal Task Tracker

A simple containerized task tracker application built and operated with Docker, GitHub Actions, and Kubernetes.

## Team Roles
* **App / Content:** 
* **Container / Integration:** Frank DeRango
* **CI/CD:** Ivette Garia
* **Kubernetes / Operations:** Frank Rosales-Franco

##Application Features
- View existing tasks
- Add new tasks
- Mark tasks as completed

##Prerequisites
# Before running project, make sure to install:
- Git 
- Python 3.12
- Docker

# For kubernetes, install:
- kubectl
- kind

## Quick Start (Local)
```bash
# Run locally with Docker Compose
docker compose up --build
```
Open http://localhost:5000 in your browser.

## Kubernetes Deployment
```bash
# Create local cluster and apply manifests
kind create cluster --name task-tracker
kubectl apply -f k8s/
```
