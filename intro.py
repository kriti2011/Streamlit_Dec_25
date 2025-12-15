import streamlit as st

st.title("Welcome to the Streamlit App!")
st.subheader("Getting Started with Streamlit")
st.write("My first Streamlit app is up and running.")

agree=st.checkbox("I agree to the terms and conditions.")
if agree:
    st.write("Thank you for agreeing!")

genre=st.radio("Select your favorite genre:", 
                ["Comedy","Drama","Documentary"])
if genre=="Comedy":
    st.write("Hahaha! You selected Comedy.")
elif genre=="Drama":
    st.write("Oh no! Drama it is.")
else:
    st.write("Documentaries are so informative!")

