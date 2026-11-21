# Personal Task Tracker

A simple containerized task tracker application built and operated with Docker, GitHub Actions, and Kubernetes.

## Team Roles
* **App / Content:** 
* **Container / Integration:** Frank DeRango
* **CI/CD:** Ivette Garia
* **Kubernetes / Operations:** Frank Rosales-Franco

## Application Features
- View existing tasks
- Add new tasks
- Mark tasks as completed

## Prerequisites
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

## Running with Docker
Build the Docker image:
```bash
docker build -t task-it:local .
```

Run the Docker container:
```bash
docker run --rm -p 5000:5000 task-it:local
```
Open http://localhost:5000 in your browser.

# To verify that app is running correctly, open another Terminal window and run:
curl http://localhost:5000/health

Expected response should be:
```bash
{"status":"ok"}
```

- This Dockerfile uses Python 3.12 and runs the application as a non-root user.

## CI/CD Pipeline

GitHub Actions is used to automate testing and building the Task-It Docker image.

The workflow is located in `.github/workflows/task-it.yml`.

The workflow runs when:

- Changes are pushed to the main branch.
- A pull request is created targeting main.
- The workflow is manually triggered.

The CI/CD pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs the required dependencies and pytest.
4. Runs automated tests for the Flask application.
5. Builds the Docker image after the tests pass.
6. Publishes the Docker image to GitHub Container Registry (GHCR) with a SHA-based tag when changes are pushed to main.

The automated tests check the health endpoint, homepage, and task creation.

To run the tests locally:

```bash
python3 -m pip install -r requirements.txt pytest
python3 -m pytest -v tests/
```

The workflow builds the Docker image for pull requests but only publishes it to GHCR on pushes to main.

## Kubernetes Deployment
```json
# Create local cluster and apply manifests
kind create cluster --name task-tracker
kubectl apply -f k8s/
```
