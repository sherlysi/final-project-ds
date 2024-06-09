import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import re

# Attribute information for the ML section
attribute_info = """
                 - Text: The news text to be tested
                 """

# Helper function to load pickle files
def load_pickle(pickle_file):
    with open(pickle_file, 'rb') as file:
        loaded_pickle = joblib.load(file)
    return loaded_pickle

# Function to remove punctuation from text
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Function to run the ML app
def run_ml_app():
    st.subheader("Prediction")
    with st.expander("Attribute Info"):
        st.markdown(attribute_info)

    st.subheader("Input Your Data")
    text_input = st.text_area("News Text", "Enter the news text here")

    if st.button("Predict"):
        with st.expander("Your Input"):
            st.write(text_input)

        # Clean the input text
        cleaned_text = remove_punctuation(text_input)
        
        # Load the models
        model = load_pickle('MEMBARA_ANTI_HOAX.pkl')
        vectorizer = load_pickle('PENG_VECTOR_TEXT.pkl')

        # Transform the text input
        text_vectorized = vectorizer.transform([cleaned_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)

        # Encode the result
        result = "Real News" if prediction[0] == 1 else "Fake News"

        st.subheader('Prediction Result')
        if result == "Fake News":
            st.warning('The text is Fake News')
        else:
            st.success('The text is Real News')

    # Display image at the bottom of the ML section
    try:
        st.image("News_Image.png", width=200)
    except FileNotFoundError:
        st.error("Image not found. Please make sure 'News_image.png' is available.")

if __name__ == '__main__':
    run_ml_app()
