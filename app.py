import os
from flask import Flask,  send_from_directory

STATIC_PATH = os.path.join("web", "build")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret key'


@app.route("/")
def index():
    return send_from_directory(STATIC_PATH, "index.html")


@app.route("/<path:name>")
def download_file(name):
    return send_from_directory(
        os.path.join("web", "build"), name
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT")) if os.getenv("PORT") else 5000
    app.run(host='127.0.0.1', port=port)

