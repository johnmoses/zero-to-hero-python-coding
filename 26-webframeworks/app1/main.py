""" 
Flask API
Write a basic Flask API
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """GET /"""
    return jsonify({"message": "Hello World"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001")
