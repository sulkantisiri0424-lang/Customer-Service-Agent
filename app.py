from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load intents
INTENTS_FILE = os.path.join("data", "intents.json")

def load_intents():
    if os.path.exists(INTENTS_FILE):
        with open(INTENTS_FILE, "r") as file:
            return json.load(file)
    return {"intents": []}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    intents = load_intents()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_message:
                return jsonify({
                    "response": intent["responses"][0]
                })

    return jsonify({
        "response": "Sorry, I couldn't understand your question. Please try again."
    })

if __name__ == "__main__":
    app.run(debug=True)
