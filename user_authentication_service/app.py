#!/usr/bin/env python3
"""
Basic Flask app module
"""
from typing import Optional, cast
from flask import Flask, jsonify, abort, redirect, request
from flask.typing import ResponseReturnValue
from auth import Auth
from user import User

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


@app.route("/sessions", methods=["DELETE"])
def logout() -> ResponseReturnValue:
    """ DELETE /sessions
    Deletes session for user in database (logout)
    """
    session_id: str = request.cookies.get("session_id") or ""
    user: User = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    user_id: int = cast(int, user.id)
    AUTH.destroy_session(user_id)

    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile() -> ResponseReturnValue:
    """ GET /profile
    Gets profile (email) for session
    """
    session_id: str = request.cookies.get("session_id") or ""
    user: User = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> ResponseReturnValue:
    """ POST /reset_password
    Gets reset token for user (email)
    """
    email: str = request.form.get("email") or ""
    try:
        reset_token: str = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        }), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"])
def update_password() -> ResponseReturnValue:
    """ PUT /reset_password
    Updates password for user
    """
    email: str = request.form.get("email") or ""
    reset_token: str = request.form.get("reset_token") or ""
    new_password: str = request.form.get("new_password") or ""
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({
            "email": email,
            "message": "Password updated"
        })
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
