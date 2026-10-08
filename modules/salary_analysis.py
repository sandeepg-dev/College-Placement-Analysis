import streamlit as st
import pandas as pd


def render_salary_analysis(df: pd.DataFrame):
    """
    Analyzes and displays salary metrics, salary distribution, and department-wise average salary.
    """
    # ============================================
    # SALARY ANALYSIS
    # ============================================

    st.subheader("💰 Salary Analysis")

    # Consider only placed students with valid salary
    salary_df = df[
        (df["Placement_Status"].isin(["Yes", "yes", "Placed", "placed"])) &
        (df["Salary_INR"].notna()) &
        (df["Salary_INR"] > 0)
    ].copy()

    # Salary summary
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Salary",
            f"₹{salary_df['Salary_INR'].mean():,.0f}"
        )

    with col2:
        st.metric(
            "Minimum Salary",
            f"₹{salary_df['Salary_INR'].min():,.0f}"
        )

    with col3:
        st.metric(
            "Maximum Salary",
            f"₹{salary_df['Salary_INR'].max():,.0f}"
        )

    # Salary distribution
    st.subheader("📈 Salary Distribution")

    st.bar_chart(
        salary_df["Salary_INR"].value_counts().sort_index()
    )

    # Department-wise average salary
    st.subheader("🏢 Department-wise Average Salary")

    department_salary = (
        salary_df.groupby("Department")
        .agg(
            Average_Salary=("Salary_INR", "mean"),
            Students_Placed=("Salary_INR", "count")
        )
        .reset_index()
    )

    department_salary["Average_Salary"] = (
        department_salary["Average_Salary"].round(0)
    )

    st.dataframe(
        department_salary,
        use_container_width=True
    )

    st.bar_chart(
        department_salary.set_index("Department")[
            "Average_Salary"
        ]
    )

    st.write(
        "This analysis shows the salary distribution and "
        "average salary across different departments."
    )
