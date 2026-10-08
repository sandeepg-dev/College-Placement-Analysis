import streamlit as st
import pandas as pd


def render_technical_skill_analysis(df: pd.DataFrame):
    """
    Analyzes and displays technical skill score ranges vs placement rate.
    """
    # ============================================
    # TECHNICAL SKILL VS PLACEMENT ANALYSIS
    # ============================================

    st.subheader("💻 Technical Skill vs Placement Analysis")

    # Create technical skill ranges
    df["Technical_Skill_Range"] = pd.cut(
        df["Technical_Skill_Score"],
        bins=[0, 40, 60, 80, 100],
        labels=["Below 40", "40-60", "60-80", "80-100"],
        include_lowest=True
    )

    # Create summary
    technical_placement = (
        df.groupby("Technical_Skill_Range", observed=False)
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
    technical_placement["Placement_Percentage"] = (
        technical_placement["Placed"]
        / technical_placement["Total_Students"]
        * 100
    ).round(2)

    # Display table
    st.dataframe(
        technical_placement,
        use_container_width=True
    )

    # Chart
    st.subheader("📈 Placement Percentage by Technical Skill")

    st.bar_chart(
        technical_placement.set_index("Technical_Skill_Range")[
            "Placement_Percentage"
        ]
    )

    st.write(
        "This analysis shows how placement percentage varies "
        "across different technical skill score ranges."
    )


def render_communication_skill_analysis(df: pd.DataFrame):
    """
    Analyzes and displays communication skill score ranges vs placement rate.
    """
    # ============================================
    # COMMUNICATION SKILL VS PLACEMENT ANALYSIS
    # ============================================

    st.subheader("🗣️ Communication Skill vs Placement Analysis")

    # Create communication skill ranges
    df["Communication_Skill_Range"] = pd.cut(
        df["Communication_Skill_Score"],
        bins=[0, 40, 60, 80, 100],
        labels=["Below 40", "40-60", "60-80", "80-100"],
        include_lowest=True
    )

    # Create summary
    communication_placement = (
        df.groupby("Communication_Skill_Range", observed=False)
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
    communication_placement["Placement_Percentage"] = (
        communication_placement["Placed"]
        / communication_placement["Total_Students"]
        * 100
    ).round(2)

    # Display table
    st.dataframe(
        communication_placement,
        use_container_width=True
    )

    # Chart
    st.subheader("📈 Placement Percentage by Communication Skill")

    st.bar_chart(
        communication_placement.set_index("Communication_Skill_Range")[
            "Placement_Percentage"
        ]
    )

    st.write(
        "This analysis shows how placement percentage varies "
        "across different communication skill score ranges."
    )


def render_aptitude_skill_analysis(df: pd.DataFrame):
    """
    Analyzes and displays aptitude score ranges vs placement rate.
    """
    # ============================================
    # APTITUDE SCORE VS PLACEMENT ANALYSIS
    # ============================================

    st.subheader("🧠 Aptitude Score vs Placement Analysis")

    # Create aptitude score ranges
    df["Aptitude_Score_Range"] = pd.cut(
        df["Aptitude_Score"],
        bins=[0, 40, 60, 80, 100],
        labels=["Below 40", "40-60", "60-80", "80-100"],
        include_lowest=True
    )

    # Create summary
    aptitude_placement = (
        df.groupby("Aptitude_Score_Range", observed=False)
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
    aptitude_placement["Placement_Percentage"] = (
        aptitude_placement["Placed"]
        / aptitude_placement["Total_Students"]
        * 100
    ).round(2)

    # Display table
    st.dataframe(
        aptitude_placement,
        use_container_width=True
    )

    # Chart
    st.subheader("📈 Placement Percentage by Aptitude Score")

    st.bar_chart(
        aptitude_placement.set_index("Aptitude_Score_Range")[
            "Placement_Percentage"
        ]
    )

    st.write(
        "This analysis shows how placement percentage varies "
        "across different aptitude score ranges."
    )


def render_skills_analysis(df: pd.DataFrame):
    """
    Renders all skill analyses:
    - Technical Skill
    - Communication Skill
    - Aptitude Score
    """
    render_technical_skill_analysis(df)
    render_communication_skill_analysis(df)
    render_aptitude_skill_analysis(df)
