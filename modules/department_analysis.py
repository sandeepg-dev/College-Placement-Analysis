import streamlit as st
import pandas as pd


def render_department_analysis(df: pd.DataFrame):
    """
    Performs and displays department-wise placement analysis:
    - Detailed breakdown table
    - Placement percentage bar chart
    - Summary metrics (Highest and Lowest placement rates)
    """
    # ==========================================
    # DEPARTMENT-WISE PLACEMENT ANALYSIS
    # ==========================================

    st.subheader("📊 Department-wise Placement Analysis")

    # Create a clean placement status column
    df["Placement_Clean"] = (
        df["Placement_Status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Convert placement status into Placed / Not Placed
    df["Placement_Result"] = df["Placement_Clean"].map({
        "placed": "Placed",
        "yes": "Placed",
        "not placed": "Not Placed",
        "no": "Not Placed"
    })

    # Department-wise total students
    dept_analysis = (
        df.groupby("Department")
        .agg(
            Total_Students=("Student_ID", "count"),
            Placed=("Placement_Result", lambda x: (x == "Placed").sum()),
            Not_Placed=("Placement_Result", lambda x: (x == "Not Placed").sum())
        )
        .reset_index()
    )

    # Calculate placement percentage
    dept_analysis["Placement_Percentage"] = (
        dept_analysis["Placed"] /
        dept_analysis["Total_Students"] * 100
    ).round(2)

    # Display the complete table
    st.write("### 📋 Department-wise Placement Details")

    st.dataframe(
        dept_analysis,
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------
    # Placement Percentage Chart
    # ------------------------------------------

    st.write("### 📈 Department-wise Placement Percentage")

    placement_chart = (
        dept_analysis
        .set_index("Department")["Placement_Percentage"]
    )

    st.bar_chart(placement_chart)

    # ------------------------------------------
    # Summary
    # ------------------------------------------

    st.write("### 📌 Placement Summary")

    highest_dept = dept_analysis.loc[
        dept_analysis["Placement_Percentage"].idxmax()
    ]

    lowest_dept = dept_analysis.loc[
        dept_analysis["Placement_Percentage"].idxmin()
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Placement Rate",
            f"{highest_dept['Placement_Percentage']:.2f}%",
            highest_dept["Department"]
        )

    with col2:
        st.metric(
            "Lowest Placement Rate",
            f"{lowest_dept['Placement_Percentage']:.2f}%",
            lowest_dept["Department"]
        )

    st.bar_chart(placement_chart)
