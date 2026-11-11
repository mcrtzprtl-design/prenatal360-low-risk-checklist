from fetal_synthetic.generator import generate_session
s = generate_session(gestational_week=34, duration_seconds=30, seed=1)
print("Synthetic only:", s["synthetic"])
print("HR samples:", len(s["fetal_heart_rate_bpm"]))
print(s["fetal_heart_rate_bpm"][:8])
