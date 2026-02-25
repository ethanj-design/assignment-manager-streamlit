import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

st.divider()

assignment = [
    {
    "id": "HW1",
    "title":"Intro to DB",
    "description": "Basics of DB design.",
    "points": 100,
    "type": "Homework"
    },
    {
    "id": "HW2",
    "title":"Normalization",
    "description": "Normalize table designs.",
    "points": 100,
    "type": "Lab"
    },
]

# Add New Assignment
st.markdown("### Add New Assignment")

# inputs
title = st.text_input("Title",placeholder="ex: Homework 1",
                        help="This is the name of the assignment.")
description = st.text_area("Description",placeholder="ex: Introduction to DB Design.",
                                help="This is the smaller details of the assignment.")
points = st.number_input("Point Value",placeholder="ex: 100", help="How many points is this worth?")
assign_type2 = st.selectbox("Type",["Homework", "Lab", "Other"])

if assign_type2 == "Other":
    assign_type2 = st.text_input("Other", placeholder="What type of assignment?")

with st.expander("Assignment Preview",expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save Assignment",width="stretch")
if btn_save:
    st.warning("Working on it!")