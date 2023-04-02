from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return '<a href="/pong">pong</a>'


@app.route('/pong')
def pong():
    return '<a href="/ping">ping</a>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
