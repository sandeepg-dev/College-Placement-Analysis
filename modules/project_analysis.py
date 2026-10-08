import streamlit as st
import pandas as pd


def render_project_analysis(df: pd.DataFrame):
    """
    Analyzes and displays placement performance based on number of projects completed:
    - Project count summary table
    - Placement percentage bar chart
    """
    # ============================================
    # PROJECTS VS PLACEMENT ANALYSIS
    # ============================================

    st.subheader("📊 Projects vs Placement Analysis")

    # Clean placement status values
    df["Placement_Status"] = (
        df["Placement_Status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Create project-wise summary
    project_placement = (
        df.groupby("Projects_Count")
        .agg(
            Total_Students=("Student_ID", "count"),
            Placed=("Placement_Status", 
                    lambda x: x.isin(["yes", "placed", "true"]).sum()),
            Not_Placed=("Placement_Status", 
                        lambda x: x.isin(["no", "not placed", "false"]).sum())
        )
        .reset_index()
    )

    # Calculate placement percentage
    project_placement["Placement_Percentage"] = (
        project_placement["Placed"]
        / project_placement["Total_Students"]
        * 100
    ).round(2)

    # Display summary table
    st.dataframe(
        project_placement,
        use_container_width=True
    )

    # Chart
    st.subheader("📈 Placement Percentage by Number of Projects")

    st.bar_chart(
        project_placement.set_index("Projects_Count")[
            "Placement_Percentage"
        ]
    )

    st.write(
        "This analysis shows the placement percentage "
        "for students based on the number of projects completed."
    )
