import streamlit as st


st.expander("Data Preparation: ")
st.title("Data Preparation: ")
st.write("For the data preparation part, we first took a close look at our dataset. Our dataset consists of five different materials: cardboard, glass, metal, paper, plastic and trash. Initially, our plan was to merge cardboard and paper into one trash type, as we felt that both always belonged in the same garbage can. After some research, however, we found out that cardboard is often coated with plastic and that this is often compound packaging made of paper and plastic, which then no longer belongs into the blue garbage can, but into the yellow garbage can. Therefore, the division of the waste types has not changed in the end and we have left it as it was. ")



option = st.selectbox('Choose an image', ('cardboard', 'glass', 'metal', 'paper', 'plastic'))


type_path = os.path.join(dir + 'Garbage classification/Garbage classification/', option)
list_of_images = os.listdir(type_path)
image_box = st.selectbox("Sample", list_of_images)
sample_path = os.path.join(type_path, image_box)
image = Image.open(sample_path)
st.image(image, caption=image_box)
