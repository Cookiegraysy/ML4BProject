import streamlit as st

st.title("Modeling")

st.subheader("Select Modeling Technique: ")
st.markdown(
    "In the modeling part we used 'Convolutional Neural Network' as our modeling technique, "
    "which is a type of neural network model allows us to extract higher representations for "
    "the image content. Unlike the classical image recognition where you define the image "
    "features yourself, CNN takes the image’s raw pixel data, trains the model, then extracts "
    "the features automatically for better classification. ",
    True)

st.markdown("<hr/>", True)

st.subheader("Build Model: ")
st.code('''

model=Sequential()
#Convolution blocks
model.add(Conv2D(32, kernel_size = (3,3), padding='same',input_shape=(300,300,3),activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(64, kernel_size = (3,3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(32, kernel_size = (3,3), padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=2))

#Classification layers
model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(6,activation='softmax'))
''')

st.markdown("<hr/>", True)

st.subheader("Full Model Architecture: ")
st.code('''

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 300, 300, 32)      896       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 150, 150, 32)     0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 150, 150, 64)      18496     
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 75, 75, 64)       0         
 2D)                                                             
                                                                 
 conv2d_2 (Conv2D)           (None, 75, 75, 32)        18464     
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 37, 37, 32)       0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 43808)             0         
                                                                 
 dense (Dense)               (None, 64)                2803776   
                                                                 
 dropout (Dropout)           (None, 64)                0         
                                                                 
 dense_1 (Dense)             (None, 32)                2080      
                                                                 
 dropout_1 (Dropout)         (None, 32)                0         
                                                                 
 dense_2 (Dense)             (None, 6)                 198       
                                                                 
=================================================================
Total params: 2,843,910
Trainable params: 2,843,910
Non-trainable params: 0
_________________________________________________________________

''')

st.markdown("<hr/>", True)

st.subheader("Model Compilation and Training: ")
st.code('''

model.compile(optimizer = 'Adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(train_generator,
          epochs=10,
          steps_per_epoch=2184//32,
          validation_data= test_generator)

''')
st.image("./visualize/training.jpg")


