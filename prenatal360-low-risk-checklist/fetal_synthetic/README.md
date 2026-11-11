# Fetal Monitoring - Synthetic Data Only

> ⚠️ SYNTHETIC DATA ONLY. NO real patient data. NOT clinical. NOT a medical device.
> Do NOT use this to monitor, diagnose, or treat any real pregnancy.

## What is this?

A generator that creates **fake, simulated** fetal monitoring signals to prototype and test a future AI:

- Synthetic fetal heart rate: 110-160 bpm simulated, with variability
- Synthetic fetal movement counts
- Gestational week, duration, sample rate
- Signal quality label **for testing the pipeline only** - never a clinical label

## What it is NOT

- Not real data
- Not a diagnosis of fetal wellbeing
- Not a replacement for clinical monitoring (CTG, ultrasound, in-person care)
- No personal data, no names, no dates of real patients

## Quick start

```python
from fetal_synthetic.generator import generate_session

session = generate_session(gestational_week=32, duration_seconds=60, seed=42)
print(session["fetal_heart_rate_bpm"][:10])
```

## Rules for contributors

1. Never add real patient data, audio, images, or clinical records.
2. Never add a clinical label like "healthy / at risk".
3. Keep the synthetic-only disclaimer in every file.
4. If you want to propose a real-data study, it needs ethics approval + informed consent + regulatory review - discuss in an issue first, do NOT open a PR with data.
