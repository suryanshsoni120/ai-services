from rules import KEYWORD_RULES
from utils import normalize

def score_text(text: str):
    text = normalize(text)
    scores = {}

    for category, rules in KEYWORD_RULES.items():
        score = 0

        for word in rules.get("strong", []):
            if word in text:
                score += 3   # stronger signal

        for word in rules.get("weak", []):
            if word in text:
                score += 1

        if score > 0:
            scores[category] = score

    return scores


def predict_category(text: str):
    if not text or not text.strip():
        return {"category": "Other", "confidence": 0.0}

    scores = score_text(text)

    if not scores:
        return {"category": "Other", "confidence": 0.3}

    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    # Confidence scaling
    confidence = min(0.95, 0.5 + best_score * 0.1)

    return {
        "category": best_category,
        "confidence": round(confidence, 2)
    }