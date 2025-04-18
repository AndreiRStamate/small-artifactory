import logging
import os
from flask import Blueprint, request
from config import get_upload_folder
from utils.file_utils import handle_file_upload, serve_file, list_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

football_bp = Blueprint('football', __name__)
UPLOAD_FOLDER = get_upload_folder('football')

@football_bp.route('/upload', methods=['POST'])
def upload_file():
    return handle_file_upload(request, UPLOAD_FOLDER, logger)

@football_bp.route('/<filename>', methods=['GET'])
def serve_file_route(filename):
    return serve_file(filename, UPLOAD_FOLDER)

@football_bp.route('/', methods=['GET'])
def list_files_route():
    return list_files(UPLOAD_FOLDER, 'football')