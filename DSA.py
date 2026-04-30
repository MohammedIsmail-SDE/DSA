import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my web site!'

if __name__ == '__main__':
    app.run(debug=True)