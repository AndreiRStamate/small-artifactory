import logging
import os
from flask import request
from config import get_upload_folder
from utils.custom_blueprint import SecureBlueprint
from utils.file_utils import allowed_file, handle_file_upload, serve_file, list_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

hockey_bp = SecureBlueprint('hockey', __name__)
UPLOAD_FOLDER = get_upload_folder('hockey')

@hockey_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return {"error": "Invalid file type"}, 400
    return handle_file_upload(request, UPLOAD_FOLDER, logger)

@hockey_bp.route('/<filename>', methods=['GET'])
def serve_file_route(filename):
    return serve_file(filename, UPLOAD_FOLDER)

@hockey_bp.route('/', methods=['GET'])
def list_files_route():
    return list_files(UPLOAD_FOLDER, 'hockey')