from PIL import Image
import streamlit as st
import os
import pandas as pd

def app():
  st.title("Data Preparation")
  st.subheader("Data Split")
  number_of_samples = df[['img_name', 'category']].groupby('category').count()
  number_of_samples
