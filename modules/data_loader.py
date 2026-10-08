import streamlit as st
import pandas as pd


def load_data(file_name: str = "placement_dataset_1500_students_realistic.csv") -> pd.DataFrame:
    """
    Loads the placement dataset CSV file and strips whitespace from column names.
    If the file is not found, displays an error message in Streamlit and halts execution.
    """
    try:
        df = pd.read_csv(file_name)
        df.columns = df.columns.str.strip()
        if "Salary" in df.columns and "Salary" not in df.columns:
            df["Salary"] = df["Salary"]
        return df
    except FileNotFoundError:
        st.error(
            f"Dataset file '{file_name}' was not found. "
            "Please keep the CSV file in the same folder as app.py."
        )
        st.stop()
