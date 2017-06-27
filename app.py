from flask import flask
app = Flask(__name__)

@app.rout("/")
def hello:
    return "Hello World!"


if __name__ == '__main__':
    app.run()