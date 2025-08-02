import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
from utils.preprocessing import clean_text
import os

# Load first 1000 rows from each CSV and treat all text columns as strings
df_fake = pd.read_csv("data/Fake.csv", usecols=["title", "text"], dtype=str).head(50)
df_fake['label'] = 0

df_real = pd.read_csv("data/True.csv", usecols=["title", "text"], dtype=str).head(50)
df_real['label'] = 1

# Combine fake and real news
df = pd.concat([df_fake, df_real]).reset_index(drop=True)

# Clean the 'text' column using custom preprocessing
df['cleaned_text'] = df['text'].fillna("").apply(clean_text)

# Split features and target
X_text = df['cleaned_text']
y = df['label']

# TF-IDF vectorization
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(X_text)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("\n=== Model Evaluation ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
os.makedirs("models", exist_ok=True)
with open("models/fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("\n✅ Model and TF-IDF vectorizer saved to 'models/' directory.")
