# 📰 Fake News Detection System

This is a simple yet powerful Fake News Detection system built with Python, Natural Language Processing (NLP), and Machine Learning using the **scikit-learn** library. It classifies news articles as **Real** or **Fake** based on their content. An optional Streamlit web app is included for an interactive experience.

---

## 📌 Features

- Clean and preprocess news text using NLP
- Train a Logistic Regression model using TF-IDF vectorization
- Detect fake or real news articles with high accuracy
- Simple web interface built using **Streamlit**
- Modular structure for training and prediction

---

## 🛠️ Tech Stack

- **Language**: Python  
- **ML/NLP**: scikit-learn, nltk  
- **Frontend (UI)**: Streamlit  
- **Data**: [Kaggle Fake & Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector


python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python train.py
python predict.py
streamlit run app.py
