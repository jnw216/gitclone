from flask import render_template



@app.route('/')
def index():
    # PRINT ALL COMMITS  By DEFAULT?
    return "GitClone! work in progress   <br>" 

@app.route('/push')
def push():
    # write new "string" to database entry
    return "pushing file"

@app.route('/pull')
def pull():
    #get latest "string" from database
    return "pulling file"
