# PreNatal 360® Low-Risk Checklist

An open-source, education-only toolkit for low-risk pregnancy and postpartum guidance.

**Built by MJV Health Ecosystem® in Cajamarca, Peru.**

> ⚠️ EDUCATION ONLY. This is NOT medical advice, diagnosis, treatment, or emergency care.
> It does NOT replace prenatal care. If there is any warning sign, seek in-person care immediately.

## What it does

1. **Gestational age calculator** - from last menstrual period (LMP) to current week
2. **Low-risk screening checklist** - yes/no questions to decide if education-only content is appropriate, or if urgent in-person care is needed
3. **Weekly education templates** - week-by-week education, nutrition, gentle exercise, wellbeing (low-risk only)

## Who is it for?

- Prenatal educators
- Developers building pregnancy apps in Spanish / English
- Small clinics that need a safe, education-first starting point

## Quick start (Python)

```python
from src.checklist import gestational_week, low_risk_screening

week = gestational_week("2026-08-01", "2026-11-11")
print(week)  # e.g. 14

result = low_risk_screening({
    "severe_preeclampsia": False,
    "uncontrolled_diabetes": False,
    "heavy_bleeding": False,
    "preterm_labor_signs": False,
    "severe_headache_vision_changes": False,
})
print(result)
# {"eligible_for_education_only": True, "action": "Continue with low-risk education content"}
```

## Quick start (JavaScript)

See `examples/example.js`

## Safety rules (non-negotiable)

- Only for low-risk pregnancy / postpartum
- Any red flag = stop education content, recommend urgent in-person care
- No diagnosis, no treatment recommendation, no emergency use
- Always show the disclaimer and a local emergency number

## Contributing

See CONTRIBUTING.md. Good first issues: translations, more weekly templates, tests.

## License

MIT - see LICENSE

## Part 2 - Fetal Monitoring (Synthetic Data Only)

See `fetal_synthetic/README.md`. Generates fake fetal heart rate / movement signals for testing only. No real patient data, no clinical use.
