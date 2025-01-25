#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, Response
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str | Response:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str | Response:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@app_views.route('/unauthorized')
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - 401 abort error
    """
    abort(401)
