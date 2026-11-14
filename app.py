import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualisation",
    page_icon="📊",
    layout="wide"
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



if page == "Home":

    # HOME PAGE STYLING
    st.markdown("""
    <style>
    .home-hero {
        background: linear-gradient(120deg, #172554, #1e293b);
        padding: 32px;
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 25px;
    }

    .home-hero h1 {
        color: #ffffff;
        font-size: 34px;
        margin-bottom: 12px;
    }

    .home-hero p {
        color: #cbd5e1;
        font-size: 16px;
        margin-bottom: 0;
    }

    .home-kpi {
        background: #1e293b;
        padding: 24px;
        border-radius: 14px;
        border: 1px solid #334155;
        text-align: center;
        min-height: 140px;
    }

    .home-kpi-value {
        color: #ffffff;
        font-size: 32px;
        font-weight: 700;
    }

    .home-kpi-label {
        color: #94a3b8;
        font-size: 14px;
    }

    .home-dataset {
        background: #1e293b;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #334155;
        min-height: 215px;
    }

    .home-dataset h3 {
        color: #ffffff;
        font-size: 21px;
        margin-bottom: 10px;
    }

    .home-dataset p {
        color: #cbd5e1;
        font-size: 14px;
    }

    .home-tag {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        margin-bottom: 12px;
    }

    .home-about {
        background: #1e293b;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #334155;
        color: #cbd5e1;
    }

    .home-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        padding: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION
    st.markdown("""
    <div class="home-hero">
        <h1>📊 Malaysia Socioeconomic & Health Insights Dashboard</h1>
        <p>
            Interactive Data Analytics Dashboard | Malaysia
        </p>
        <p style="margin-top: 12px;">
            Explore maternal health, life expectancy, and
            household income through interactive visualisations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # DASHBOARD OVERVIEW
    st.subheader("📌 Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="home-kpi">
            <div class="home-kpi-value">3</div>
            <div class="home-kpi-label">📁 Datasets</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="home-kpi">
            <div class="home-kpi-value">9</div>
            <div class="home-kpi-label">📊 Visualisations</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="home-kpi">
            <div class="home-kpi-value">Malaysia</div>
            <div class="home-kpi-label">📍 Data Coverage</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # DATASET CARDS
    st.subheader("🔎 Explore the Datasets")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="home-dataset"
             style="border-top: 4px solid #f87171;">
            <h3>🩺 Maternal Death</h3>
            <span class="home-tag"
                  style="background:#450a0a;color:#fca5a5;">
                2000–2025
            </span>
            <p>
                Explore maternal death trends, mortality
                rates, and differences across Malaysian states.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="home-dataset"
             style="border-top: 4px solid #60a5fa;">
            <h3>👥 Life Expectancy</h3>
            <span class="home-tag"
                  style="background:#172554;color:#93c5fd;">
                2022–2026
            </span>
            <p>
                Compare life expectancy across states,
                genders, and ethnic groups in Malaysia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="home-dataset"
             style="border-top: 4px solid #34d399;">
            <h3>💰 Household Income</h3>
            <span class="home-tag"
                  style="background:#064e3b;color:#a7f3d0;">
                2019, 2022 & 2024
            </span>
            <p>
                Analyse household income trends,
                state differences, and income percentiles.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # ABOUT PROJECT
    st.subheader("ℹ️ About This Project")

    st.markdown("""
    <div class="home-about">
        This dashboard was developed using
        <b>Python, Streamlit, and Plotly</b> to visualise
        three Malaysian datasets sourced from the
        <b>Department of Statistics Malaysia (DOSM)</b>.
        It supports interactive exploration of
        socioeconomic and demographic patterns.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.info(
        "👈 Select an analysis from the sidebar "
        "to explore the interactive visualisations."
    )

    # FOOTER
    st.markdown("""
    <div class="home-footer">
        Data Source: DOSM |
        Built with Python, Streamlit & Plotly
    </div>
    """, unsafe_allow_html=True)




# Maternal Death Page
elif page == "Maternal Death Analysis":
    st.header("Maternal Death Analysis")
    st.write("Analysis Period: 2000–2025")

    # Objective Statement
    st.info(
        "Objective: To analyse the distribution and trends "
        "of maternal mortality across Malaysian states."
    )

    # Load dataset
    data_path = (
        Path(__file__).resolve().parent
        / "datasets"
        / "death_maternal_state.csv"
    )

    if not data_path.exists():
        st.error("Dataset not found: datasets/death_maternal_state.csv")
        st.stop()

    @st.cache_data
    def load_maternal_data(path):
        data = pd.read_csv(path)
        data["year"] = pd.to_datetime(
            data["date"], errors="coerce"
        ).dt.year

        return data.dropna(
            subset=["state", "year"]
        )

    df = load_maternal_data(data_path)

    # Filters
    st.subheader("Data Filters")

    states = sorted(df["state"].unique().tolist())

    selected_states = st.multiselect(
        "Select State(s)",
        states,
        default=states
    )

    years = sorted(
        df["year"].astype(int).unique().tolist()
    )

    selected_years = st.slider(
        "Select Year Range",
        min(years),
        max(years),
        (min(years), max(years))
    )

    measure = st.selectbox(
        "Measurement",
        ["abs", "rate"],
        format_func=lambda v:
            "Number of Maternal Deaths"
            if v == "abs"
            else "Maternal Death Rate"
    )

    # Filter dataset
    filtered = df[
        df["state"].isin(selected_states)
        & df["year"].between(*selected_years)
    ].copy()

    if filtered.empty:
        st.warning(
            "No data for this selection. "
            "Choose another state or year range."
        )

    else:
        label = (
            "Number of Maternal Deaths"
            if measure == "abs"
            else "Maternal Death Rate"
        )

        # Visualization 1: Interactive Line Chart
        st.subheader("Maternal Death Trends by State")

        chart_data = (
            filtered.groupby(
                ["state", "year"], as_index=False
            )[measure].mean()
            .sort_values("year")
        )

        fig = px.line(
            chart_data,
            x="year",
            y=measure,
            color="state",
            markers=True,
            labels={
                "year": "Year",
                measure: label,
                "state": "State"
            },
            title="Maternal Mortality Trends Across Malaysian States"
        )

        fig.update_layout(
            hovermode="x unified",
            legend_title_text="State"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Summary Box
        st.subheader("Summary Box")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "States Selected",
                filtered["state"].nunique()
            )

        with col2:
            st.metric(
                "Years Covered",
                filtered["year"].nunique()
            )

        with col3:
            st.metric(
                "Highest Observed Value",
                f"{chart_data[measure].max():,.2f}"
            )

        # Interpretation
        st.subheader("Interpretation")

        st.write(
            "The line chart illustrates changes in maternal "
            "mortality across selected Malaysian states over "
            "the chosen period. It allows comparisons of "
            "mortality patterns between states and highlights "
            "fluctuations over time. Differences between "
            "the lines indicate variations in the selected "
            "maternal mortality measurement across states."
        )

        st.caption(
            "Source: Department of Statistics Malaysia (DOSM)"
        )



# Life Expectancy Page
elif page == "Life Expectancy Analysis":
    st.header("Life Expectancy Analysis")

    # Objective Statement
    st.info(
        "Objective: To examine variations in life expectancy "
        "across Malaysian states based on gender, ethnicity, and time."
    )

    # Dataset path
    data_path = (
        Path(__file__).resolve().parent
        / "datasets"
        / "life_expectancy_state_ethnic.csv"
    )

    if not data_path.exists():
        st.error(
            "Dataset not found: "
            "datasets/life_expectancy_state_ethnic.csv"
        )
        st.stop()

    # Load and prepare data
    @st.cache_data
    def load_life_data(path):
        data = pd.read_csv(path)

        data["year"] = pd.to_datetime(
            data["date"], errors="coerce"
        ).dt.year

        data["life_expectancy"] = pd.to_numeric(
            data["life_expectancy"], errors="coerce"
        )

        return data.dropna(
            subset=[
                "state",
                "year",
                "sex",
                "ethnicity",
                "life_expectancy"
            ]
        )

    df_life = load_life_data(data_path)

    # Data Filters
    st.subheader("Data Filters")

    states = sorted(df_life["state"].unique().tolist())

    default_states = [
        s for s in ["Johor", "Selangor"]
        if s in states
    ]

    selected_states = st.multiselect(
        "Select State(s)",
        states,
        default=default_states
    )

    genders = ["both", "male", "female"]
    selected_gender = st.selectbox(
        "Select Gender",
        genders,
        format_func=lambda x: {
            "both": "Both Sexes",
            "male": "Male",
            "female": "Female"
        }[x]
    )

    ethnic_labels = {
        "overall": "Overall",
        "bumi_malay": "Bumiputera Malay",
        "bumi_other": "Other Bumiputera",
        "chinese": "Chinese",
        "indian": "Indian"
    }

    available_ethnicities = [
        e for e in ethnic_labels
        if e in df_life["ethnicity"].unique()
    ]

    selected_ethnicity = st.selectbox(
        "Select Ethnicity",
        available_ethnicities,
        format_func=lambda x: ethnic_labels[x]
    )

    years = sorted(
        df_life["year"].astype(int).unique().tolist()
    )

    selected_years = st.slider(
        "Select Year Range",
        min(years),
        max(years),
        (min(years), max(years))
    )

    # Filter dataset
    filtered = df_life[
        df_life["state"].isin(selected_states)
        & (df_life["sex"] == selected_gender)
        & (df_life["ethnicity"] == selected_ethnicity)
        & df_life["year"].between(*selected_years)
    ].copy()

    if filtered.empty:
        st.warning(
            "No data available for the selected filters. "
            "Please choose another state, gender, "
            "ethnicity, or year range."
        )

    else:
        # Prepare data for visualization
        chart_data = (
            filtered.groupby(
                ["state", "year"], as_index=False
            )["life_expectancy"].mean()
            .sort_values("year")
        )

        # One Interactive Line Chart
        st.subheader(
            "Life Expectancy Trends Across Malaysian States"
        )

        fig = px.line(
            chart_data,
            x="year",
            y="life_expectancy",
            color="state",
            markers=True,
            title=(
                "Life Expectancy Trends by State "
                f"({selected_years[0]}–{selected_years[1]})"
            ),
            labels={
                "year": "Year",
                "life_expectancy": "Life Expectancy (Years)",
                "state": "State"
            }
        )

        fig.update_xaxes(dtick=1)

        fig.update_layout(
            template="plotly_dark",
            hovermode="x unified",
            legend_title_text="State"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Summary Box
        st.subheader("Summary Box")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "States Selected",
                chart_data["state"].nunique()
            )

        with col2:
            st.metric(
                "Years Covered",
                chart_data["year"].nunique()
            )

        with col3:
            st.metric(
                "Highest Life Expectancy",
                f"{chart_data['life_expectancy'].max():.1f} years"
            )

        # Interpretation
        st.subheader("Interpretation")

        st.write(
            "The interactive line chart illustrates changes "
            "in life expectancy across selected Malaysian "
            "states over time. Users can explore differences "
            "based on gender and ethnicity through the "
            "available filters. The visualisation highlights "
            "variations between states and shows how life "
            "expectancy changes throughout the selected period."
        )

        st.caption(
            "Source: Department of Statistics Malaysia (DOSM)"
        )


    

# Household Income Analysis Page
elif page == "Household Income Analysis":
    st.header("Household Income Analysis")

    # Objective Statement
    st.info(
        "Objective: To analyse household income distribution, "
        "trends, and differences across Malaysian states "
        "and income percentiles."
    )

    # Dataset path
    data_path = (
        Path(__file__).resolve().parent
        / "datasets"
        / "hies_state_percentile.csv"
    )

    if not data_path.exists():
        st.error("Household income dataset not found.")
        st.stop()

    # Load and prepare dataset
    @st.cache_data
    def load_income_data(path):
        data = pd.read_csv(path)

        data["year"] = pd.to_datetime(
            data["date"], errors="coerce"
        ).dt.year

        data["percentile"] = pd.to_numeric(
            data["percentile"], errors="coerce"
        )

        data["income"] = pd.to_numeric(
            data["income"], errors="coerce"
        )

        return data.dropna(
            subset=[
                "year",
                "state",
                "percentile",
                "variable",
                "income"
            ]
        )

    df_income = load_income_data(data_path)

    # Data Filters
    st.subheader("Data Filters")

    states = sorted(
        df_income["state"].unique().tolist()
    )

    selected_states = st.multiselect(
        "Select State(s)",
        states,
        default=[
            s for s in ["Johor", "Selangor", "Melaka"]
            if s in states
        ]
    )

    years = sorted(
        df_income["year"].astype(int).unique().tolist()
    )

    selected_years = st.select_slider(
        "Select Year Range",
        options=years,
        value=(years[0], years[-1])
    )

    percentiles = sorted(
        df_income["percentile"].unique().tolist()
    )

    selected_percentile = st.selectbox(
        "Select Income Percentile",
        percentiles,
        index=(
            percentiles.index(50)
            if 50 in percentiles else 0
        ),
        format_func=lambda p: f"P{int(p)}"
    )

    measures = sorted(
        df_income["variable"].unique().tolist()
    )

    selected_measure = st.selectbox(
        "Select Income Measurement",
        measures,
        index=(
            measures.index("median")
            if "median" in measures else 0
        )
    )

    # Filter dataset
    filtered = df_income[
        df_income["state"].isin(selected_states)
        & df_income["year"].between(*selected_years)
        & (df_income["percentile"] == selected_percentile)
        & (df_income["variable"] == selected_measure)
    ].copy()

    if filtered.empty:
        st.warning(
            "No data available for the selected filters. "
            "Please choose another state, year, "
            "percentile or measurement."
        )

    else:
        # Prepare data for visualization
        chart_data = (
            filtered.groupby(
                ["state", "year"], as_index=False
            )["income"].mean()
            .sort_values("year")
        )

        # One Interactive Line Chart
        st.subheader(
            "Household Income Trends Across Malaysian States"
        )

        fig = px.line(
            chart_data,
            x="year",
            y="income",
            color="state",
            markers=True,
            title=(
                "Household Income Trends by State "
                f"(P{int(selected_percentile)})"
            ),
            labels={
                "year": "Year",
                "income": "Household Income (RM)",
                "state": "State"
            }
        )

        fig.update_xaxes(
            tickmode="array",
            tickvals=years
        )

        fig.update_layout(
            template="plotly_dark",
            hovermode="x unified",
            legend_title_text="State"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Summary Box
        st.subheader("Summary Box")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "States Selected",
                chart_data["state"].nunique()
            )

        with col2:
            st.metric(
                "Years Covered",
                chart_data["year"].nunique()
            )

        with col3:
            st.metric(
                "Highest Household Income",
                f"RM {chart_data['income'].max():,.2f}"
            )

        # Interpretation
        st.subheader("Interpretation")

        st.write(
            "The interactive line chart illustrates "
            "household income trends across selected "
            "Malaysian states over time. Users can explore "
            "income differences by selecting different "
            "income percentiles and measurements. "
            "The visualisation highlights variations "
            "between states and changes in household "
            "income throughout the selected period."
        )

        st.caption(
            "Source: Department of Statistics Malaysia (DOSM)"
        )



    
   
