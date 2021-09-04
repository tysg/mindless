from flask import Flask, escape, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret key'


@app.route('/')
def hello():
    return "Hello World!"
