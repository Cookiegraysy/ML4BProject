import streamlit as st
import pathlib
import os
from PIL import Image

st.title("Data Preparation")
st.subheader("Data Cleaning")
st.markdown("The Dataset is in a good condition. Therefore no cleaning had to be done.")
st.subheader("Data Split")
st.markdown("We've split the Dataset into a Training and Test set. We split about 15% of each category and moved it to the test set and the remaing pictures we left as the training set.")

dir = './Dataset/'
data_dir = pathlib.Path(os.path.join(dir, './train/'))
data_dir2 = pathlib.Path(os.path.join(dir, './test/'))

dicts = []

#Training set
for label in os.listdir(data_dir):
    directory = os.path.join(data_dir, label)
    samples = os.listdir(directory)

    for img in samples:
        z = Image.open(os.path.join(directory, img))
        x = {'Training set': img, 'category': label, 'size': z.size}
        dicts.append(x)

df1 = pd.DataFrame.from_dict(dicts)

#Test set
for label in os.listdir(data_dir2):
    directory = os.path.join(data_dir2, label)
    samples = os.listdir(directory)

    for img in samples:
        z = Image.open(os.path.join(directory, img))
        x = {'Test set': img, 'category': label, 'size': z.size}
        dicts.append(x)

df2 = pd.DataFrame.from_dict(dicts)

#Combine Sets
result = pd.concat([df1, df2], axis=1, ignore_index=True)

st.write("result")
