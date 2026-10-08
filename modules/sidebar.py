import streamlit as st
import pandas as pd


def render_sidebar(df: pd.DataFrame):
    """
    Renders sidebar filters for Department and Gender.
    Returns:
        tuple: (filtered_df, selected_department, selected_gender)
    """
    st.sidebar.header("🔎 Filters")

    departments = ["All"] + sorted(df["Department"].unique().tolist())

    selected_department = st.sidebar.selectbox(
        "Select Department",
        departments
    )

    genders = ["All"] + sorted(df["Gender"].unique().tolist())

    selected_gender = st.sidebar.selectbox(
        "Select Gender",
        genders
    )

    filtered_df = df.copy()

    if selected_department != "All":
        filtered_df = filtered_df[
            filtered_df["Department"] == selected_department
        ]

    if selected_gender != "All":
        filtered_df = filtered_df[
            filtered_df["Gender"] == selected_gender
        ]

    return filtered_df, selected_department, selected_gender
