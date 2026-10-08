import streamlit as st


def render_insights(metrics: dict):
    """
    Displays key insights summary bullet points and success status banner.
    """
    # -------------------------------------------------
    # FINAL INSIGHTS
    # -------------------------------------------------
    st.header("💡 Key Insights")

    total_students = metrics["total_students"]
    placed_students = metrics["placed_students"]
    placement_percentage = metrics["placement_percentage"]
    average_salary = metrics["average_salary"]
    highest_salary = metrics["highest_salary"]

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

    # -------------------------------------------------
    # CONCLUSION & KEY PLACEMENT INSIGHTS
    # -------------------------------------------------
    with st.expander("📝 Conclusion & Key Placement Insights", expanded=False):
        st.subheader("🎯 Conclusion")
        st.write(
            "The College Placement Data Analysis project provides a comprehensive and interactive "
            "platform for analyzing student placement data and identifying meaningful patterns and "
            "trends. By applying data cleaning, exploratory data analysis, statistical techniques, "
            "and visualizations, the system transforms raw placement data into clear and useful insights."
        )
        st.write(
            "The website enables users to understand important placement factors such as placement "
            "rates, salary trends, department-wise performance, academic performance, and student "
            "placement outcomes through an easy-to-use dashboard."
        )
        st.write(
            "Overall, this project demonstrates how data analysis and visualization can support "
            "data-driven decision-making in an educational environment. The insights generated from "
            "the analysis can help students understand placement trends, assist institutions in "
            "evaluating placement performance, and support future improvements in training and recruitment strategies."
        )
        st.write(
            "This project successfully combines data processing, analysis, visualization, and "
            "web-based presentation into a single platform, making complex placement information "
            "easier to understand and interpret."
        )

        st.subheader("🔍 Key Comparative Insights")
        st.markdown(
            "- **Technical Skills:** Students with stronger technical skills recorded a higher "
            "placement rate compared with students who reported lower technical proficiency.\n"
            "- **Communication Skills:** Students with good communication skills showed better "
            "placement outcomes than students with comparatively weaker communication skills.\n"
            "- **Projects:** Students who completed relevant academic or technical projects "
            "demonstrated stronger placement outcomes compared with students without project experience.\n"
            "- **Internship Experience:** Students with internship experience achieved a higher "
            "placement rate than students who had not completed an internship, indicating the value of practical industry exposure.\n"
            "- **Academic Performance:** Students with stronger academic performance generally "
            "showed better placement outcomes compared with students with lower academic performance.\n"
            "- **Multiple Skills & Experience:** Students who combined technical skills, communication "
            "skills, project experience, internship exposure, and good academic performance showed the strongest overall placement outcomes."
        )

        st.subheader("📊 Overall Finding")
        st.write(
            "The analysis indicates that placement success is associated with a combination of academic "
            "knowledge, technical capability, communication ability, practical project experience, and "
            "industry exposure rather than a single factor."
        )
        st.write(
            "For example, if X out of Y students with internship experience were placed, compared with "
            "A out of B students without internship experience, the placement rate can be directly "
            "compared to identify the difference. Similar comparisons can be made for projects, "
            "technical skills, communication skills, and academic performance."
        )

        st.subheader("💡 Final Insight")
        st.write(
            "The findings suggest that students can strengthen their placement readiness by developing "
            "technical skills, communication skills, practical projects, internship experience, and "
            "academic performance together. Institutions can also use these insights to design targeted "
            "training programs and improve placement preparation strategies."
        )
        st.write(
            "Overall, the College Placement Analysis transforms raw student and placement data into "
            "actionable insights, helping students and institutions understand the factors associated with successful placement outcomes."
        )

        st.subheader("🏁 Final Outcome")
        st.write(
            "The developed website serves as a professional and user-friendly College Placement "
            "Analytics Dashboard, providing meaningful insights from placement data and demonstrating "
            "the practical application of Exploratory Data Analysis (EDA) in real-world educational analytics."
        )
