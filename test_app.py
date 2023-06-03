import time

import streamlit as st

st.title("Fruit App")

fruits = ["Apple", "Orange", "Mango", "Banana"]
fruits_selection =  st.multiselect("Select your favorite fruits", fruits, [])

if fruits_selection:
    st.markdown("## Your Selection")
    st.write(fruits_selection)

if st.button('Make a smoothie'):
    with st.spinner("coming right up..."):
        time.sleep(2)
        st.write("Tadaaaaa! Here's your" + "+ ".join(fruits_selection) + " smoothie")
