from cycle_patterns import CYCLE_PATTERNS


def carb_targets(weight_kg: float) -> dict:
    """
    Return carb targets (g/day) based on body weight.
    """
    return {
        "low": {
            "min": round(weight_kg * 0.8),
            "max": round(weight_kg * 1.2),
        },
        "mid": {
            "min": round(weight_kg * 1.6),
            "max": round(weight_kg * 2.2),
        },
        "high": {
            "min": round(weight_kg * 2.6),
            "max": round(weight_kg * 3.4),
        },
    }


def recommend_cycle(goal_diff_kg: float, eat_out: bool) -> str:
    """
    Recommend a carb cycling pattern.
    """
    if eat_out:
        return "low → mid → high → mid → low"

    if goal_diff_kg <= 5:
        return "low → mid → high → low → mid"

    return "low → mid → mid → high → low"

def choose_cycle(goal_diff_kg: float, eat_out: bool):
    if eat_out:
        return CYCLE_PATTERNS["social_friendly"]
    if goal_diff_kg <= 5:
        return CYCLE_PATTERNS["rapid_fat_loss"]
    return CYCLE_PATTERNS["balanced"]
