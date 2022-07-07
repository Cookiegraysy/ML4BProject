import streamlit as st
import pathlib
import os

st.title("Data Understanding")
st.subheader("Collect Initial Data:")
st.markdown("For the data preparation part, we first took a close look at our dataset. Our dataset consists of five different materials: cardboard, glass, metal, paper, plastic and trash. Initially, our plan was to merge cardboard and paper into one trash type, as we felt that both always belonged in the same garbage can.
After some research, however, we found out that cardboard is often coated with plastic and that this is often compound packaging made of paper and plastic, which then no longer belongs into the blue garbage can, but into the yellow garbage can. 
Therefore, the division of the waste types has not changed in the end and we have left it as it was.")

st.markdown("We used the following code:")
