#!/usr/bin/env python3
"""
Basic Flask app module
"""
from flask import Flask, jsonify, abort, request
from flask.typing import ResponseReturnValue

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def welcome_message() -> ResponseReturnValue:
    """Greets the user
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
