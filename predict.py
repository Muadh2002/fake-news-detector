# predict.py

import pickle
from utils.preprocessing import clean_text

# Load model and vectorizer
with open("models/fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_news(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)
    return "Real" if prediction[0] == 1 else "Fake"

# Example usage
if __name__ == "__main__":
    sample = input("Enter news text: ")
    result = predict_news(sample)
    print("Prediction:", result)
