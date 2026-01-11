import os
from flask import jsonify, send_from_directory, render_template

ALLOWED_EXTENSIONS = {'json'}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_file_upload(request, upload_folder, logger):
    if 'file' not in request.files:
        logger.error("No file part in request")
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    if file.filename == '':
        logger.error("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        save_path = os.path.join(upload_folder, file.filename)
        file.save(save_path)
        logger.info(f"File {file.filename} uploaded successfully")
        return jsonify({'message': f'{file.filename} uploaded successfully'}), 200

    logger.error("Invalid file type")
    return jsonify({'error': 'Only .json files are allowed'}), 400

def serve_file(filename, upload_folder):
    if not allowed_file(filename):
        return jsonify({'error': 'Only .json files can be downloaded'}), 400
    try:
        return send_from_directory(upload_folder, filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

def list_files(upload_folder, sport):
    files = os.listdir(upload_folder)
    files = [f for f in files if allowed_file(f)]
    return render_template('list_files.html', sport=sport, files=files)

def delete_all_files(upload_folder, logger):
    """
    Deletes all files in the given upload_folder.
    Returns a list of deleted filenames.
    """
    try:
        files = os.listdir(upload_folder)
        deleted_files = []
        for filename in files:
            file_path = os.path.join(upload_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_files.append(filename)
        logger.info(f"Deleted files: {deleted_files}")
        return deleted_files
    except Exception as e:
        logger.error(f"Error deleting files: {e}")
        raise