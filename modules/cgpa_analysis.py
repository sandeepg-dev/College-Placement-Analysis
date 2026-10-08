import streamlit as st
import pandas as pd


def render_cgpa_analysis(df: pd.DataFrame):
    """
    Analyzes and displays placement percentage across CGPA score ranges.
    """
    # ==========================================
    # CGPA vs Placement Analysis
    # ==========================================

    st.subheader("📈 CGPA vs Placement Analysis")

    # Convert Placement Status into numeric values
    status = df["Placement_Status"].astype(str).str.strip().str.lower()

    df["Placement_Numeric"] = status.isin(["yes", "placed"]).astype(int)

    # Create CGPA groups
    df["CGPA_Group"] = pd.cut(
        df["CGPA"],
        bins=[0, 6, 7, 8, 9, 10],
        labels=["Below 6", "6 - 7", "7 - 8", "8 - 9", "9 - 10"],
        include_lowest=True
    )

    # Calculate placement percentage
    cgpa_placement = (
        df.groupby("CGPA_Group", observed=False)["Placement_Numeric"]
        .mean()
        .mul(100)
        .reset_index(name="Placement_Percentage")
    )

    # Display chart
    st.bar_chart(
        cgpa_placement.set_index("CGPA_Group")["Placement_Percentage"]
    )

    st.caption(
        "This chart shows the placement percentage across different CGPA ranges."
    )
