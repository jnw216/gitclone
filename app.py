import os 

from flask import Flask
from flask import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABSE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)


@app.route('/')
def index():
    # PRINT ALL COMMITS
    #dburi = os.environ['DATABSE_URL']
    #db2 = SQLALCHEMY_DATABSE_URI
    return "GitClone!         adding SQLAlchemy to import           <br>" #+ dburi + "<br>" + db2

@app.route('/push')
def push():
    return "pushing file"

@app.route('/pull')
def pull():
    return "pulling file"

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
