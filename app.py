from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import sqlite3
from database import create_database

app = Flask(__name__)

create_database()

def save_chat(user_message, bot_response):
    conn = sqlite3.connect("customer_service.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)",
        (user_message, bot_response)
    )
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = get_response(user_message)
    save_chat(user_message, bot_response)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
