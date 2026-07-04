def evaluate_understanding(similarity, filler_ratio, audio):
    score = 0

    # Semantic similarity score
    if similarity >= 70:
        score += 50
    elif similarity >= 40:
        score += 30
    else:
        score += 10

    # Filler word score
    if filler_ratio < 0.05:
        score += 20
    else:
        score += 10

    # Pause ratio score
    if audio["pause_ratio"] < 0.25:
        score += 15
    else:
        score += 5

    # RMS energy score
    if audio["rms_energy"] > 0.01:
        score += 15
    else:
        score += 5

    if score >= 80:
        return score, "Strong Understanding", "#2ecc71"
    elif score >= 50:
        return score, "Moderate Understanding", "#f39c12"
    else:
        return score, "Poor Understanding", "#e74c3c"