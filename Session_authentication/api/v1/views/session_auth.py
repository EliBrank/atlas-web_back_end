#!/usr/bin/env python3
""" Module of Session Auth views
"""
import os
from typing import Optional

from flask.typing import ResponseReturnValue
from api.v1.views import app_views
from flask import Response, abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'])
def user_login() -> ResponseReturnValue:
    """ POST /api/v1/auth_session/login/
    JSON body:
        email
        password
    Return:
        User object as JSON,
        400 if no email or password,
        401 if wrong password,
        404 if matching user not in db
    """
    email: Optional[str] = request.form.get("email")
    password: Optional[str] = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users: list[User] = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id: str = auth.create_session(user.id)  # type: ignore
            response: Response = jsonify(user.to_json())
            response.set_cookie(str(os.getenv("SESSION_NAME")), session_id)
            return response

    # no user in users matched password
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'])
def user_logout() -> ResponseReturnValue:
    """ DELETE /api/v1/auth/session_auth
    Return:
        Empty JSON and code 200 if session correctly deleted,
        404 if the User ID doesn't exist
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):  # type: ignore
        abort(404)
    return jsonify({}), 200
