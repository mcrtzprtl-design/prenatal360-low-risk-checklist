from fetal_synthetic.generator import generate_session, generate_fetal_heart_rate
def test_synthetic_flag():
    s = generate_session(gestational_week=32, duration_seconds=10, seed=1)
    assert s["synthetic"] == True
    assert s["clinical_label"] is None
def test_hr_range():
    hr = generate_fetal_heart_rate(10, 4, 32, seed=1)
    assert all(110 <= x <= 160 for x in hr)
