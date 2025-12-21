def normalize(text: str) -> str:
    text = text.lower().strip()

    # Basic plural handling
    if text.endswith("ies"):
        text = text[:-3] + "y"
    elif text.endswith("s") and len(text) > 3:
        text = text[:-1]

    return text