import streamlit as st

st.set_page_config(
    page_title="Blue Strike Environmental, Dashboards",
    page_icon="🌱",
    layout="wide",
)

st.title("Blue Strike Environmental")
st.subheader("Interactive dashboards for our climate and GHG projects")

st.markdown(
    "Welcome to the Blue Strike Environmental dashboard portal. "
    "Select a project from the sidebar to explore its analysis and scenarios."
)

st.info(
    "**Rural Counties GHG Calculator** — Del Norte, Amador, and Tuolumne. "
    "Baseline emissions, material breakdowns, diversion scenarios. Currently in preview (v0.1)."
)

st.caption("Blue Strike Environmental, 2026")
