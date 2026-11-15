import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import textwrap

st.set_page_config(
    page_title="Scientific Visualisation",
    page_icon="📊",
    layout="wide"
)


# =========================
# SIDEBAR STYLING
# =========================
st.markdown("""
<style>

/* Sidebar background */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg, #0f172a 0%, #172554 100%
    );
    border-right: 1px solid #334155;
}

/* Sidebar title */
[data-testid="stSidebar"] h2 {
    color: #f8fafc;
    font-weight: 700;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #cbd5e1;
}

/* Radio navigation items */
[data-testid="stSidebar"] [role="radiogroup"] label {
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 7px;
    background: #1e293b;
    border: 1px solid #334155;
    transition: all 0.2s ease;
}

/* Hover effect */
[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #334155;
    border-color: #14b8a6;
}

/* Selected navigation item */
[data-testid="stSidebar"]
[role="radiogroup"] label:has(input:checked) {
    background: #134e4a;
    border-color: #2dd4bf;
}

/* Selected text */
[data-testid="stSidebar"]
[role="radiogroup"] label:has(input:checked) p {
    color: #ccfbf1;
    font-weight: 600;
}

/* Radio button accent */
[data-testid="stSidebar"] input[type="radio"] {
    accent-color: #2dd4bf;
}

</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR NAVIGATION
# =========================
with st.sidebar:

    st.markdown("## 📊 Malaysia Insights")

    st.caption(
        "Socioeconomic & Health Dashboard"
    )

    st.divider()

    page = st.radio(
        "🧭 Select Analysis",
        [
            "Home",
            "Maternal Death Analysis",
            "Life Expectancy Analysis",
            "Household Income Analysis"
        ],
        index=0
    )

    st.divider()

    st.markdown("### 📌 Dashboard Information")

    st.caption(
        "Explore three Malaysian datasets "
        "using interactive visualisations."
    )

    st.markdown("**Data Source:** DOSM")

    st.caption(
        "Built with Python, Streamlit & Plotly"
    )



if page == "Home":

    # =========================
    # HOME PAGE STYLING
    # =========================
    st.markdown("""
    <style>
    .home-hero {
        background: linear-gradient(120deg, #0f172a, #164e63, #0f766e);
        padding: 40px 35px;
        border-radius: 20px;
        border: 1px solid #155e75;
        margin-bottom: 28px;
    }

    .home-eyebrow {
        color: #99f6e4;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .home-hero h1 {
        color: #ffffff;
        font-size: clamp(26px, 3vw, 38px);
        font-weight: 750;
        line-height: 1.3;
        margin-bottom: 15px;
    }

    .home-hero p {
        color: #cbd5e1;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 0;
    }

    .home-kpi {
        background: linear-gradient(145deg, #1e293b, #172033);
        padding: 25px 15px;
        border-radius: 16px;
        border: 1px solid #334155;
        text-align: center;
        min-height: 155px;
        transition: all 0.25s ease;
    }

    .home-kpi:hover {
        transform: translateY(-4px);
        border-color: #14b8a6;
    }

    .home-kpi-icon {
        font-size: 27px;
        margin-bottom: 8px;
    }

    .home-kpi-value {
        color: #ffffff;
        font-size: 30px;
        font-weight: 700;
    }

    .home-kpi-label {
        color: #94a3b8;
        font-size: 14px;
        margin-top: 5px;
    }

    .home-dataset {
        background: #1e293b;
        padding: 25px 22px;
        border-radius: 16px;
        border: 1px solid #334155;
        min-height: 260px;
        transition: all 0.25s ease;
    }

    .home-dataset:hover {
        transform: translateY(-5px);
        border-color: #64748b;
        box-shadow: 0 10px 25px rgba(0,0,0,0.18);
    }

    .home-dataset-icon {
        font-size: 32px;
        margin-bottom: 12px;
    }

    .home-dataset h3 {
        color: #ffffff;
        font-size: 21px;
        margin-bottom: 14px;
    }

    .home-dataset p {
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.7;
        margin-top: 15px;
    }

    .home-tag {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        line-height: 1.5;
    }

    .home-about {
        background: #1e293b;
        padding: 26px;
        border-radius: 16px;
        border: 1px solid #334155;
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.9;
    }

    .home-about strong {
        color: #5eead4;
    }

    .home-about p {
        margin-top: 14px;
    }

    .home-guide {
        background: #134e4a;
        border-left: 4px solid #2dd4bf;
        border-radius: 12px;
        padding: 18px 22px;
        color: #ccfbf1;
        font-size: 14px;
        margin-top: 22px;
    }

    .home-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        padding: 25px 10px;
        margin-top: 20px;
        border-top: 1px solid #334155;
    }

    @media (max-width: 768px) {
        .home-hero {
            padding: 28px 20px;
        }

        .home-dataset {
            min-height: auto;
        }

        .home-kpi {
            min-height: auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Helper function to render HTML correctly
    def home_html(html):
        st.markdown(
            textwrap.dedent(html).strip(),
            unsafe_allow_html=True
        )

    # =========================
    # HERO SECTION
    # =========================
    home_html("""
    <div class="home-hero">
        <div class="home-eyebrow">MALAYSIA DATA ANALYTICS</div>
        <h1>📊 Malaysia Socioeconomic &amp; Health Insights</h1>
        <p>
            An interactive dashboard for exploring maternal deaths,
            life expectancy, and household income across Malaysia.
        </p>
    </div>
    """)

    # =========================
    # DASHBOARD OVERVIEW
    # =========================
    st.subheader("📌 Dashboard Overview")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        home_html("""
        <div class="home-kpi">
            <div class="home-kpi-icon">📁</div>
            <div class="home-kpi-value">3</div>
            <div class="home-kpi-label">Datasets</div>
        </div>
        """)

    with col2:
        home_html("""
        <div class="home-kpi">
            <div class="home-kpi-icon">📊</div>
            <div class="home-kpi-value">3</div>
            <div class="home-kpi-label">Visualisations</div>
        </div>
        """)

    with col3:
        home_html("""
        <div class="home-kpi">
            <div class="home-kpi-icon">📍</div>
            <div class="home-kpi-value">Malaysia</div>
            <div class="home-kpi-label">Data Coverage</div>
        </div>
        """)

    st.write("")
    st.divider()

    # =========================
    # EXPLORE DATASETS
    # =========================
    st.subheader("🔎 Explore the Datasets")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        home_html("""
        <div class="home-dataset"
             style="border-top: 4px solid #fb7185;">
            <div class="home-dataset-icon">🩺</div>
            <h3>Maternal Death</h3>
            <span class="home-tag"
                  style="background:#4c0519;color:#fda4af;">
                2000–2025 | Line Chart
            </span>
            <p>
                Explore maternal death trends and compare
                the number of deaths across Malaysian states.
            </p>
        </div>
        """)

    with col2:
        home_html("""
        <div class="home-dataset"
             style="border-top: 4px solid #38bdf8;">
            <div class="home-dataset-icon">👥</div>
            <h3>Life Expectancy</h3>
            <span class="home-tag"
                  style="background:#082f49;color:#7dd3fc;">
                2022–2026 | Grouped Bar Chart
            </span>
            <p>
                Compare life expectancy by gender,
                ethnicity, and state using interactive
                year selection.
            </p>
        </div>
        """)

    with col3:
        home_html("""
        <div class="home-dataset"
             style="border-top: 4px solid #34d399;">
            <div class="home-dataset-icon">💰</div>
            <h3>Household Income</h3>
            <span class="home-tag"
                  style="background:#064e3b;color:#a7f3d0;">
                2019, 2022, 2024 | Bubble Chart
            </span>
            <p>
                Explore household income differences
                across states and income percentiles
                using interactive filters.
            </p>
        </div>
        """)

    st.write("")
    st.divider()

   
    # =========================
    # ABOUT THIS PROJECT
    # =========================
    st.subheader("ℹ️ About This Project")

    st.markdown("""
<div class="home-about">
    This dashboard was developed using
    <strong>Python, Streamlit, and Plotly</strong>
    to visualise three Malaysian datasets from
    the Department of Statistics Malaysia (DOSM).
    <p>
        It includes an interactive line chart for maternal deaths,
        a grouped bar chart for life expectancy, and a bubble chart
        for household income.
    </p>
    <p>
        Users can select different states, years, and other filters
        to explore the data and compare the results.
    </p>
</div>
""", unsafe_allow_html=True)


    # =========================
    # NAVIGATION GUIDE
    # =========================
    home_html("""
    <div class="home-guide">
        👈 <strong>Get Started:</strong>
        Select an analysis from the sidebar
        to explore the interactive visualisations.
    </div>
    """)

    # =========================
    # FOOTER
    # =========================
    home_html("""
    <div class="home-footer">
        Data Source: DOSM |
        Developed with Python, Streamlit &amp; Plotly
    </div>
    """)


# =========================
# MATERNAL DEATH ANALYSIS
# =========================
elif page == "Maternal Death Analysis":

    # PAGE STYLING
    st.markdown("""
    <style>
    .analysis-hero {
        background: linear-gradient(120deg, #0f172a, #164e63);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #155e75;
        margin-bottom: 22px;
    }

    .analysis-hero h1 {
        color: #ffffff;
        font-size: 32px;
        margin: 0 0 10px 0;
    }

    .analysis-hero p {
        color: #cbd5e1;
        font-size: 15px;
        margin: 0;
    }

    .analysis-objective {
        background: #134e4a;
        border-left: 4px solid #2dd4bf;
        padding: 18px 22px;
        border-radius: 12px;
        color: #ccfbf1;
        font-size: 15px;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    .analysis-kpi {
        background: #1e293b;
        padding: 22px 15px;
        border: 1px solid #334155;
        border-radius: 14px;
        text-align: center;
        min-height: 125px;
    }

    .analysis-kpi-label {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .analysis-kpi-value {
        color: #ffffff;
        font-size: 29px;
        font-weight: 700;
    }

    .analysis-note {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 22px;
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.8;
    }

    .analysis-footer {
        color: #94a3b8;
        font-size: 13px;
        text-align: center;
        margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    # PAGE HEADER
    st.markdown(
        '<div class="analysis-hero">'
        '<h1>🩺 Maternal Death Analysis</h1>'
        '<p>Exploring maternal death trends across Malaysian states | 2000–2025</p>'
        '</div>',
        unsafe_allow_html=True
    )

    # OBJECTIVE
    st.markdown(
        '<div class="analysis-objective">'
        '<strong>🎯 Objective:</strong> '
        'To analyse the distribution and trends of maternal mortality '
        'across Malaysian states.'
        '</div>',
        unsafe_allow_html=True
    )

    # LOAD DATASET
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

    # DATA FILTERS
    st.subheader("⚙️ Data Filters")

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

    # FILTER DATASET
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

        # LINE CHART
        st.subheader("📈 Maternal Death Trends by State")

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
            template="plotly_dark",
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font=dict(color="#e2e8f0"),
            title_font=dict(size=18),
            hovermode="x unified",
            legend_title_text="State",
            margin=dict(l=25, r=25, t=65, b=30),
            xaxis=dict(
                showgrid=False,
                title="Year"
            ),
            yaxis=dict(
                gridcolor="#334155",
                title=label
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # SUMMARY BOX
        st.subheader("📊 Summary Box")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                '<div class="analysis-kpi">'
                '<div class="analysis-kpi-label">📍 States Selected</div>'
                f'<div class="analysis-kpi-value">{filtered["state"].nunique()}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                '<div class="analysis-kpi">'
                '<div class="analysis-kpi-label">📅 Years Covered</div>'
                f'<div class="analysis-kpi-value">{filtered["year"].nunique()}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                '<div class="analysis-kpi">'
                '<div class="analysis-kpi-label">🏆 Highest Observed Value</div>'
                f'<div class="analysis-kpi-value">{chart_data[measure].max():,.2f}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        # INTERPRETATION
        st.subheader("💡 Interpretation")

        st.markdown(
            '<div class="analysis-note">'
            'The line chart shows changes in maternal mortality '
            'across selected Malaysian states over the chosen period. '
            'Users can compare trends between states and identify '
            'increases or decreases over time. Differences between '
            'the lines show variations in the selected maternal '
            'mortality measurement across states.'
            '</div>',
            unsafe_allow_html=True
        )

        # DATA SOURCE
        st.markdown(
            '<div class="analysis-footer">'
            'Data Source: Department of Statistics Malaysia (DOSM)'
            '</div>',
            unsafe_allow_html=True
        )



# =========================
# LIFE EXPECTANCY ANALYSIS
# =========================
elif page == "Life Expectancy Analysis":

    # PAGE STYLING
    st.markdown("""
    <style>
    .life-hero {
        background: linear-gradient(120deg, #0f172a, #164e63);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #155e75;
        margin-bottom: 22px;
    }

    .life-hero h1 {
        color: #ffffff;
        font-size: 32px;
        margin: 0 0 10px 0;
    }

    .life-hero p {
        color: #cbd5e1;
        font-size: 15px;
        margin: 0;
    }

    .life-objective {
        background: #134e4a;
        border-left: 4px solid #2dd4bf;
        padding: 18px 22px;
        border-radius: 12px;
        color: #ccfbf1;
        font-size: 15px;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    .life-kpi {
        background: #1e293b;
        padding: 22px 15px;
        border: 1px solid #334155;
        border-radius: 14px;
        text-align: center;
        min-height: 125px;
    }

    .life-kpi-label {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .life-kpi-value {
        color: #ffffff;
        font-size: 29px;
        font-weight: 700;
    }

    .life-note {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 22px;
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.8;
    }

    .life-footer {
        color: #94a3b8;
        font-size: 13px;
        text-align: center;
        margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================
    # PAGE HEADER
    # =========================
    st.markdown(
        '<div class="life-hero">'
        '<h1>👥 Life Expectancy Analysis</h1>'
        '<p>Comparing life expectancy across Malaysian states | 2022–2026</p>'
        '</div>',
        unsafe_allow_html=True
    )

    # OBJECTIVE
    st.markdown(
        '<div class="life-objective">'
        '<strong>🎯 Objective:</strong> '
        'To examine variations in life expectancy across '
        'Malaysian states based on gender, ethnicity, and time.'
        '</div>',
        unsafe_allow_html=True
    )

    # =========================
    # LOAD DATASET
    # =========================
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

    # =========================
    # DATA FILTERS
    # =========================
    st.subheader("⚙️ Data Filters")

    years = sorted(
        df_life["year"].astype(int).unique().tolist()
    )

    selected_year = st.selectbox(
        "Select Year",
        years,
        index=len(years) - 1
    )

    states = sorted(df_life["state"].unique().tolist())

    default_states = [
        "Johor",
        "Selangor",
        "Melaka",
        "Kedah",
        "Sarawak"
    ]

    selected_states = st.multiselect(
        "Select State(s)",
        states,
        default=[
            s for s in default_states if s in states
        ]
    )

    comparison_type = st.selectbox(
        "Select Comparison Type",
        ["Gender", "Ethnicity"]
    )

    # =========================
    # FILTER DATA
    # =========================
    if comparison_type == "Gender":

        filtered = df_life[
            (df_life["year"] == selected_year)
            & df_life["state"].isin(selected_states)
            & (df_life["ethnicity"] == "overall")
            & df_life["sex"].isin(["male", "female"])
        ].copy()

        category = "sex"

        chart_title = (
            f"Life Expectancy by State and Gender ({selected_year})"
        )

    else:

        filtered = df_life[
            (df_life["year"] == selected_year)
            & df_life["state"].isin(selected_states)
            & (df_life["sex"] == "both")
            & df_life["ethnicity"].isin([
                "bumi_malay",
                "bumi_other",
                "chinese",
                "indian"
            ])
        ].copy()

        category = "ethnicity"

        chart_title = (
            f"Life Expectancy by State and Ethnicity ({selected_year})"
        )

        ethnic_labels = {
            "bumi_malay": "Bumiputera Malay",
            "bumi_other": "Other Bumiputera",
            "chinese": "Chinese",
            "indian": "Indian"
        }

        filtered["ethnicity"] = (
            filtered["ethnicity"].replace(ethnic_labels)
        )

    if filtered.empty:
        st.warning(
            "No data available for the selected filters. "
            "Please choose another year or state."
        )

    else:

        # =========================
        # PREPARE CHART DATA
        # =========================
        chart_data = (
            filtered.groupby(
                ["state", category], as_index=False
            )["life_expectancy"].mean()
        )

        # =========================
        # GROUPED BAR CHART
        # =========================
        st.subheader("📊 Life Expectancy Comparison")

        fig = px.bar(
            chart_data,
            x="state",
            y="life_expectancy",
            color=category,
            barmode="group",
            title=chart_title,
            labels={
                "state": "State",
                "life_expectancy": "Life Expectancy (Years)",
                "sex": "Gender",
                "ethnicity": "Ethnic Group"
            }
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font=dict(color="#e2e8f0"),
            title_font=dict(size=18),
            xaxis_tickangle=-30,
            legend_title_text=comparison_type,
            height=580,
            margin=dict(l=30, r=30, t=65, b=40),
            xaxis=dict(
                title="State",
                showgrid=False
            ),
            yaxis=dict(
                title="Life Expectancy (Years)",
                gridcolor="#334155"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =========================
        # SUMMARY BOX
        # =========================
        st.subheader("📊 Summary Box")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                '<div class="life-kpi">'
                '<div class="life-kpi-label">📍 States Selected</div>'
                f'<div class="life-kpi-value">{chart_data["state"].nunique()}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                '<div class="life-kpi">'
                '<div class="life-kpi-label">👥 Comparison Type</div>'
                f'<div class="life-kpi-value">{comparison_type}</div>'
                '</div>',
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                '<div class="life-kpi">'
                '<div class="life-kpi-label">🏆 Highest Life Expectancy</div>'
                f'<div class="life-kpi-value">{chart_data["life_expectancy"].max():.1f} years</div>'
                '</div>',
                unsafe_allow_html=True
            )

        # =========================
        # INTERPRETATION
        # =========================
        st.subheader("💡 Interpretation")

        interpretation = (
            "The grouped bar chart compares life expectancy "
            "across selected Malaysian states based on "
            f"{comparison_type.lower()} in {selected_year}. "
            "Users can compare demographic groups and "
            "explore differences between states. "
            "The year filter also allows comparisons "
            "across different years."
        )

        st.markdown(
            '<div class="life-note">'
            + interpretation +
            '</div>',
            unsafe_allow_html=True
        )

        # =========================
        # DATA SOURCE
        # =========================
        st.markdown(
            '<div class="life-footer">'
            'Data Source: Department of Statistics Malaysia (DOSM)'
            '</div>',
            unsafe_allow_html=True
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
                "year", "state", "percentile",
                "variable", "income"
            ]
        )

    df_income = load_income_data(data_path)

    # Data Filters
    st.subheader("Data Filters")

    years = sorted(
        df_income["year"].astype(int).unique().tolist()
    )

    selected_year = st.selectbox(
        "Select Year",
        years,
        index=len(years) - 1
    )

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

    percentile_mode = st.selectbox(
        "Select Percentile Display",
        [
            "Key Percentiles (P10, P25, P50, P75, P90)",
            "All Percentiles (P1-P100)"
        ]
    )

    # Filter dataset
    filtered = df_income[
        (df_income["year"] == selected_year)
        & df_income["state"].isin(selected_states)
        & (df_income["variable"] == selected_measure)
    ].copy()

    if percentile_mode.startswith("Key Percentiles"):
        filtered = filtered[
            filtered["percentile"].isin(
                [10, 25, 50, 75, 90]
            )
        ].copy()
    else:
        filtered = filtered[
            filtered["percentile"].between(1, 100)
        ].copy()

    if filtered.empty:
        st.warning(
            "No data available for the selected filters. "
            "Please choose another year, state, "
            "measurement or percentile display."
        )

    else:
        # Prepare bubble chart data
        chart_data = (
            filtered.groupby(
                ["state", "percentile"], as_index=False
            )["income"].mean()
            .sort_values(["state", "percentile"])
        )

        # One Interactive Bubble Chart
        st.subheader(
            "Household Income Distribution by Percentile"
        )

        fig = px.scatter(
            chart_data,
            x="percentile",
            y="income",
            color="state",
            size="income",
            size_max=35,
            title=(
                "Household Income by State and Percentile "
                f"({selected_year})"
            ),
            labels={
                "percentile": "Income Percentile",
                "income": "Household Income (RM)",
                "state": "State"
            },
            hover_data={
                "state": True,
                "percentile": True,
                "income": ":,.2f"
            }
        )

        fig.update_traces(
            marker=dict(
                opacity=0.7,
                line=dict(width=1)
            )
        )

        fig.update_layout(
            template="plotly_dark",
            height=650,
            legend_title_text="State",
            xaxis_title="Income Percentile",
            yaxis_title="Household Income (RM)"
        )

        if percentile_mode.startswith("Key Percentiles"):
            fig.update_xaxes(
                tickmode="array",
                tickvals=[10, 25, 50, 75, 90]
            )
        else:
            fig.update_xaxes(
                range=[0, 101],
                dtick=10
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
                "Percentiles Displayed",
                chart_data["percentile"].nunique()
            )

        with col3:
            st.metric(
                "Highest Household Income",
                f"RM {chart_data['income'].max():,.2f}"
            )

        # Interpretation
        st.subheader("Interpretation")

        st.write(
            "The interactive bubble chart illustrates "
            "household income differences across selected "
            "Malaysian states and income percentiles. "
            "The position and size of each bubble represent "
            "the household income value, while different "
            "colours distinguish states. Users can explore "
            "changes across different years and income "
            "measurements using the available filters."
        )

        st.caption(
            "Source: Department of Statistics Malaysia (DOSM)"
        )



    
   
