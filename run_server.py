from flask import Flask
from gitclone import app
app = Flas(__name__)
from views import *

if __name__ == '__main__':
    app.run(debug=True)

#if __name__ == "__main__":
#    port = int(os.environ.get("PORT",5000))
#    app.run(host="0.0.0.0",port=port)