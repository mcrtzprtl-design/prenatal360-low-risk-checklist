"""
PreNatal 360 Fetal Monitoring - SYNTHETIC DATA ONLY.

Generates fake but realistic fetal monitoring signals for testing / research.
NO real patient data. NO clinical use. NOT a medical device.
NOT for diagnosis, monitoring, or treatment of any real pregnancy.

Use: to train / test models, to learn signal shapes, to prototype.
Any real use requires ethics approval, informed consent, and regulatory clearance.
"""
import random
import math
from datetime import datetime, timedelta

DISCLAIMER = "Synthetic data only. Not clinical. Not medical advice. Do not use on real patients."

def generate_fetal_heart_rate(duration_seconds=60, sample_rate_hz=4, gestational_week=32, seed=None):
    """
    Returns a list of synthetic fetal heart rate samples in bpm.
    Normal simulated range 110-160 bpm, with gentle variability.
    This is a simulation, not a real measurement.
    """
    if seed is not None:
        random.seed(seed)
    if not (20 <= gestational_week <= 42):
        raise ValueError("gestational_week must be 20-42 for this simulator")
    n = int(duration_seconds * sample_rate_hz)
    base = 140 + (gestational_week - 32) * 0.3
    samples = []
    for i in range(n):
        t = i / sample_rate_hz
        # slow wave + variability + small noise, all synthetic
        value = base + 8 * math.sin(t * 0.3) + 4 * math.sin(t * 1.1) + random.gauss(0, 2)
        value = max(110, min(160, round(value, 1)))
        samples.append(value)
    return samples

def generate_session(gestational_week=32, duration_seconds=60, seed=None):
    """One synthetic session: metadata + heart rate + movement counts. All fake."""
    if seed is not None:
        random.seed(seed)
    start = datetime(2026, 1, 1, 10, 0, 0) + timedelta(days=random.randint(0, 30))
    hr = generate_fetal_heart_rate(duration_seconds, 4, gestational_week, seed=seed)
    movements = random.randint(0, 12)  # synthetic, per session
    # Signal quality label is for testing the pipeline, NOT a clinical label
    signal_quality = "good" if len(hr) > 100 else "noisy"
    return {
        "synthetic": True,
        "disclaimer": DISCLAIMER,
        "gestational_week": gestational_week,
        "duration_seconds": duration_seconds,
        "sample_rate_hz": 4,
        "session_start_fake": start.isoformat(),
        "fetal_heart_rate_bpm": hr,
        "fetal_movements_synthetic_count": movements,
        "signal_quality_for_testing_only": signal_quality,
        "clinical_label": None,  # intentionally never set - this is not a diagnosis
    }

if __name__ == "__main__":
    s = generate_session(gestational_week=32, duration_seconds=10, seed=42)
    print(s["disclaimer"])
    print("samples:", len(s["fetal_heart_rate_bpm"]), "first 10:", s["fetal_heart_rate_bpm"][:10])
    print("movements (synthetic):", s["fetal_movements_synthetic_count"])
