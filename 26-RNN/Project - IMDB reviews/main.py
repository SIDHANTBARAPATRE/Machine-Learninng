# Step 1: Import Libraries and Load the Model
import re
import numpy as np
import tensorflow as tf
import streamlit as st
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import SimpleRNN

# Patch for the Keras version mismatch (.h5 saved with older Keras)
class PatchedSimpleRNN(SimpleRNN):
    def __init__(self, *args, **kwargs):
        kwargs.pop('time_major', None)
        super().__init__(*args, **kwargs)

# Load the IMDB word index and the model only once, not on every rerun
@st.cache_resource
def load_resources():
    word_index = imdb.get_word_index()
    model = load_model(
        'simple_rnn_imdb.h5',
        custom_objects={'SimpleRNN': PatchedSimpleRNN},
        compile=False
    )
    return word_index, model

word_index, model = load_resources()

# Step 2: Helper Functions
MAX_FEATURES = 10000  # must match the vocab size used when training

def preprocess_text(text):
    words = re.findall(r"[a-z']+", text.lower())  # strips punctuation like "fantastic!"
    encoded_review = []
    for word in words:
        idx = word_index.get(word)
        if idx is None or idx + 3 >= MAX_FEATURES:
            encoded_review.append(2)      # unknown token
        else:
            encoded_review.append(idx + 3)
    return sequence.pad_sequences([encoded_review], maxlen=500)

# Step 3: Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

user_input = st.text_area('Movie Review')

if st.button('Classify'):
    if user_input.strip():
        preprocessed_input = preprocess_text(user_input)
        prediction = model.predict(preprocessed_input)
        score = float(prediction[0][0])
        sentiment = 'Positive' if score > 0.5 else 'Negative'

        st.write(f'Sentiment: {sentiment}')
        st.write(f'Prediction Score: {score:.4f}')
    else:
        st.warning('Please enter a movie review.')