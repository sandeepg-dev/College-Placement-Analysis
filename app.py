import streamlit as st
import pandas as pd
import plotly.express as px

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

file_name = "placement_dataset_1500_students_realistic.csv"

try:
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.strip()
    if "Salary" in df.columns and "Salary" not in df.columns:
     df["Salary"] = df["Salary"]
except FileNotFoundError:
    st.error(
        f"Dataset file '{file_name}' was not found. "
        "Please keep the CSV file in the same folder as app.py."
    )
    st.stop()

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------

st.sidebar.header("🔎 Filters")

departments = ["All"] + sorted(df["Department"].unique().tolist())

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)

genders = ["All"] + sorted(df["Gender"].unique().tolist())

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    genders
)

filtered_df = df.copy()

if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]

# -------------------------------------------------
# KEY METRICS
# -------------------------------------------------

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

# -------------------------------------------------
# DASHBOARD METRICS
# -------------------------------------------------

st.header("📊 Placement Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "👨‍🎓 Total Students",
    total_students
)

col2.metric(
    "✅ Placed Students",
    placed_students
)

col3.metric(
    "📈 Placement %",
    f"{placement_percentage:.1f}%"
)

col4.metric(
    "💰 Average Salary",
    f"₹{average_salary:,.0f}"
)

col5.metric(
    "🏆 Highest Salary",
    f"₹{highest_salary:,.0f}"
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

# -------------------------------------------------
# FINAL INSIGHTS
# -------------------------------------------------

st.header("💡 Key Insights")

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