def rate_note(note: int) -> str:
    if note < 10:
        return "unsuccessful"
    if note < 12:
        return "acceptable"
    if note < 14:
        return "good"
    if note < 16:
        return "verygood"
    if note <= 20:
        return "excellent"

