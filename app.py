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

    data_path = (
        Path(__file__).resolve().parent
        / "datasets"
        / "hies_state_percentile.csv"
    )

    if not data_path.exists():
        st.error("Household income dataset not found.")
        st.stop()

    df_income = pd.read_csv(data_path)

    st.subheader("Household Income Dataset Preview")
    st.dataframe(df_income.head())


    # Interactive Household Income by State
    st.subheader("Household Income by State")

    df_income["year"] = pd.to_datetime(
        df_income["date"]
    ).dt.year

    # Select year
    income_year = st.selectbox(
        "Select Year for Income Analysis",
        sorted(df_income["year"].dropna().unique(), reverse=True)
    )

    # Select percentile
    income_percentile = st.selectbox(
        "Select Income Percentile",
        sorted(df_income["percentile"].dropna().unique()),
        index=0
    )

    # Select measurement
    income_measure = st.selectbox(
        "Select Income Measurement",
        ["mean", "median"]
    )

    # Filter data
    filtered_income = df_income[
        (df_income["year"] == income_year) &
        (df_income["percentile"] == income_percentile) &
        (df_income["variable"] == income_measure)
    ].copy()

    filtered_income["income"] = pd.to_numeric(
        filtered_income["income"], errors="coerce"
    )
    filtered_income = filtered_income.dropna(subset=["income"])

    if not filtered_income.empty:
        filtered_income = filtered_income.sort_values("income")

        fig_income = px.bar(
            filtered_income,
            x="income",
            y="state",
            orientation="h",
            title=f"Household Income by State ({income_year})",
            labels={
                "income": "Household Income (RM)",
                "state": "State"
            },
            color="income",
            color_continuous_scale="Blues"
        )

        fig_income.update_layout(
            template="plotly_dark",
            height=650
        )

        st.plotly_chart(
            fig_income,
            use_container_width=True
        )
    else:
        st.warning("No data available for selected filters.")

    
    # Household Income Trends
    st.subheader("Household Income Trends Across States")

    # Prepare year column
    df_income["year"] = pd.to_datetime(
        df_income["date"]
    ).dt.year

    # Select states
    trend_states = st.multiselect(
        "Select States for Income Trend",
        sorted(df_income["state"].dropna().unique()),
        default=["Johor", "Selangor"]
    )

    # Select percentile
    trend_percentile = st.selectbox(
        "Select Percentile for Income Trend",
        sorted(df_income["percentile"].dropna().unique()),
        index=0
    )

    # Select measurement
    trend_measure = st.selectbox(
        "Select Measurement for Income Trend",
        ["mean", "median"]
    )

    # Filter selected data
    income_trend = df_income[
        (df_income["state"].isin(trend_states)) &
        (df_income["percentile"] == trend_percentile) &
        (df_income["variable"] == trend_measure)
    ].copy()

    income_trend["income"] = pd.to_numeric(
        income_trend["income"], errors="coerce"
    )

    income_trend = income_trend.dropna(subset=["income"])

    # Plot interactive line chart
    if not income_trend.empty:
        fig_income_trend = px.line(
            income_trend.sort_values("year"),
            x="year",
            y="income",
            color="state",
            markers=True,
            title="Household Income Trends by State",
            labels={
                "year": "Year",
                "income": "Household Income (RM)",
                "state": "State"
            }
        )

        fig_income_trend.update_xaxes(
            tickmode="array",
            tickvals=sorted(income_trend["year"].unique())
        )

        fig_income_trend.update_layout(
            template="plotly_dark",
            hovermode="x unified"
        )

        st.plotly_chart(
            fig_income_trend,
            use_container_width=True
        )
    else:
        st.warning("No income trend data available.")


    # Household Income Distribution by Percentile
    st.subheader("Household Income Distribution by Percentile")

    # Prepare independent dataset
    df_percentile = df_income.copy()

    df_percentile["year"] = pd.to_datetime(
        df_percentile["date"], errors="coerce"
    ).dt.year

    df_percentile["percentile"] = pd.to_numeric(
        df_percentile["percentile"], errors="coerce"
    )

    df_percentile["income"] = pd.to_numeric(
        df_percentile["income"], errors="coerce"
    )

    df_percentile = df_percentile.dropna(
        subset=["year", "state", "percentile", "income"]
    )

    # Select year
    available_years = sorted(
        df_percentile["year"].unique().astype(int).tolist(),
        reverse=True
    )

    if not available_years:
        st.warning("No valid income data available.")
        st.stop()

    dist_year = st.selectbox(
        "Select Year for Percentile Analysis",
        available_years,
        key="dist_year_v3"
    )

    # Select states
    available_states = sorted(
        df_percentile["state"].dropna().unique().tolist()
    )

    default_states = [
        state for state in
        ["Johor", "Selangor", "Melaka"]
        if state in available_states
    ]

    dist_states = st.multiselect(
        "Select States for Percentile Comparison",
        available_states,
        default=default_states,
        key="dist_states_v3"
    )

    # Select measurement
    available_measures = sorted(
        df_percentile["variable"].dropna().unique().tolist()
    )

    default_measure = (
        available_measures.index("median")
        if "median" in available_measures else 0
    )

    dist_measure = st.selectbox(
        "Select Measurement for Percentile Analysis",
        available_measures,
        index=default_measure,
        key="dist_measure_v3"
    )

    # Select percentile display
    percentile_mode = st.selectbox(
        "Select Percentile Display",
        [
            "Key Percentiles (P10, P25, P50, P75, P90)",
            "All Percentiles (P1-P100)"
        ],
        key="percentile_mode_v3"
    )

    # Filter year, state and measurement
    df_dist = df_percentile[
        (df_percentile["year"] == dist_year) &
        (df_percentile["state"].isin(dist_states)) &
        (df_percentile["variable"] == dist_measure)
    ].copy()

    # Apply percentile filter only for key mode
    if percentile_mode.startswith("Key Percentiles"):
        df_dist = df_dist[
            df_dist["percentile"].isin([10, 25, 50, 75, 90])
        ].copy()
    else:
        df_dist = df_dist[
            df_dist["percentile"].between(1, 100)
        ].copy()

    # Create chart
    if not df_dist.empty:

        df_dist = df_dist.sort_values(
            ["percentile", "state"]
        )

        fig_dist = px.bar(
            df_dist,
            x="percentile",
            y="income",
            color="state",
            barmode="group",
            title=f"Household Income by Percentile ({dist_year})",
            labels={
                "percentile": "Income Percentile",
                "income": "Household Income (RM)",
                "state": "State"
            },
            hover_data=["variable"]
        )

        # Improve chart layout
        fig_dist.update_layout(
            template="plotly_dark",
            xaxis_title="Income Percentile",
            yaxis_title="Household Income (RM)",
            legend_title="State",
            height=650,
            hovermode="closest"
        )

        if percentile_mode.startswith("Key Percentiles"):
            fig_dist.update_xaxes(
                tickmode="array",
                tickvals=[10, 25, 50, 75, 90]
            )
        else:
            fig_dist.update_xaxes(
                tickmode="linear",
                tick0=1,
                dtick=5,
                range=[0, 101]
            )

        st.plotly_chart(
            fig_dist,
            use_container_width=True
        )

        # Optional dataset information
        with st.expander("View Filtered Dataset"):
            st.write("Number of rows:", len(df_dist))
            st.write(
                "Number of percentiles:",
                df_dist["percentile"].nunique()
            )
            st.dataframe(df_dist)

    else:
        st.warning(
            "No data available for the selected filters. "
            "Please select another year, state or measurement."
        )



    
   
