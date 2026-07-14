import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Rural Counties GHG Calculator",
    page_icon="♻️",
    layout="wide",
)

DN = "#1F5F3E"
AM = "#B08D00"
TU = "#2A5F7A"

DATA = {
    "Del Norte": {
        "disposal": {2020: 21672, 2021: 21916, 2022: 26142, 2023: 22859, 2024: 24516, 2025: 18720},
        "population": 27000,
        "baseline_ghg": 1391,
        "color": DN,
        "tier": "Tier 1 (monthly RDRS)",
    },
    "Amador": {
        "disposal": {2020: 37044, 2021: 36363, 2022: 35660, 2023: 35244, 2024: 32933, 2025: 25311},
        "population": 40000,
        "baseline_ghg": -1826,
        "color": AM,
        "tier": "Tier 2 (state quarterly)",
    },
    "Tuolumne": {
        "disposal": {2020: 45799, 2021: 48336, 2022: 47240, 2023: 48370, 2024: 50101, 2025: 36134},
        "population": 55000,
        "baseline_ghg": -10456,
        "color": TU,
        "tier": "Tier 2 (state quarterly)",
    },
}

st.title("Rural Counties GHG Calculator")
st.caption("Del Norte, Amador, Tuolumne. Baseline emissions and scenario modeling. Preview v0.1.")

county = st.selectbox("County", list(DATA.keys()))
data = DATA[county]

col1, col2, col3, col4 = st.columns(4)
col1.metric("2024 disposal", f"{data['disposal'][2024]:,} tons")
col2.metric("Population", f"~{data['population']:,}")
col3.metric("Per capita disposal", f"{data['disposal'][2024]/data['population']:.2f} tons per resident")
col4.metric("Net baseline GHG", f"{data['baseline_ghg']:+,} MTCO2e/yr")

st.caption(f"Data confidence: {data['tier']}")

st.divider()

st.subheader("Waste disposed per year")
st.caption("All three counties. 2025 is partial year reporting.")

fig1 = go.Figure()
for c, d in DATA.items():
    fig1.add_trace(go.Scatter(
        x=list(d["disposal"].keys()),
        y=list(d["disposal"].values()),
        mode="lines+markers",
        name=c,
        line=dict(color=d["color"], width=3),
        marker=dict(color=d["color"], size=9, line=dict(color="white", width=1.5)),
    ))
fig1.update_layout(
    font=dict(family="Arial", size=13),
    xaxis_title="Year",
    yaxis_title="Tons disposed per year",
    height=420,
    margin=dict(l=20, r=20, t=30, b=20),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hovermode="x unified",
)
fig1.update_xaxes(showgrid=False, tickmode="linear")
fig1.update_yaxes(gridcolor="#E0E0E0", tickformat=",")
st.plotly_chart(fig1, use_container_width=True)

st.divider()

st.subheader("Net GHG emissions by county (EPA WARM v16)")
st.caption(
    "Sink means the landfill locks away more carbon in undecomposed wood and paper than the "
    "food and mixed waste give off as methane. The next iteration adds scenario toggles for food "
    "recovery, composting, anaerobic digestion, and biochar."
)

counties = list(DATA.keys())
values = [d["baseline_ghg"] for d in DATA.values()]
colors = [d["color"] for d in DATA.values()]

fig2 = go.Figure(go.Bar(
    x=counties, y=values,
    marker_color=colors,
    text=[f"{v:+,}" for v in values],
    textposition="outside",
    textfont=dict(size=16),
))
fig2.update_layout(
    font=dict(family="Arial", size=13),
    yaxis_title="MTCO2e per year",
    height=420,
    margin=dict(l=20, r=20, t=30, b=20),
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False,
)
fig2.update_yaxes(gridcolor="#E0E0E0", zeroline=True, zerolinecolor="#1A1A1A", zerolinewidth=2)
fig2.update_xaxes(showgrid=False)
st.plotly_chart(fig2, use_container_width=True)

st.info(
    "v0.1 preview. Interactive scenario toggles (food rescue, windrow composting, "
    "community and backyard composting, anaerobic digestion, biochar) are coming in the next iteration. "
    "Contact Brittany Mahoney at Blue Strike Environmental for status."
)
