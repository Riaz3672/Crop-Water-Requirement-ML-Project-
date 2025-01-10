import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import seaborn as sns 
crop_model=pickle.load(open('Crop_Water_Requirement.pkl','rb'))

st.title('Crop Water Requirement Model')
st.header('Input Variales')
CROP_TYPE=st.text_input('Crop Type')
SOIL_TYPE=st.text_input('Soil Type')
REGION=st.text_input('Region')
WEATHER_CONDITION=st.text_input('Weather')
TEMP_MIN=st.number_input('Minimum Temp')
TEMP_MAX=st.number_input('Maximum Temp')

if st.button('Water Requirement of  Crop'):
    data={
        'CROP_TYPE':[CROP_TYPE],
        'SOIL_TYPE':[SOIL_TYPE],
        'REGION':[REGION],
        'WEATHER_CONDITION':[WEATHER_CONDITION],
        'TEMP_MIN':[TEMP_MIN],
        'TEMP_MAX':[TEMP_MAX],
    }
    df=pd.DataFrame(data)
    prediction=crop_model.predict(df)
    st.write(prediction)
