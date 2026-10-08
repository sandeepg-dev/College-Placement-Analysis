# 🎓 College Placement Analytics Dashboard

A comprehensive, modular exploratory data analysis (EDA) dashboard built with **Streamlit**, **Pandas**, and **Plotly** to evaluate college placement trends, academic factors, skill distributions, and salary outcomes.

---

## 📁 Project Architecture & File Organization

The application is structured into clean, single-responsibility modules so that future changes, debugging, and enhancements can be made easily without affecting other parts of the application.

```text
College-Placement-Analysis/
│
├── app.py                                            # Main application orchestrator
├── placement_dataset_1500_students_realistic.csv      # Dataset (1,500 students)
├── requirements.txt                                  # Python dependencies
├── .gitignore                                        # Ignored files (venv, cache, etc.)
│
└── modules/                                          # Feature-specific modules
    ├── __init__.py                                   # Package initialization
    ├── data_loader.py                                # CSV dataset loading & validation
    ├── sidebar.py                                    # Sidebar filter widgets (Dept, Gender)
    ├── overview.py                                   # KPI metrics & dataset preview table
    ├── department_analysis.py                        # Department-wise breakdown & charts
    ├── internship_analysis.py                        # Internship vs placement analysis
    ├── project_analysis.py                           # Projects count vs placement analysis
    ├── skill_analysis.py                             # Technical, Communication & Aptitude scores
    ├── salary_analysis.py                            # Salary metrics, distribution & dept averages
    ├── cgpa_analysis.py                              # CGPA score ranges vs placement analysis
    ├── visualizations.py                             # Interactive Plotly charts & heatmaps
    └── insights.py                                   # Key summary insights & completion banner
```

---

## 🧩 Module Breakdown

| Module | Primary Responsibility | Key Functions |
|---|---|---|
| [`app.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/app.py) | Main dashboard entry point, page config, and module orchestration | Application flow |
| [`modules/data_loader.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/data_loader.py) | Safely loads CSV dataset, strips column whitespace, and handles missing files | `load_data()` |
| [`modules/sidebar.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/sidebar.py) | Provides Department and Gender filters in the Streamlit sidebar | `render_sidebar()` |
| [`modules/overview.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/overview.py) | Calculates key metrics (Total, Placed, Placement %, Avg & Max Salary) and renders preview | `calculate_key_metrics()`, `render_overview()` |
| [`modules/department_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/department_analysis.py) | Department placement table, bar chart, and highest/lowest rate highlights | `render_department_analysis()` |
| [`modules/internship_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/internship_analysis.py) | Evaluates placement outcomes based on internship experience | `render_internship_analysis()` |
| [`modules/project_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/project_analysis.py) | Evaluates placement outcomes across project counts | `render_project_analysis()` |
| [`modules/skill_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/skill_analysis.py) | Bins and analyzes Technical Skill, Communication Skill, and Aptitude scores | `render_skills_analysis()` |
| [`modules/salary_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/salary_analysis.py) | Computes salary summary, salary distribution, and department-wise average salaries | `render_salary_analysis()` |
| [`modules/cgpa_analysis.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/cgpa_analysis.py) | Bins CGPA scores and plots placement percentages | `render_cgpa_analysis()` |
| [`modules/visualizations.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/visualizations.py) | Generates interactive Plotly bar charts, box plots, histograms, and correlation heatmap | `render_interactive_visualizations()` |
| [`modules/insights.py`](file:///c:/Users/koush/Music/College-Placement-Analysis/modules/insights.py) | Displays final summary key insights and success notification | `render_insights()` |

---

## 🚀 How to Run the Dashboard

1. **Activate your environment** (or create one):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
