import streamlit as st
import pathlib
import os
import pandas as pd

st.title("Evaluation")
st.header("Internet Samples")
st.markdown("We have uploaded a few examples of each category from the internet into our app.")

dir = './Result_img/'
dir2 = './Result/'

categories = ["Select Category", "Cardboard", "Glass", "Metal", "Paper", "Plastic"]
result = st.selectbox("Select a Category", categories)
./Result_img/cardboard1.jpg

def cardboard():
  st.write("Sample 1")
  st.write()
