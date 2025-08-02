# app.py

import streamlit as st
from predict import predict_news

st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detection System")
st.markdown("Enter a news article or paragraph to check if it's **Real** or **Fake**.")

user_input = st.text_area("Paste News Article Text Here:")

if st.button("Check Now"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = predict_news(user_input)
        st.success(f"🧠 This news is predicted to be: **{result}**")
