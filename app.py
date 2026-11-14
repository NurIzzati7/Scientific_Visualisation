import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

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

    data_path = Path(__file__).resolve().parent / "datasets" / "death_maternal_state.csv"
    if not data_path.exists():
        st.error("Dataset not found: datasets/death_maternal_state.csv")
        st.stop()

    @st.cache_data
    def load_maternal_data(path):
        data = pd.read_csv(path)
        data["year"] = pd.to_datetime(data["date"], errors="coerce").dt.year
        return data.dropna(subset=["state", "year"])

    df = load_maternal_data(data_path)
    states = sorted(df["state"].unique().tolist())
    selected_states = st.multiselect("Select State(s)", states, default=states)
    years = sorted(df["year"].astype(int).unique().tolist())
    selected_years = st.slider("Select Year Range", min(years), max(years), (min(years), max(years)))
    measure = st.selectbox("Measurement", ["abs", "rate"],
                           format_func=lambda v: "Number of Maternal Deaths" if v == "abs" else "Maternal Death Rate")
    filtered = df[df["state"].isin(selected_states) & df["year"].between(*selected_years)].copy()
    if filtered.empty:
        st.warning("No data for this selection. Choose another state or year range.")
    else:
        label = "Number of Maternal Deaths" if measure == "abs" else "Maternal Death Rate"
        st.subheader("Maternal Death Trends")
        fig = px.line(filtered.sort_values("year"), x="year", y=measure, color="state",
                      markers=True, labels={"year": "Year", measure: label, "state": "State"})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Maternal Deaths by State")
        if measure == "abs":
            totals = filtered.groupby("state", as_index=False)["abs"].sum().sort_values("abs")
            bar = px.bar(totals, x="abs", y="state", orientation="h",
                         labels={"abs": "Total Maternal Deaths", "state": "State"})
            st.plotly_chart(bar, use_container_width=True)
        else:
            st.caption("Rates should not be summed across years; the chart below shows yearly rates.")
            heat = filtered.pivot_table(index="state", columns="year", values="rate", aggfunc="mean")
            fig_heat = px.imshow(heat, aspect="auto", labels={"x": "Year", "y": "State", "color": "Rate"})
            st.plotly_chart(fig_heat, use_container_width=True)

# Life Expectancy Page
elif page == "Life Expectancy Analysis":
    st.header("Life Expectancy Analysis")

    data_path = Path(__file__).resolve().parent / "datasets" / "life_expectancy_state_ethnic.csv"
    if not data_path.exists():
        st.error("Dataset not found: datasets/life_expectancy_state_ethnic.csv")
        st.stop()

    # Load life expectancy dataset
    df_life = pd.read_csv(data_path)

    # Display dataset preview
    st.subheader("Life Expectancy Dataset Preview")
    st.dataframe(df_life.head())

    
    # Prepare life expectancy data
    df_life["year"] = pd.to_datetime(df_life["date"]).dt.year

    # Filter overall ethnicity to avoid duplicate comparisons
    df_gender = df_life[
        (df_life["ethnicity"] == "overall") &
        (df_life["sex"].isin(["male", "female"]))
    ].copy()

    # Select analysis year
    st.subheader("Life Expectancy by State and Gender")

    selected_year = st.selectbox(
        "Select Year",
        sorted(df_gender["year"].unique(), reverse=True)
    )

    filtered_gender = df_gender[
        df_gender["year"] == selected_year
    ]

    # Create interactive grouped bar chart
    fig_gender = px.bar(
        filtered_gender,
        x="state",
        y="life_expectancy",
        color="sex",
        barmode="group",
        title=f"Life Expectancy by State and Gender ({selected_year})",
        labels={
            "state": "State",
            "life_expectancy": "Life Expectancy (Years)",
            "sex": "Gender"
        },
        color_discrete_map={
            "male": "#80B3A2",
            "female": "#E6A080"
        }
    )

    fig_gender.update_layout(
        xaxis_tickangle=-45,
        template="plotly_dark"
    )

    st.plotly_chart(fig_gender, use_container_width=True)

