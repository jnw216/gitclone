import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

#from models import commits

#migrate = Migrate(app,db)

@app.route('/')
def index():
    # PRINT ALL COMMITS  
    return "GitClone! Work In Progress app.config  <br>" 

@app.route('/push', methods=["POST"])
def push():
    '''
    for each file write it to database as string    
    '''
    return "pushing file"

@app.route('/pull')
def pull():
    return "pulling file"

@app.route('/dbtest')
def dbtest():
    #m = os.environ['DATABASE_url']
    m = os.path.abspath(os.path.dirname(__file__))
    m = m + " "  
    return m



if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)