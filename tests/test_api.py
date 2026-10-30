
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    payload = {
        "tenure_months": 5,
        "monthly_fee": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    result = response.json()
    assert "churn_probability" in result
    assert 0 <= result["churn_probability"] <= 1


def test_missing_field():
    payload = {
        "tenure_months": 5,
        "monthly_fee": 89.9,
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_model_loaded():
    from src.app.main import model

    assert model is not None


def test_prediction_is_deterministic():
    payload = {
        "tenure_months": 5,
        "monthly_fee": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response1 = client.post("/predict", json=payload)
    response2 = client.post("/predict", json=payload)

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert (
        response1.json()["churn_probability"]
        == response2.json()["churn_probability"]
    )


def test_negative_tenure_rejected():
    payload = {
        "tenure_months": -1,
        "monthly_fee": 89.9,
        "contract": "month-to-month",
        "internet_service": "fiber",
        "support_calls": 3,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
