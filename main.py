import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_input_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))

if user_input_animal_type == "Cat":
    pet_color = st.sidebar.text_area("What's the color of your cat?", max_chars=15)

if user_input_animal_type == "Dog":
    pet_color = st.sidebar.text_area("What's the color of your dog?", max_chars=15)

if user_input_animal_type == "Bird":
    pet_color = st.sidebar.text_area("What's the color of your bird?", max_chars=15)

if user_input_animal_type == "Hamster":
    pet_color = st.sidebar.text_area("What's the color of your hamster?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(user_input_animal_type, pet_color)
    st.text(response['pet_name'])