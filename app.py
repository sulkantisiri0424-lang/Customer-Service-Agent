
from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import create_database
import sqlite3

app = Flask(__name__)

create_database()

DB_NAME = "customer_service.db"


def save_chat(user_message, bot_response):
    conn = sqlite3.connect(DB_NAME)
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
    data = request.get_json()
    user_message = data.get("message", "")

    bot_response = get_response(user_message)

    save_chat(user_message, bot_response)

    return jsonify({
        "response": bot_response
    })


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/history")
def history():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_message, bot_response FROM chat_history ORDER BY id DESC"
    )

    chats = cursor.fetchall()

    conn.close()

    return render_template("history.html", chats=chats)


@app.route("/analytics")
def analytics():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM chat_history")
    total_chats = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_chats": total_chats,
        "total_feedback": total_feedback
    })


if __name__ == "__main__":
    app.run(debug=True)