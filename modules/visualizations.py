import streamlit as st
import pandas as pd
import plotly.express as px


def render_department_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive bar chart for placement status by department.
    """
    # -------------------------------------------------
    # DEPARTMENT-WISE PLACEMENT
    # -------------------------------------------------
    st.header("🏢 Department-wise Placement")

    department_data = (
        filtered_df
        .groupby(["Department", "Placement_Status"])
        .size()
        .reset_index(name="Students")
    )

    fig_department = px.bar(
        department_data,
        x="Department",
        y="Students",
        color="Placement_Status",
        barmode="group",
        title="Placement Status by Department"
    )

    st.plotly_chart(
        fig_department,
        use_container_width=True
    )


def render_cgpa_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive box plot for CGPA distribution by placement status.
    """
    # -------------------------------------------------
    # CGPA VS PLACEMENT
    # -------------------------------------------------
    st.header("📚 CGPA vs Placement")

    fig_cgpa = px.box(
        filtered_df,
        x="Placement_Status",
        y="CGPA",
        color="Placement_Status",
        title="CGPA Distribution by Placement Status"
    )

    st.plotly_chart(
        fig_cgpa,
        use_container_width=True
    )


def render_internship_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive bar chart for internship experience vs placement.
    """
    # -------------------------------------------------
    # INTERNSHIP VS PLACEMENT
    # -------------------------------------------------
    st.header("💼 Internship vs Placement")

    internship_data = (
        filtered_df
        .groupby(["Internship", "Placement_Status"])
        .size()
        .reset_index(name="Students")
    )

    fig_internship = px.bar(
        internship_data,
        x="Internship",
        y="Students",
        color="Placement_Status",
        barmode="group",
        title="Internship Experience vs Placement"
    )

    st.plotly_chart(
        fig_internship,
        use_container_width=True
    )


def render_projects_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive bar chart for number of projects vs placement.
    """
    # -------------------------------------------------
    # PROJECTS VS PLACEMENT
    # -------------------------------------------------
    st.header("🛠️ Projects vs Placement")

    project_data = (
        filtered_df
        .groupby(["Projects_Count", "Placement_Status"])
        .size()
        .reset_index(name="Students")
    )

    fig_projects = px.bar(
        project_data,
        x="Projects_Count",
        y="Students",
        color="Placement_Status",
        barmode="group",
        title="Number of Projects vs Placement"
    )

    st.plotly_chart(
        fig_projects,
        use_container_width=True
    )


def render_salary_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive histogram for salary distribution of placed students.
    """
    # -------------------------------------------------
    # SALARY DISTRIBUTION
    # -------------------------------------------------
    st.header("💰 Salary Distribution")

    salary_data = filtered_df[
        (filtered_df["Placement_Status"] == "Placed")
        & (filtered_df["Salary_INR"] > 0)
    ]

    if len(salary_data) > 0:

        fig_salary = px.histogram(
            salary_data,
            x="Salary_INR",
            nbins=20,
            title="Salary Distribution of Placed Students"
        )

        st.plotly_chart(
            fig_salary,
            use_container_width=True
        )

    else:
        st.info("No salary data available for the selected filters.")


def render_skills_chart(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive box plot for skills distribution by placement status.
    """
    # -------------------------------------------------
    # SKILLS ANALYSIS
    # -------------------------------------------------
    st.header("🧠 Skills Analysis")

    skill_columns = [
        "Aptitude_Score",
        "Technical_Skill_Score",
        "Communication_Skill_Score"
    ]

    available_skills = [
        column for column in skill_columns
        if column in filtered_df.columns
    ]

    if available_skills:

        skill_data = filtered_df[
            ["Placement_Status"] + available_skills
        ].melt(
            id_vars="Placement_Status",
            var_name="Skill",
            value_name="Score"
        )

        fig_skills = px.box(
            skill_data,
            x="Skill",
            y="Score",
            color="Placement_Status",
            title="Skills Distribution by Placement Status"
        )

        st.plotly_chart(
            fig_skills,
            use_container_width=True
        )


def render_correlation_heatmap(filtered_df: pd.DataFrame):
    """
    Renders Plotly interactive correlation heatmap for numeric features.
    """
    # -------------------------------------------------
    # CORRELATION HEATMAP
    # -------------------------------------------------
    st.header("🔥 Correlation Analysis")

    numeric_df = filtered_df.select_dtypes(
        include="number"
    )

    if len(numeric_df.columns) >= 2:

        correlation = numeric_df.corr()

        fig_corr = px.imshow(
            correlation,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap"
        )

        st.plotly_chart(
            fig_corr,
            use_container_width=True
        )


def render_interactive_visualizations(filtered_df: pd.DataFrame):
    """
    Renders all interactive Plotly visualization charts in sequence.
    """
    render_department_chart(filtered_df)
    render_cgpa_chart(filtered_df)
    render_internship_chart(filtered_df)
    render_projects_chart(filtered_df)
    render_salary_chart(filtered_df)
    render_skills_chart(filtered_df)
    render_correlation_heatmap(filtered_df)
