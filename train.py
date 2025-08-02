# train.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
from utils.preprocessing import clean_text

# Load datasets
df_fake = pd.read_csv("data/Fake.csv")
df_fake['label'] = 0

df_real = pd.read_csv("data/True.csv")
df_real['label'] = 1

# Combine
df = pd.concat([df_fake, df_real]).reset_index(drop=True)
df['cleaned_text'] = df['text'].apply(clean_text)

# Features and labels
X_text = df['cleaned_text']
y = df['label']

# Vectorize
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(X_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open("models/fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)
