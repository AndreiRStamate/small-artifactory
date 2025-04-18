import os

BASE_UPLOAD_FOLDER = 'uploads'

def get_upload_folder(sport):
    folder = os.path.join(BASE_UPLOAD_FOLDER, sport)
    os.makedirs(folder, exist_ok=True)
    return folder