from pages import information, model_demo, Modeling, Evaluation
import streamlit as st

# Page Settings
st.set_page_config(page_title="Garbage Classification")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# Load Animation
animation_symbol1 = "♻️"
animation_symbol2 = "🗑️"
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol1}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol2}</div>
    """,
    unsafe_allow_html=True,
)
PAGES = {
    "Model Demo": model_demo,
    "About The Project": information,
    "Modeling": Modeling,
    "Evaluation": Evaluation
}

st.sidebar.title('Garbage Classification')
selection = st.sidebar.radio("Navigate To", list(PAGES.keys()))
page = PAGES[selection]
page.app()

