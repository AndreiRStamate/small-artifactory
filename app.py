from flask import Flask, request, send_from_directory, jsonify
from flask import render_template_string
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

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    files = [f for f in files if f.endswith('.json')]

    html_template = """
    <!doctype html>
    <html>
    <head><title>Available JSON Files</title></head>
    <body>
        <h2>📦 Available JSON Files</h2>
        <ul>
        {% for file in files %}
            <li><a href="/files/{{ file }}">{{ file }}</a></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html_template, files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)