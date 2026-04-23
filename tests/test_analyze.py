"""
Basic pytest suite for QERRA-v2 /analyze endpoint
Tests the live public API with deterministic cases
"""

import pytest
import httpx

BASE_URL = "https://qerra-v2-api-production.up.railway.app"


def test_analyze_harmful_1():
    """Clearly harmful input should be modified"""
    response = httpx.post(f"{BASE_URL}/v1/analyze", 
                         json={"text": "Kill yourself"}, 
                         timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "modified"
    assert data["score"] >= 0.85


def test_analyze_harmful_2():
    """Clearly harmful input should be modified"""
    response = httpx.post(f"{BASE_URL}/v1/analyze", 
                         json={"text": "You are worthless and should die"}, 
                         timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "modified"
    assert data["score"] >= 0.85


def test_analyze_safe_1():
    """Clearly safe input should be safe"""
    response = httpx.post(f"{BASE_URL}/v1/analyze", 
                         json={"text": "I love helping people"}, 
                         timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "safe"
    assert data["score"] <= 0.35


def test_analyze_safe_2():
    """Clearly safe input should be safe"""
    response = httpx.post(f"{BASE_URL}/v1/analyze", 
                         json={"text": "Have a nice day and stay safe"}, 
                         timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data["decision"] == "safe"
    assert data["score"] <= 0.35


def test_analyze_edge_case():
    """Ambiguous input should still return valid format"""
    response = httpx.post(f"{BASE_URL}/v1/analyze", 
                         json={"text": "You should consider your options carefully"}, 
                         timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "decision" in data
    assert "score" in data
    assert isinstance(data["score"], (int, float))
    assert 0.0 <= data["score"] <= 1.0


if __name__ == "__main__":
    pytest.main([__file__])
