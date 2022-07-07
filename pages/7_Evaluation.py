import streamlit as st
import pathlib
import os
import pandas as pd

st.title("Evaluation")
st.headliner("Internet Samples")
st.markdown("We have uploaded a few examples of each category from the internet into our app.")

categories = ["Select Category", "Cardboard", "Glass", "Metal", "Paper", "Plastic"]
result = st.selectbox("Select a Category", categories)
