import logging
import os
from flask import request
from config import get_upload_folder
from utils.custom_blueprint import OpenBlueprint
from utils.file_utils import allowed_file, handle_file_upload, serve_file, list_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tips_bp = OpenBlueprint('tips', __name__)
UPLOAD_FOLDER = get_upload_folder('tips')

@tips_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return {"error": "Invalid file type"}, 400
    return handle_file_upload(request, UPLOAD_FOLDER, logger)

@tips_bp.route('/<filename>', methods=['GET'])
def serve_file_route(filename):
    return serve_file(filename, UPLOAD_FOLDER)

@tips_bp.route('/', methods=['GET'])
def list_files_route():
    return list_files(UPLOAD_FOLDER, 'tips')