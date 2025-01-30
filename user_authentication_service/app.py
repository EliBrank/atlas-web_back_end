#!/usr/bin/env python3
"""
Basic Flask app module
"""
from typing import Optional
from flask import Flask, jsonify, abort, request
from flask.typing import ResponseReturnValue
from auth import Auth

AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def welcome_message() -> ResponseReturnValue:
    """ GET /
    Greets the user
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> ResponseReturnValue:
    """ POST /users
    Creates user if not already in database
    """
    email: str = str(request.form.get("email"))
    password: str = str(request.form.get("password"))

    try:
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login() -> ResponseReturnValue:
    """ POST /sessions
    Creates session for user in database (login)
    """
    email: str = request.form.get("email") or ""
    password: str = request.form.get("password") or ""

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id: str = AUTH.create_session(email)
    response: ResponseReturnValue = jsonify({
        "email": email,
        "message": "logged in"
    })
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
