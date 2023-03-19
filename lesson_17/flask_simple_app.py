from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')
    return f'<p>Hello, {name}!</p>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
