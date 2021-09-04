import os
from flask import Flask,  send_from_directory, request
from model.generate_text import TextGenerator

STATIC_PATH = os.path.join("web", "build")
SENTENCE_LENGTH = 7

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret key'

@app.route("/")
@app.route("/chat")
def index():
    return send_from_directory(STATIC_PATH, "index.html")

@app.route("/api/talk", methods=['GET', 'POST'])
def get_gibberish():
    input_phrase = request.get_data() if request.method == "POST" else ""

    if input_phrase:
        return TextGenerator().continue_to_say_something(input_phrase.decode())
    else:
        return TextGenerator().say_something()


@app.route("/<path:name>")
def download_file(name):
    return send_from_directory(
        os.path.join("web", "build"), name
    )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


