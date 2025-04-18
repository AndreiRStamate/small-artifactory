from flask import Flask
from routes.football import football_bp
# from routes.basketball import basketball_bp
# from routes.hockey import hockey_bp

app = Flask(__name__)

app.register_blueprint(football_bp, url_prefix='/football')
# app.register_blueprint(basketball_bp, url_prefix='/basketball')
# app.register_blueprint(hockey_bp, url_prefix='/hockey')

@app.route('/')
def index():
    return "Sports JSON Uploader is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)