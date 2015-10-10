import os
from flask import Flask, render_template, request

from flask_bootstrap import Bootstrap
from flask.ext import uploads

from sklearn import datasets

app = Flask(__name__)
app.config['DEBUG'] = True

Bootstrap(app)

@app.route('/')
def hello():
    iris = datasets.load_iris().data
    return render_template('index.html', data=iris)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data = request.files['file'].read()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
