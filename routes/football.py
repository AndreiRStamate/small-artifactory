import logging
import os
from flask import Blueprint, request, jsonify, send_from_directory, render_template
from config import get_upload_folder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

football_bp = Blueprint('football', __name__)
UPLOAD_FOLDER = get_upload_folder('football')

@football_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.error("No file part in request")
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    if file.filename == '':
        logger.error("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.json'):
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        logger.info(f"File {file.filename} uploaded successfully")
        return jsonify({'message': f'{file.filename} uploaded successfully'}), 200

    logger.error("Invalid file type")
    return jsonify({'error': 'Only .json files are allowed'}), 400

@football_bp.route('/<filename>', methods=['GET'])
def serve_file(filename):
    if not filename.endswith('.json'):
        return jsonify({'error': 'Only .json files can be downloaded'}), 400
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

@football_bp.route('/', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    files = [f for f in files if f.endswith('.json')]
    return render_template('list_files.html', sport='football', files=files)