
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Scientific Visualisation",
    page_icon="📊",
    layout="wide"
)

st.title("Scientific Visualisation of Malaysian Data")

st.write(
    "An interactive dashboard exploring maternal deaths, "
    "life expectancy, and household income in Malaysia."
)

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Home",
        "Maternal Death Analysis",
        "Life Expectancy Analysis",
        "Household Income Analysis"
    ]
)

# Home Page
if page == "Home":
    st.header("Project Overview")

    st.write(
        "This project analyses three Malaysian datasets "
        "using Python and data visualisation techniques."
    )

    st.info("Select an analysis from the sidebar to explore the data.")

# Maternal Death Page
elif page == "Maternal Death Analysis":
    st.header("Maternal Death Analysis")
    st.write("Analysis Period: 2000–2025")

    folder = Path("visualizations/maternal_death")

    charts = [
        "maternal_deaths_by_state.png",
        "maternal_deaths_lineplot.png",
        "maternal_death_rates_heatmap.png"
    ]

    for chart in charts:
        st.image(str(folder / chart), use_container_width=True)

# Life Expectancy Page
elif page == "Life Expectancy Analysis":
    st.header("Life Expectancy Analysis")
    st.write("Analysis Period: 2022–2026")

    folder = Path("visualizations/life_expectancy")

    charts = [
        "life_expectancy_gender_2026.png",
        "life_expectancy_ethnicity_2026.png",
        "life_expectancy_trends_2022_2026.png"
    ]

    for chart in charts:
        st.image(str(folder / chart), use_container_width=True)

# Household Income Page
elif page == "Household Income Analysis":
    st.header("Household Income Analysis")
    st.write("Analysis Years: 2019, 2022 and 2024")

    folder = Path("visualizations/household_income")

    charts = [
        "household_income_50th_percentile_2024.png",
        "household_income_heatmap.png",
        "household_income_percentiles_2024.png"
    ]

    for chart in charts:
        st.image(str(folder / chart), use_container_width=True)
