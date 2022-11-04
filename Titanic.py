# This app was adapted from this source: https://github.com/krishnaik06/Dockers/blob/master/app.py
# Streamlit documentation: https://docs.streamlit.io/

# Load Libraries----------------
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

# Import the Model--------------
pickle_in = open("rf.pkl","rb")
rf = pickle.load(pickle_in)


# A function to predict survival------------------------------------------
def predict_survival(Pclass,SibSp,Fare):
    prediction= rf.predict([[Pclass,SibSp,Fare]])
    print(prediction)
    return prediction


# User Interface--------------------------------------------------------
def main():
    st.title("Survival Prediction")
    Pclass = st.text_input("Which Ticket Class","Type Here")
    SibSp = st.text_input("# of Siblings or Spouse","Type Here")
    Fare= st.text_input("What was the fare of the ticket","Type Here")
    result="" 
    if st.button("Predict"):
        result=predict_survival(Pclass,SibSp,Fare)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()