import json
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Train TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X, tags)

# Save model
joblib.dump(model, "chatbot_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Training completed successfully!")