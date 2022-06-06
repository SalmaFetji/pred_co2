import os
import streamlit as st
import pandas as pd
import numpy as np

### Load / Preprocess / Predict test.csv dataset ###

# MODEL_DIR = os.path.join(os.path.dirname('__file__'), 'first_model.h5')
# model = keras.models.load_model(MODEL_DIR)

###### STREAMLIT ######

### Header ###
st.title('Digit Prediction App')
st.header('Which prediction tool to use?')

### Upload test dataset ###
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data_test = pd.read_csv(uploaded_file)
    X_raw_final = data_test.values
    X_test_final = data_test.values.reshape(data_test.shape[0], 28, 28, 1)
    pred_testing = model.predict(X_test_final)
    pred_testing = np.argmax(pred_testing, axis=1)
    st.write('Predicted number : ' + str(pred_testing))

    ### Display button for prediction ###
    # if st.button('Predict a random image from our dataframe'):
    #     random_number = randrange(28000)
    #     st.write('Picture number ' + str(random_number))
    #     st.write('Predicted number : ' + str(pred_testing[random_number]))
    #     viz = viz_num(random_number)
    #     st.pyplot(viz)
else:
    st.write("Bonjour dans l'application")
