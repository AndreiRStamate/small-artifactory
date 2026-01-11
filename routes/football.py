import logging
import os
from flask import request
from config import get_upload_folder
from utils.custom_blueprint import SecureBlueprint
from utils.file_utils import allowed_file, handle_file_upload, serve_file, list_files, delete_all_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

football_bp = SecureBlueprint('football', __name__)
UPLOAD_FOLDER = get_upload_folder('football')

@football_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return {"error": "Invalid file type"}, 400
    return handle_file_upload(request, UPLOAD_FOLDER, logger)

@football_bp.route('/<filename>', methods=['GET'])
def serve_file_route(filename):
    return serve_file(filename, UPLOAD_FOLDER)

@football_bp.route('/', methods=['GET'])
def list_files_route():
    return list_files(UPLOAD_FOLDER, 'football')

@football_bp.route('/delete_all', methods=['DELETE'])
def delete_all_files_route():
    try:
        deleted_files = delete_all_files(UPLOAD_FOLDER, logger)
        return {"deleted_files": deleted_files}, 200
    except Exception as e:
        return {"error": str(e)}, 500