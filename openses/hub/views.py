from typing import Dict, Tuple, List

from flask import Flask
from flask.json import jsonify
from flask.views import MethodView


def error_response(
    error: str, error_description: str, status_code: int = 400
) -> Tuple[Dict[str, str], int]:
    """Returns a standardized json error response back to the user with status code"""
    return jsonify(error=error, error_description=error_description), status_code


def not_found(e) -> Tuple[Dict[str, str], int]:
    return error_response(
        error="not_found", error_description="Not Found.", status_code=404
    )


def method_not_allowed(e) -> Tuple[Dict[str, str], int]:
    return error_response(
        error="method_not_allowed",
        error_description="Method not allowed.",
        status_code=405,
    )


class MarketDataFetchAPI(MethodView):
    def get(self) -> Dict:
        return jsonify({})


def add_views_to_app(app: Flask) -> None:
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    app.add_url_rule("/data", view_func=MarketDataFetchAPI.as_view("market_data_fetch"))
