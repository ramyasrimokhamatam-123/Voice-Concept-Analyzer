def filler_word_ratio(text):
    fillers = [
        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "you know"
    ]

    words = text.lower().split()

    if len(words) == 0:
        return 0

    filler_count = 0

    for word in words:
        if word in fillers:
            filler_count += 1

    return filler_count / len(words)