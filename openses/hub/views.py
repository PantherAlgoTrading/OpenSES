from typing import Dict, Tuple, List

from flask import request
from flask.json import jsonify
from flask.views import MethodView


def error_response(
    error: str, error_description: str, status_code: int = 400
) -> Tuple[Dict[str, str], int]:
    """Returns a standardized json error response back to the user with status code"""
    return jsonify(error=error, error_description=error_description), status_code


# TODO: Renable once app is established
# @app.errorhandler(404)
def not_found(e) -> Tuple[Dict[str, str], int]:
    return error_response(
        error="not_found", error_description="Not Found.", status_code=404
    )


# @app.errorhandler(405)
def method_not_allowed(e) -> Tuple[Dict[str, str], int]:
    return error_response(
        error="method_not_allowed",
        error_description="Method not allowed.",
        status_code=405,
    )


def register_api():
    pass