from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def get_balance(user_id):

    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    cursor.execute(
        "SELECT balance FROM users WHERE user_id = ?",
        (user_id,)
    )

    result = cursor.fetchone()

    db.close()

    if result:
        return result[0]

    return 0


@app.get("/balance")
def balance():

    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({
            "balance": 0
        })

    return jsonify({
        "balance": get_balance(user_id)
    })


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )