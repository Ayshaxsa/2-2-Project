import streamlit as st
from transformers import pipeline

# Load sentiment analysis model (cached for faster performance)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# App title
st.set_page_config(page_title="Quick Sentiment Analyzer", page_icon="💬")
st.title("💬 Quick Sentiment Analysis App")
st.write("Type some text below and see if it's positive, negative, or neutral!")

# User input
user_input = st.text_area("Enter text here:")

# Analyze button
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        result = model(user_input)[0]
        sentiment = result['label']
        score = round(result['score'], 3)

        # Show emoji + result
        emoji = "😊" if sentiment == "POSITIVE" else "😟"
        st.success(f"{emoji} Sentiment: **{sentiment}** (Confidence: {score})")
