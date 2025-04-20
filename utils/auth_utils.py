import os
from dotenv import load_dotenv
from flask import request, abort

load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")

def require_api_key():
    """Validate the API key from the request headers."""
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        abort(403)  # Forbidden
