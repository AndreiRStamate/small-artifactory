import os
from flask import request, abort

API_KEY = os.getenv("API_KEY", "your-secure-api-key")

def require_api_key():
    """Validate the API key from the request headers."""
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        abort(403)  # Forbidden