import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from sklearn import linear_model
import pickle
import warnings
warnings.filterwarnings('ignore')

#data = pd.read_csv("C:\\Users\\himan\\Desktop\\DS-ML\\CarPrice_Assignment.csv")

st.title("Car Price Prediction")
st.markdown('**Objective** : Given details about the car features we try to predict the price of car.')



# Add the form elements to the left column
with st.form("template_form"):
    # Create a column layout
    left, right = st.columns(2)

    with left:
    
        carlength = st.number_input("Car Length", min_value= 145, max_value=210, value= 175)
        carwidth = st.number_input("Car Width", min_value= 64, max_value=67, value= 65)
        carheight = st.number_input("Car Height", min_value= 52, max_value=56, value= 54)
        curbweight = st.number_input("Curb weight", min_value= 1000, max_value=5000, value= 3000)
        highwaympg = st.number_input("Highway MPG", min_value= 16, max_value=54, value= 30)
        enginesize = st.number_input("Engine size", min_value=1000, max_value=3000, value= 2000)
        boreratio = st.number_input("Bore ratio", min_value= 0.3, max_value=0.8, value= 0.5)
        stroke = st.number_input("Stroke", min_value= 2.5, max_value=5.0, value= 3.5)
        compressionratio = st.number_input("Compression ratio", min_value= 8, max_value=12, value= 10)
        horsepower = st.number_input("Horsepower", min_value= 50, max_value=300, value= 150)
        
    
    

# Add the form elements to the right column
    with right:
        peakrpm = st.number_input("Peak RPM", min_value= 5000, max_value=8000, value= 6000)
        wheelbase = st.number_input("Wheelbase", min_value= 87, max_value=115, value= 100)
        brand = st.selectbox("Brand", ("BMW","Buick","Jaguar","Porsche"))
        carbody = st.selectbox("Car body", ("convertible","hatchback","hardtop","sedan","wagon"), index=0)
        cylindernumber = st.selectbox("Number of cylinders", (2,3,4,5,6,8,12), index=0)
        symboling = st.selectbox("Symboling", (-3,-2,-1,0,1,2,3,))
        aspiration = st.radio("Aspiration", ("std","turbo"), index=0, horizontal=True)
        fueltype = st.radio("Fuel type",("gas","diesel") , index=0, horizontal=True)
        enginelocation = st.radio("Engine location",("front","rear") , index=0, horizontal=True)
        doornumber = st.radio("Number of doors", (2,4), index=0, horizontal=True)
        drivewheel = st.radio("Drive wheel", ("fwd","rwd"), index=0, horizontal=True)
        
        
    
    
    
    

# Create a form

    # Add the form elements to the form
    submit = st.form_submit_button()

if submit:
    hptype_medium = 0
    drivewheel_fwd = 0

    Brand_bmw = 0
    Brand_buick = 0
    Brand_jaguar = 0
    Brand_porsche = 0

    if horsepower < 116 and horsepower > 70:
        hptype_medium = 1
    if drivewheel == "fwd":
        drivewheel_fwd = 1
    if brand == "bmw":
        Brand_bmw = 1
    if brand == "buick":
        Brand_buick = 1
    if brand == "jaguar":
        Brand_jaguar = 1
    if brand == "porsche":
        Brand_porsche = 1
    
    carwidth = (65-carwidth)/2
    cylindernumber = (5-cylindernumber)/3
    highwaympg = (30-highwaympg)/6
    
    arr = pd.DataFrame([[carwidth,cylindernumber,highwaympg,hptype_medium,drivewheel_fwd,Brand_bmw,
                        Brand_buick,Brand_jaguar,Brand_porsche]])
    x_test = sm.add_constant(arr,has_constant='add')
    with open('linear_model.sav', 'rb') as f:
        model = pickle.load(f)
    
    
    preds = model.predict([x_test])[0][0]
    result = round(preds,2)

    st.header(f"Predicted car price in USD: {result}")
    
    
