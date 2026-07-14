from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Rural Counties GHG Calculator",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
  .block-container {padding: 0 !important; max-width: 100% !important;}
  section.main > div {padding: 0 !important;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "ghg_dashboard.html"
html_content = html_path.read_text()

components.html(html_content, height=3400, scrolling=True)
