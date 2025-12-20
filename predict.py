from model import embed, category_embeddings
from rules import KEYWORD_RULES
import numpy as np

CONFIDENCE_THRESHOLD = 0.45

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def rule_based_category(text):
    text_lower = text.lower()
    for category, keywords in KEYWORD_RULES.items():
        for keyword in keywords:
            if keyword in text_lower:
                return category
    return None

def predict_category(text):
    # 1️⃣ RULE-BASED (HIGH CONFIDENCE)
    rule_category = rule_based_category(text)
    if rule_category:
        return rule_category, 0.9

    # 2️⃣ AI-BASED
    text_vec = embed(text)
    best_cat = "Other"
    best_score = 0

    for cat, vec in category_embeddings.items():
        score = cosine_similarity(text_vec, vec)
        if score > best_score:
            best_score = score
            best_cat = cat

    if best_score < CONFIDENCE_THRESHOLD:
        return "Other", round(float(best_score), 2)

    return best_cat, round(float(best_score), 2)