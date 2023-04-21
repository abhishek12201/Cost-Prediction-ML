import streamlit as st
import pickle
import numpy as np

# Import the model
Lin = pickle.load(open('Linw.pkl','rb'))
df = pickle.load(open('dfw.pkl','rb'))

# Title
st.title("Gearbox Price Predictor")

# Parameters
Planet_Gears = st.selectbox('Planet_Gears',df['Planet_Gears'].unique())
Input_Shaft = st.selectbox('Input_Shaft',df['Input_Shaft'].unique())
Output_Shaft = st.selectbox('Output_Shaft',df['Output_Shaft'].unique())
Housing = st.selectbox('Housing',df['Housing'].unique())
Ring_Gear = st.selectbox('Ring_Gear',df['Ring_Gear'].unique())
Sun_Gear = st.selectbox('Sun_Gear',df['Sun_Gear'].unique())
Carrier = st.selectbox('Carrier',df['Carrier'].unique())
Bearings = st.selectbox('Bearings',df['Bearings'].unique())
Seals = st.selectbox('Seals',df['Seals'].unique())


if st.button('Predict Price'):

    query = np.array([Planet_Gears, Input_Shaft, Output_Shaft, Housing, Ring_Gear, Sun_Gear, Carrier, Bearings, Seals])
    query = query.reshape(1,9)

    predicted_price = int(Lin.predict(query)[0]) * 500
    st.title("Predicted Price : ₹ " + str(predicted_price))
    