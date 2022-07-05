import streamlit as st

with st.expander("1. Business Understanding: ")
st.title("1. Business Understanding: ")
st.write("Climate change is a problem that young people, in particular, have been addressing over the last few years. People use vast amounts of packaging waste, etc. and thus destroy our planet step by step. The earth is full of garbage. One step to counter this problem is recycling. In Germany, fortunately, everyone is obliged to recycle properly. In other countries this is unfortunately neglected. Since it is not a compulsory task for many people, they have no idea how to recycle properly. This prevents many people from even trying, resulting in a lot of garbage ending up in our oceans.", True)

with st.expander("2. Data Preparation: ")
st.title("2. Data Preparation: ")
st.write("For the data preparation part, we first took a close look at our dataset. Our dataset consists of five different materials: cardboard, glass, metal, paper, plastic and trash. Initially, our plan was to merge cardboard and paper into one trash type, as we felt that both always belonged in the same garbage can."
         "After some research, however, we found out that cardboard is often coated with plastic and that this is often compound packaging made of paper and plastic, which then no longer belongs into the blue garbage can, but into the yellow garbage can."
         "Therefore, the division of the waste types has not changed in the end and we have left it as it was. We split the dataset into a training and a test dataset. 85% of the data is for training and 15% for testing. The subdivision was done manually. ")

st.write("We used the following code:")

st.image(