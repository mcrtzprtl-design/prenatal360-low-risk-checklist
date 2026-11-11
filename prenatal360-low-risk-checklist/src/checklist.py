"""
PreNatal 360 Low-Risk Checklist - education only.
Not medical advice. Not a medical device.
"""
from datetime import date

DISCLAIMER = "Education only. Not medical advice. Seek in-person care for any warning sign."

RED_FLAGS = [
    "severe_preeclampsia",
    "uncontrolled_diabetes",
    "heavy_bleeding",
    "preterm_labor_signs",
    "severe_headache_vision_changes",
    "decreased_fetal_movement",
    "high_fever",
]

def gestational_week(lmp: str, today: str) -> int:
    """lmp and today as YYYY-MM-DD. Returns completed weeks, 0-42."""
    y1,m1,d1 = map(int, lmp.split("-"))
    y2,m2,d2 = map(int, today.split("-"))
    delta = (date(y2,m2,d2) - date(y1,m1,d1)).days
    if delta < 0:
        raise ValueError("LMP is in the future")
    return max(0, min(42, delta // 7))

def low_risk_screening(answers: dict) -> dict:
    """answers: dict of flag -> bool. Any True = not eligible for education-only."""
    flagged = [k for k in RED_FLAGS if answers.get(k)]
    if flagged:
        return {
            "eligible_for_education_only": False,
            "action": "Stop education content. Recommend urgent in-person care.",
            "flagged": flagged,
            "disclaimer": DISCLAIMER,
        }
    return {
        "eligible_for_education_only": True,
        "action": "Continue with low-risk education content",
        "flagged": [],
        "disclaimer": DISCLAIMER,
    }

def weekly_topic(week: int) -> str:
    if week <= 0:
        return "Confirm pregnancy with in-person care."
    if week <= 13:
        return "First trimester: nutrition, hydration, rest, gentle movement."
    if week <= 27:
        return "Second trimester: balanced nutrition, safe exercise, wellbeing."
    return "Third trimester: birth preparation, postpartum planning, warning signs education."
