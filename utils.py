import re

def normalize(text: str) -> str:
    """
    Normalizes transaction descriptions for rule-based matching.
    """
    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove special characters (keep letters & numbers)
    text = re.sub(r"[^a-z0-9 ]", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text