import streamlit as st
import pandas as pd


def calculate_key_metrics(filtered_df: pd.DataFrame) -> dict:
    """
    Calculates summary placement and salary metrics based on the filtered data.
    """
    total_students = len(filtered_df)

    placed_students = len(
        filtered_df[
            filtered_df["Placement_Status"] == "Placed"
        ]
    )

    if total_students > 0:
        placement_percentage = (
            placed_students / total_students
        ) * 100
    else:
        placement_percentage = 0

    if "Salary_INR" in filtered_df.columns:
        placed_salary = filtered_df.loc[
            filtered_df["Placement_Status"] == "Placed",
            "Salary_INR"
        ]

        average_salary = (
            placed_salary.mean()
            if len(placed_salary) > 0
            else 0
        )

        highest_salary = (
            placed_salary.max()
            if len(placed_salary) > 0
            else 0
        )
    else:
        average_salary = 0
        highest_salary = 0

    return {
        "total_students": total_students,
        "placed_students": placed_students,
        "placement_percentage": placement_percentage,
        "average_salary": average_salary,
        "highest_salary": highest_salary,
    }


def render_overview(filtered_df: pd.DataFrame) -> dict:
    """
    Renders the key metrics cards and the dataset preview table.
    Returns:
        dict: The calculated metrics dictionary for downstream use.
    """
    metrics = calculate_key_metrics(filtered_df)

    # -------------------------------------------------
    # DASHBOARD METRICS
    # -------------------------------------------------
    st.header("📊 Placement Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "👨‍🎓 Total Students",
        metrics["total_students"]
    )

    col2.metric(
        "✅ Placed Students",
        metrics["placed_students"]
    )

    col3.metric(
        "📈 Placement %",
        f"{metrics['placement_percentage']:.1f}%"
    )

    col4.metric(
        "💰 Average Salary",
        f"₹{metrics['average_salary']:,.0f}"
    )

    col5.metric(
        "🏆 Highest Salary",
        f"₹{metrics['highest_salary']:,.0f}"
    )

    st.divider()

    # -------------------------------------------------
    # DATASET PREVIEW
    # -------------------------------------------------
    st.header("📋 Dataset Preview")

    st.dataframe(
        filtered_df.head(10),
        use_container_width=True
    )

    return metrics
