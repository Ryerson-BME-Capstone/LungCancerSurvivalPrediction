import requests
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import pandas as pd
import numpy as np
from pydantic import BaseModel
import json
from tensorflow.keras.models import load_model

model = load_model('prediction') 

header = Image.open('image.jpg')
happy = Image.open('happy.jpg')
sad = Image.open('sad.jpg') 


st.title("Lung Cancer Survival Prediction System")
st.text('')

st.image(header, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 
st.text('')
st.text('')


st.caption("The following is a survival prediction model that accepts genomic data and outputs a survivability in the form of a number between 0 and 1. A number greater than 0.5 indicates surviving, while a number below 0.5 indicates not surviving. The survival prediction is based on a 5 year time span. Please upload your data in a .txt file format.", unsafe_allow_html=False) 

uploaded_file=st.file_uploader("Upload Genomic Data Here", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)


if uploaded_file is not None:
   dataframe = pd.read_csv(uploaded_file)
   
   st.write(dataframe)
    
   uploadbutton=st.button('Upload',disabled= False)

  
       
if st.button('Predict!'):
    y = model.predict(dataframe)
    y = [0 if val < 0.5 else 1 for val in y]
    if y[0] == 1:
        survival = 'You will survive.'
        st.image(happy, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 
    if y[0] == 0:
        survival = 'You will not survive.'
        st.image(sad, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto") 
    st.write(survival) ##begin prediction and output results here
        
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.subheader('FAQ', anchor=None)

st.text('What is the current accuracy of the model?')

st.caption('The current accuracy of the model is 74%.') 

st.text('What kind of genomic data is used in the prediction?')

st.caption('The model currently takes in RPPA (Reverse phase protein arrays) data and converts it in to prediction. Age and gender currently do not play a role in the prediction of the model.') 

st.text('What is RPPA?')

st.caption('RPPA or Reverse Phase Protein arrays involve taking samples of tissue and/or bodily fluid (e.g. urine, saliva, or serum), and blotting them into a single array. Each array has a specific antibody, which can detect the presence or expression of a certain protein or antigen. Ep-CAM is one antigen that is a known tumor marker and a marker for tumor-initiating cells.')

st.text('Where was the data acquired to produce the model?')

st.caption('The model was produced using data from the TCGA and the Pancancer Survival Prediction community.') 






st.text("")
st.text("")
st.text("")

st.subheader('Acknowledgements', anchor=None)


st.caption('Throughout the development of this project we have recieved a great deal of support and assistance.')
st.text("")
st.caption('We would like to thank our Faculty Lab Coordinator, Professor Omar Grant, for his continued support and assistance in the development of this web app and model. We could not have done it without your expertise and guidance. Your feedback was insightful and greatly helped us.') 
st.text("")
st.caption('We would also like to thank our friends and family for their continued support, and counsel, allowing us to keep pushing forward even when things got difficult.')
