import streamlit as st
import pandas as pd


def render_internship_analysis(df: pd.DataFrame):
    """
    Analyzes and displays placement rates based on internship experience:
    - Detailed summary table
    - Placement percentage bar chart
    - Explanatory caption
    """
    # ==========================================
    # INTERNSHIP vs PLACEMENT ANALYSIS
    # ==========================================

    st.subheader("💼 Internship vs Placement Analysis")

    # Clean Internship values
    df["Internship_Clean"] = (
        df["Internship"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Clean placement values
    df["Placement_Clean"] = (
        df["Placement_Status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Convert placement status
    df["Placement_Numeric"] = df["Placement_Clean"].map({
        "placed": 1,
        "not placed": 0,
        "yes": 1,
        "no": 0
    })

    # Calculate internship-wise placement rate
    internship_analysis = (
        df.groupby("Internship_Clean")["Placement_Numeric"]
        .agg(["count", "sum", "mean"])
        .reset_index()
    )

    internship_analysis.columns = [
        "Internship",
        "Total_Students",
        "Placed",
        "Placement_Rate"
    ]

    internship_analysis["Not_Placed"] = (
        internship_analysis["Total_Students"]
        - internship_analysis["Placed"]
    )

    internship_analysis["Placement_Percentage"] = (
        internship_analysis["Placement_Rate"] * 100
    ).round(2)

    # Display table
    st.write("### 📋 Internship-wise Placement Details")

    st.dataframe(
        internship_analysis[
            [
                "Internship",
                "Total_Students",
                "Placed",
                "Not_Placed",
                "Placement_Percentage"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # Placement percentage chart
    st.write("### 📈 Placement Percentage by Internship")

    internship_chart = (
        internship_analysis
        .set_index("Internship")["Placement_Percentage"]
    )

    st.bar_chart(internship_chart)

    st.caption(
        "This analysis compares placement rates between students with and without internship experience."
    )
