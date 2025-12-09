import json

def test_all_vectors_have_correct_verdict():
    vectors = [
        "v001_financial_28k_reclamation.json",
        "v002_family_severance.json",
        "v003_business_dissolution.json",
        "v004_employment_friendship_2025.json",
        "v005_living_environment.json",
        "v006_family_origin_survival_chain.json",
        "v007_medical_family_misdiagnosis.json",
        "v008_global_climate_inaction.json"
    ]
    
    for v in vectors:
        with open(f"vectors/{v}") as f:
            data = json.load(f)
        assert "100% match" in data["engine_verdict"], f"{v} failed!"
