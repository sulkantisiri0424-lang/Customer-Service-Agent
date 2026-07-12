import json
import random
import joblib
import os

MODEL_FILE = "chatbot_model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"

with open("intents.json", "r") as file:
    intents = json.load(file)

model = None
vectorizer = None

if os.path.exists(MODEL_FILE) and os.path.exists(VECTORIZER_FILE):
    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)


def get_response(message):
    message = message.lower()

    if model and vectorizer:
        prediction = model.predict(vectorizer.transform([message]))[0]

        for intent in intents["intents"]:
            if intent["tag"] == prediction:
                return random.choice(intent["responses"])

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in message:
                return random.choice(intent["responses"])

    return "Sorry, I couldn't understand your question."