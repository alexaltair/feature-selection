from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import numpy
from sklearn import datasets
from stats import middle
from utils import head

app = Flask(__name__)
app.config['DEBUG'] = True

Bootstrap(app)

@app.route('/')
def hello():
    data = datasets.load_iris().data

    results = {}
    results['preview'] = head(data)
    results = middle(data, results)
    return render_template('index.html', **results)

@app.route('/results', methods=['GET', 'POST'])
def upload():
    data = numpy.loadtxt(request.files['file'], delimiter=",", skiprows=1)

    results = {}
    results['preview'] = head(data)
    results = middle(data, results)
    return render_template('index.html', **results)

if __name__ == "__main__":
    app.run()
