from flask import Flask, url_for
from routes.football import football_bp
from routes.basketball import basketball_bp
from routes.hockey import hockey_bp
from routes.cricket import cricket_bp

app = Flask(__name__)

app.register_blueprint(football_bp, url_prefix='/football')
app.register_blueprint(basketball_bp, url_prefix='/basketball')
app.register_blueprint(hockey_bp, url_prefix='/hockey')
app.register_blueprint(cricket_bp, url_prefix='/cricket')

@app.route('/')
def index():
    return """
    <h1>Sports JSON Uploader</h1>
    <ul>
        <li><a href="{football}">Football</a></li>
        <li><a href="{basketball}">Basketball</a></li>
        <li><a href="{hockey}">Hockey</a></li>
        <li><a href="{cricket}">Cricket</a></li>
    </ul>
    """.format(
        football=url_for('football.list_files_route', _external=True),
        basketball=url_for('basketball.list_files_route', _external=True),
        hockey=url_for('hockey.list_files_route', _external=True),
        cricket=url_for('cricket.list_files_route', _external=True)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)