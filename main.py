from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>My site</p>"

@app.route("/test")
def test():
    return "<p>Test</p>"

app.run(debug=True)