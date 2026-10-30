# AI381 Lab 2 · Containerization & CI/CD

**Machine Learning Operations (MLOps)**

[![AI381 CI](https://github.com/razanmomani119/ai381-lab2/actions/workflows/ci.yml/badge.svg)](https://github.com/razanmomani119/ai381-lab2/actions/workflows/ci.yml)

## Project Overview

This project converts a customer churn prediction model into a containerized API with automated testing and a CI/CD pipeline.

The application uses a Logistic Regression model to predict the probability of customer churn based on customer information.

## Project Structure

| File | Description |
|---|---|
| `src/train/train.py` | Trains the machine learning model |
| `src/app/main.py` | FastAPI application |
| `tests/test_api.py` | Automated API and model tests |
| `model.joblib` | Trained machine learning model |
| `churn_v2.csv` | Dataset used for training |
| `sample_request.json` | Example prediction input |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Multi-stage Docker configuration |
| `.github/workflows/ci.yml` | GitHub Actions CI/CD workflow |

## Technologies

- Python 3.14
- Pandas
- Scikit-learn
- FastAPI
- Pydantic
- Pytest
- Docker
- GitHub Actions
- Trivy
- GitHub Container Registry (GHCR)

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks application health |
| POST | `/predict` | Returns the predicted churn probability |

### Example Request

```json
{
  "tenure_months": 12,
  "monthly_fee": 85.5,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic",
  "support_calls": 4
}
```

### Example Response

```json
{
  "churn_probability": 0.895
}
```

## Run with Docker

Run the application with one command:

```bash
docker run --rm -p 8001:8001 ghcr.io/razanmomani119/ai381-lab2@sha256:25e47caf6c268a114d8c9a9ea5a27f9caa474f4c77640a793b262c3c3da32421
```

After starting the container, access:

- Health check: http://localhost:8001/health
- API documentation: http://localhost:8001/docs

## Automated Testing

Tests are executed using Pytest.

The test suite includes six tests:

1. API health endpoint.
2. Prediction endpoint.
3. Missing input fields validation.
4. Model loading.
5. Deterministic predictions.
6. Rejection of negative `tenure_months` values.

Run the tests locally:

```bash
python -m pytest -v
```

## CI/CD Pipeline

GitHub Actions automates the following stages:

1. Checkout the repository.
2. Set up Python.
3. Install project dependencies.
4. Run automated tests.
5. Build the Docker image.
6. Scan the image using Trivy.
7. Publish the image to GitHub Container Registry on pushes to `main`.

The workflow runs tests on pull requests and pushes to the main branch.

Both the `test` and `docker` jobs must pass before merging pull requests into `main`.

## Docker Image

**GitHub Container Registry:**

`ghcr.io/razanmomani119/ai381-lab2`

**Image Tag:**

`8fecd6f007004a4ea92dda7e031141dde1023b97`

**Image Digest:**

`sha256:25e47caf6c268a114d8c9a9ea5a27f9caa474f4c77640a793b262c3c3da32421`

## Branch Protection

The `main` branch is protected with the following rules:

- Pull requests are required before merging.
- The `test` status check must pass.
- The `docker` status check must pass.

## Repository

[AI381 Lab 2 – GitHub Repository](https://github.com/razanmomani119/ai381-lab2)

---

**Machine Learning Operations (MLOps)**
