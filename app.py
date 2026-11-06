import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load saved files
model = load_model("next_word_model.keras")

with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

with open("max_len.pkl", "rb") as file:
    max_len = pickle.load(file)


# Prediction function
def predict_next_word(text):

    token_list = tokenizer.texts_to_sequences([text])[0]

    token_list = pad_sequences(
        [token_list],
        maxlen=max_len - 1,
        padding='post'
    )

    predicted = model.predict(token_list, verbose=0)

    predicted_word_index = np.argmax(predicted)

    return tokenizer.index_word.get(predicted_word_index, "Unknown")


# Streamlit interface
st.title("English Next Word Predictor")

text = st.text_input("Enter a sentence:")

if st.button("Predict Next Word"):
    if text.strip():
        result = predict_next_word(text)
        st.success(f"Next word: {result}")
    else:
        st.warning("Please enter a sentence.")