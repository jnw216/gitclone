from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
#migrate = Migrate(app,db)



@app.route('/')
def index():
    # PRINT ALL COMMITS  
    return "GitClone! Work In Progress   <br>" 



@app.route('/push', methods=["POST"])
def push():
    return "pushing file"

@app.route('/pull')
def pull():
    return "pulling file"

'''
@app.route('/dbtest')
def dbtest():
    return os.environ['DATABASE_url']
'''


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)