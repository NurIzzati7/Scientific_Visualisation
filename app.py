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

    @st.cache_data
    def load_life_data(path):
        data = pd.read_csv(path)
        data["year"] = pd.to_datetime(data["date"], errors="coerce").dt.year
        data["life_expectancy"] = pd.to_numeric(data["life_expectancy"], errors="coerce")
        return data.dropna(subset=["state", "year", "sex", "ethnicity", "life_expectancy"])

    life = load_life_data(data_path)
    years = sorted(life["year"].astype(int).unique().tolist())
    states = sorted(life["state"].unique().tolist())
    st.write(f"Analysis Period: {min(years)}–{max(years)}")

    selected_year = st.selectbox("Select Year", years, index=len(years)-1, key="life_year")
    selected_states = st.multiselect("Select State(s)", states, default=states, key="life_states")

    st.subheader("Life Expectancy by State and Gender")
    gender_data = life[
        (life["year"] == selected_year) &
        (life["state"].isin(selected_states)) &
        (life["ethnicity"] == "overall") &
        (life["sex"].isin(["male", "female"]))
    ]
    if gender_data.empty:
        st.info("No gender data for this selection.")
    else:
        fig_gender = px.bar(
            gender_data, x="state", y="life_expectancy", color="sex", barmode="group",
            labels={"state": "State", "life_expectancy": "Life Expectancy (Years)", "sex": "Gender"},
            title=f"Life Expectancy by State and Gender ({selected_year})"
        )
        fig_gender.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_gender, use_container_width=True)

    st.subheader("Life Expectancy Distribution by Ethnic Group")
    ethnic_options = ["bumi_malay", "bumi_other", "chinese", "indian"]
    selected_ethnic = st.multiselect(
        "Select Ethnic Group(s)", ethnic_options, default=ethnic_options, key="life_ethnic"
    )
    ethnic_data = life[
        (life["year"] == selected_year) &
        (life["state"].isin(selected_states)) &
        (life["sex"] == "both") &
        (life["ethnicity"].isin(selected_ethnic))
    ]
    if ethnic_data.empty:
        st.info("No ethnicity data for this selection.")
    else:
        fig_ethnic = px.box(
            ethnic_data, x="ethnicity", y="life_expectancy", points="all",
            labels={"ethnicity": "Ethnic Group", "life_expectancy": "Life Expectancy (Years)"},
            title=f"Life Expectancy Distribution by Ethnic Group ({selected_year})",
            hover_data=["state"]
        )
        st.plotly_chart(fig_ethnic, use_container_width=True)

    st.subheader("Life Expectancy Trends Across States")
    year_range = st.slider(
        "Select Year Range", min(years), max(years), (min(years), max(years)), key="life_range"
    )
    trend_data = life[
        (life["state"].isin(selected_states)) &
        (life["year"].between(*year_range)) &
        (life["sex"] == "both") &
        (life["ethnicity"] == "overall")
    ].sort_values("year")
    if trend_data.empty:
        st.info("No trend data for this selection.")
    else:
        fig_trend = px.line(
            trend_data, x="year", y="life_expectancy", color="state", markers=True,
            labels={"year": "Year", "life_expectancy": "Life Expectancy (Years)", "state": "State"},
            title="Life Expectancy Trends Across Malaysian States"
        )
        fig_trend.update_xaxes(tickmode="linear", dtick=1)
        st.plotly_chart(fig_trend, use_container_width=True)

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
