def is_relevant(text: str) -> bool:
    keywords = ["tour", "concert", "venue", "performance", "guest", "schedule", "show", "artist"]
    text_lower = text.lower()

    return any(keyword in text_lower for keyword in keywords)