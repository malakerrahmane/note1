def rate_note(note: int) -> str:
    if note < 10:
      return "unsuccessful"
    if note == 10 or note == 11:
      return "acceptable"
    if  12 <= note  < 14:
      return "good"
    return "verygood"