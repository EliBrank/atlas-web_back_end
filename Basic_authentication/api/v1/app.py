#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from typing import Union


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth_type: str = os.getenv("AUTH_TYPE", "auth")
auth = None
if auth_type == "basic_auth":
    from api.v1.auth.auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

EXCLUDED_PATHS: list = ["/api/v1/status/",
                        "/api/v1/unauthorized/",
                        "/api/v1/forbidden/"]


@app.errorhandler(404)
def not_found(error) -> Union[str, tuple]:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> Union[str, tuple]:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> Union[str, tuple]:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def check_request():
    """ Prevent invalid requests from passing
    """
    if not auth or not auth.require_auth(request.path, EXCLUDED_PATHS):
        return
    if not auth.authorization_header(request):
        abort(401)
    if not auth.current_user(request):
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)  # pyright: ignore
