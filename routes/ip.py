import logging
import os
from flask import request
from config import get_upload_folder
from utils.custom_blueprint import SecureBlueprint
from utils.file_utils import allowed_file, handle_file_upload, serve_file, list_files
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ip_bp = SecureBlueprint('ip', __name__)

@ip_bp.route('/', methods=['GET'])
def list_files_route():
    try:
        response = requests.get("https://api.ipify.org?format=text", timeout=5)
        response.raise_for_status()
        print(f"Your public IP address is: {response.text}")
    except requests.RequestException as e:
        print(f"Error retrieving public IP: {e}")
    return response.text