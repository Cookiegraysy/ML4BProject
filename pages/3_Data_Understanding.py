import streamlit as st
import pathlib
import os

st.title("Data Understanding")
st.subheader("Collect Initial Data:")
st.markdown("For the data preparation part, we first took a close look at our dataset. Initially, our plan was to merge cardboard and paper into one trash type, as we felt that both always belonged in the same garbage can. After some research, however, we found out that cardboard is often coated with plastic and that this is often compound packaging made of paper and plastic, which then no longer belongs into the blue garbage can, but into the yellow garbage can. Therefore, the division of the waste types has not changed in the end and we have left it as it was.")
st.markdown("We used the following code to import our dataset to be able to further work on it then:")
st.code('''
import os
import matplotlib.pyplot as plt
from PIL import Image
import math

dir_address = "D:/Garbage-Classification/Dataset"

classes = os.listdir(dir_address)
print(classes)
''')

st.subheader("Describe Data:")
st.markdown("Our dataset consists of five different materials: cardboard, glass, metal, paper, plastic and trash.")
st.markdown("To display the splitting of the garbage types, we used the following code: ")

st.code('''
dir_address = "D:/Garbage-Classification/Dataset/train"

train_classes = os.listdir(dir_address)
print(train_classes)
''')
