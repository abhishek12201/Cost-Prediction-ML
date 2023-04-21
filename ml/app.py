import streamlit as st
import pickle
import numpy as np

# Import the model
Lin = pickle.load(open('Lin.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

# Title
st.title("Gearbox Price Predictor")

# Parameters
Shaft_Diameter = st.selectbox('Shaft_Diameter',df['Shaft_Diameter'].unique())
Rated_torque = st.selectbox('Rated_torque',df['Rated_torque'].unique())
Max_Torque_Rating = st.selectbox('Max_Torque_Rating',df['Max_Torque_Rating'].unique())
Thermal_Rating = st.selectbox('Thermal_Rating',df['Thermal_Rating'].unique())
Stages = st.selectbox('Stages',df['Stages'].unique())
Acutal_Ratio = st.selectbox('Acutal_Ratio',df['Acutal_Ratio'].unique())
Max_Input_Power = st.selectbox('Max_Input_Power',df['Max_Input_Power'].unique())
Actual_Speed_Rpm = st.selectbox('Actual_Speed_Rpm',df['Actual_Speed_Rpm'].unique())


if st.button('Predict Price'):

    query = np.array([Shaft_Diameter, Rated_torque, Max_Torque_Rating, Thermal_Rating, Stages, Acutal_Ratio, Max_Input_Power, Actual_Speed_Rpm])
    query = query.reshape(1,8)

    st.title("Predicted Price : ₹ " + str(int(Lin.predict(query)[0])))