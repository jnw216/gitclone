from flask import render_template



@app.route('/')
def index():
    # PRINT ALL COMMITS  By DEFAULT?
    return "GitClone! work in progress   <br>" 

@app.route('/push')
def push():
    return "pushing file"

@app.route('/pull')
def pull():
    return "pulling file"
