import random
from meal_templates import (
    BREAKFAST,
    LOW_CARB_MEALS,
    MID_CARB_MEALS,
    HIGH_CARB_MEALS,
)

MEAL_MAP = {
    "low": LOW_CARB_MEALS,
    "mid": MID_CARB_MEALS,
    "high": HIGH_CARB_MEALS,
}

def generate_day_plan(day_type: str):
    meals = MEAL_MAP[day_type]
    return {
        "breakfast": BREAKFAST,
        "lunch": random.choice(meals["lunch"]),
        "dinner": random.choice(meals["dinner"]),
    }


def generate_multi_day_plan(cycle: list):
    plan = []
    for i, day_type in enumerate(cycle):
        plan.append({
            "day": i + 1,
            "type": day_type,
            "meals": generate_day_plan(day_type)
        })
    return plan
