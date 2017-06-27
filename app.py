

app = Flask(__name__)




@app.route('/')
def index():
    # PRINT ALL COMMITS  
    return "GitClone! work in progress   <br>" 



@app.route('/push')
def push():
    return "pushing file"

@app.route('/pull')
def pull():
    return "pulling file"

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)
