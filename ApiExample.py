import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to Gareth's virtual lesson</h1><p>Sorry I am still ill.</p>"

app.run()
