import streamlit as st

from modules.data_loader import load_data
from modules.sidebar import render_sidebar
from modules.overview import render_overview
from modules.department_analysis import render_department_analysis
from modules.internship_analysis import render_internship_analysis
from modules.project_analysis import render_project_analysis
from modules.skill_analysis import render_skills_analysis
from modules.salary_analysis import render_salary_analysis
from modules.cgpa_analysis import render_cgpa_analysis
from modules.visualizations import render_interactive_visualizations
from modules.insights import render_insights

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------
st.set_page_config(
    page_title="College Placement Analytics",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("🎓 College Placement Data Analysis")
st.write("Welcome to the College Placement Analytics Dashboard")

# -------------------------------------------------
# LOAD DATASET
# -------------------------------------------------
df = load_data()

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------
filtered_df, selected_department, selected_gender = render_sidebar(df)

# -------------------------------------------------
# KEY METRICS & DATASET PREVIEW
# -------------------------------------------------
metrics = render_overview(filtered_df)

# -------------------------------------------------
# STATISTICAL & CATEGORICAL ANALYSES
# -------------------------------------------------
render_department_analysis(df)
render_internship_analysis(df)
render_project_analysis(df)
render_skills_analysis(df)
render_salary_analysis(df)
render_cgpa_analysis(df)

# -------------------------------------------------
# INTERACTIVE PLOTLY VISUALIZATIONS
# -------------------------------------------------
render_interactive_visualizations(filtered_df)

# -------------------------------------------------
# FINAL INSIGHTS
# -------------------------------------------------
render_insights(metrics)