from flask import Flask
from gitclone import app

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

#if __name__ == "__main__":
#    port = int(os.environ.get("PORT",5000))
#    app.run(host="0.0.0.0",port=port)
