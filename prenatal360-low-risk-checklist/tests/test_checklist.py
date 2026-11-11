from src.checklist import gestational_week, low_risk_screening
def test_week():
    assert gestational_week("2026-08-01","2026-08-08") == 1
def test_red_flag_blocks():
    r = low_risk_screening({"heavy_bleeding": True})
    assert r["eligible_for_education_only"] == False
def test_no_flag_ok():
    r = low_risk_screening({})
    assert r["eligible_for_education_only"] == True
