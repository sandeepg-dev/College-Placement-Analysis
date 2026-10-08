import streamlit as st


def render_insights(metrics: dict):
    """
    Displays key insights summary bullet points and success status banner.
    """
    # -------------------------------------------------
    # FINAL INSIGHTS
    # -------------------------------------------------
    st.header("💡 Key Insights")

    total_students = metrics["total_students"]
    placed_students = metrics["placed_students"]
    placement_percentage = metrics["placement_percentage"]
    average_salary = metrics["average_salary"]
    highest_salary = metrics["highest_salary"]

    st.write(
        f"- The current dataset contains **{total_students} students** "
        "after applying the selected filters."
    )

    st.write(
        f"- **{placed_students} students** are placed."
    )

    st.write(
        f"- The placement percentage is "
        f"**{placement_percentage:.1f}%**."
    )

    if average_salary > 0:
        st.write(
            f"- The average salary among placed students is "
            f"**₹{average_salary:,.0f}**."
        )

    if highest_salary > 0:
        st.write(
            f"- The highest recorded salary is "
            f"**₹{highest_salary:,.0f}**."
        )

    st.success(
        "EDA Dashboard loaded successfully! 🎉"
    )
