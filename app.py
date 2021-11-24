from flask import Flask, render_template
from flask.templating import render_template
import requests

app = Flask(__name__)

# main application route
@app.route("/")
def login():
    return render_template('authenticate.html')

@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)