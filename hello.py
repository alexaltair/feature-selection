from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import numpy
import pandas
from sklearn import datasets
from stats import middle, variance, pca
from utils import head

app = Flask(__name__)
app.config['DEBUG'] = True

Bootstrap(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def upload():
    data_file = request.files['file']
    data = pandas.read_csv(data_file)

    results = {}
    head(data, results)
    middle(data, results)
    variance(data, results)
    pca(data, results)
    return render_template('index.html', **results)

if __name__ == "__main__":
    app.run()
