import streamlit as st
import pickle
import numpy as np

# Import the model
pipe = pickle.load(open('pipe.pkl','rb'))
car = pickle.load(open('car.pkl','rb'))

st.title('Car Price Prediction')
#name of the car
name = st.selectbox('Name',car['name'].unique())
# company
company = st.selectbox('Company',car['company'].unique())
# year
year = st.selectbox('Year',car['year'].unique())

# kms driven
kms_driven = st.selectbox('Kms Driven',car['kms_driven'].unique())
# fuel type
fuel_type = st.selectbox('Fuel Type',car['fuel_type'].unique())

# button
if st.button('Predict Price'):
    pass
# query
    query = np.array([name,company,year,kms_driven,fuel_type])

    query.reshape(1,5)
    st.title("The predicted price of this configuration is " + str(int(pipe.predict(query)[0])))








