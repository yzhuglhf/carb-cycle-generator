import random
import streamlit as st

from carb_rules import carb_targets, recommend_cycle, choose_cycle
from meal_templates import (
    BREAKFAST,
    LOW_CARB_MEALS,
    MID_CARB_MEALS,
    HIGH_CARB_MEALS,
)
from plan_generator import generate_multi_day_plan

st.title("🥗 Carb Cycle Meal Planner")

weight = st.number_input("Current weight (kg)", value=49.0)
goal_weight = st.number_input("Goal weight (kg)", value=45.0)
eat_out = st.checkbox("I eat out frequently")

targets = carb_targets(weight)
cycle = choose_cycle(weight - goal_weight, eat_out)

st.subheader("📊 Carb Targets (g/day)")
st.write(targets)

st.subheader("🔁 Carb Cycle Pattern")
st.write(cycle)

plan = generate_multi_day_plan(cycle)

st.subheader("📅 Meal Plan")

for day in plan:
    st.markdown(f"### Day {day['day']} — {day['type'].upper()} carb")
    st.write("**Breakfast**")
    for item in day["meals"]["breakfast"]:
        st.write("-", item)
    st.write("**Lunch**")
    st.write(day["meals"]["lunch"])
    st.write("**Dinner**")
    st.write(day["meals"]["dinner"])
