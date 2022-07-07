import streamlit as st
import pathlib
import os
import pandas as pd

st.title("Evaluation")
st.header("Internet Samples")
st.markdown("We have uploaded a few examples of each category from the internet into our app.")

categories = ["Select Category", "Cardboard", "Glas", "Metal", "Paper", "Plastic"]
result = st.selectbox("Select a Category", categories)

def cardboard():
  st.subheader("Sample 1")
  st.image("./Results_img/cardboard1.jpg")
  st.subheader("Evaluation")
  st.image("./Results/cardboard_plot.png")
  st.subheader("Sample 2")
  st.image("./Results_img/cardboard2.jpg")
  st.subheader("Evaluation")
  st.image("./Results/cardboard2_amazon.png")

def glas():
  st.subheader("Sample 1")
  st.image("./Results_img/Glas2_gruen.jpg")
  st.subheader("Evaluation")
  st.image("./Results/glas2_gruen_plot.png")
  st.subheader("Sample 2")
  st.image("./Results_img/glas_joghurt.jpg")
  st.subheader("Evaluation")
  st.image("./Results/glas3_joghurt_plot.png")
  st.subheader("Sample 3")
  st.image("./Results_img/glas1.jpg")
  st.subheader("Evaluation")
  st.image("./Results/glas1_plot.png")
  st.subheader("Sample 4")
  st.image("./Results_img/Glas1_gruen.jpg")
  st.subheader("Evaluation")
  st.image("./Results/glas_gruen_plot.png")
  
def metal():
  st.subheader("Sample 1")
  st.image("./Results_img/metal1.jpg")
  st.subheader("Evaluation")
  st.image("./Results/metal1_plot.png")
  st.subheader("Sample 2")
  st.image("./Results_img/metal2.jpg")
  st.subheader("Evaluation")
  st.image("./Results/metal_alu1_plot.png")
  st.subheader("Sample 3")
  st.image("./Results_img/metal3.jpg")
  st.subheader("Evaluation")
  st.image("./Results/metal_aluhut_plot.png")
  st.subheader("Sample 4")
  st.image("./Results_img/metal4.jpg")
  st.subheader("Evaluation")
  st.image("./Results/metal_cola_rb_plot.png")
  st.subheader("Sampe 5")
  st.image("./Results_img/metal5.jpg")
  st.subheader("Evaluation")
  st.image("./Results/dosen_stapel_plot.png")
   
def paper():
  st.subheader("Sample 1")
  st.image("./Results_img/paper1.jpg")
  st.subheader("Evaluation")
  st.image("./Results/paper_zeitung_plot.png")
  st.subheader("Sample 2")
  st.image("./Results_img/paper2.jpg")
  st.subheader("Evaluation")
  st.image("./Results/paper2_zeitung_plot.png")
  st.subheader("Sample 3")
  st.image("./Results_img/paper3.jpg")
  st.subheader("Evaluation")
  st.image("./Results/paper3_broschuere_plot.png") 
  
def plastic():
  st.subheader("Sample 1")
  st.image("./Results_img/plastic1.jpg")
  st.subheader("Evaluation")
  st.image("./Results/plastic1_gruen_plot.png")
  st.subheader("Sample 2")
  st.image("./Results_img/plastic2.jpg")
  st.subheader("Evaluation")
  st.image("./Results/plastic2_shampoo_plot.png")
  st.subheader("Sample 3")
  st.image("./Results_img/plastic3.jpg")
  st.subheader("Evaluation")
  st.image("./Results/plastic3_tuete_plot.png")
  st.subheader("Sample 4")
  st.image("./Results_img/plastic4.jpg")
  st.subheader("Evaluation")
  st.image("./Results/plastic_tuete_b_plot.png")

def update():
  if result is "Cardboard":
    st.write(cardboard())
  elif result is "Glas":
    st.write(glas())
  elif result is "Metal":
    st.write(metal())
  elif result is "Paper":
    st.write(paper())
  elif result is "Plastic":
    st.write(plastic())

if st.button("Show samples"):
  update()
