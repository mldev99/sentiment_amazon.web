import streamlit as st
import pandas as pd

name = st.text_input("Enter your name: ")
fname = st.text_input("enter your father name: ")
adt = st.text_area("enter your text: ")
classdata = st.selectbox("enter your flask: ", (1, 2, 3, 4, 5, 6))

button = st.button("Done")
if button :
    st.markdown(f"""
                Name : {name}
                Father Name : {fname}
                address : {adt}
                class : {classdata}
                """)
