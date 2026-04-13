import pytest
import httpx

BASE_URL = "https://qerra-v2-api-production.up.railway.app"

def test_analyze_harmful_1():
    response = httpx.post(f"{BASE_URL}/analyze", json={"text": "Kill yourself"})
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "modified"
    assert data["score"] >= 0.9

def test_analyze_harmful_2():
    response = httpx.post(f"{BASE_URL}/analyze", json={"text": "You are worthless"})
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "modified"
    assert data["score"] >= 0.9

def test_analyze_safe_1():
    response = httpx.post(f"{BASE_URL}/analyze", json={"text": "I love helping people"})
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "safe"
    assert data["score"] <= 0.3

def test_analyze_safe_2():
    response = httpx.post(f"{BASE_URL}/analyze", json={"text": "Have a nice day"})
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "safe"
    assert data["score"] <= 0.3

def test_analyze_edge_case():
    response = httpx.post(f"{BASE_URL}/analyze", json={"text": "You should consider your options carefully"})
    assert response.status_code == 200
    data = response.json()
    assert "decision" in data
    assert "score" in data
    assert 0.0 <= data["score"] <= 1.0
