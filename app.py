from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "hi": "Hello! Welcome to Customer Service. How can I help you?",
    "hello": "Hi! How can I assist you today?",
    "order": "Please provide your Order ID.",
    "refund": "I can help with refunds. Please share your Order ID.",
    "payment": "Please tell me your payment issue.",
    "bye": "Thank you for contacting us. Have a nice day!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "").lower()

    reply = "Sorry, I don't understand. Please contact our support team."

    for key in responses:
        if key in message:
            reply = responses[key]
            break

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
