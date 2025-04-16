from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)

# Directory to store uploaded JSON files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "JSON Uploader is running"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.json'):
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        return jsonify({'message': f'{file.filename} uploaded successfully'}), 200

    return jsonify({'error': 'Only .json files are allowed'}), 400

@app.route('/files/<filename>', methods=['GET'])
def serve_file(filename):
    if not filename.endswith('.json'):
        return jsonify({'error': 'Only .json files can be downloaded'}), 400
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)