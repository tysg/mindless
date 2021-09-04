import os
from flask import Flask,  send_from_directory, request
from model.generate_text import TextGenerator

STATIC_PATH = os.path.join("web", "build")
SENTENCE_LENGTH = 7

app = Flask(__name__, static_folder='web/build/',
            static_url_path="/web/build/")

app.config['SECRET_KEY'] = 'any secret key'


@app.route("/api/talk", methods=['GET', 'POST'])
def get_gibberish():
    input_phrase = request.get_data() if request.method == "POST" else ""

    # run generator
    tg = TextGenerator(3, 0.00001)
    output = tg.generate_text(SENTENCE_LENGTH)

    if input_phrase:
        return "phrase exists"
    else:
        return output


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def index(path):
    return app.send_static_file("index.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
