import streamlit as st
import joblib
model = joblib.load('spam-ham')
ip = st.text_input('Enter the Message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
                          
