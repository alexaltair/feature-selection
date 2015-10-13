from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import numpy
import pandas
from sklearn import datasets
from stats import middle, variance, pca, mean_shift, dbscan
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
    if request.values['header'] == 'True':
        data = pandas.read_csv(data_file)
    else:
        data = pandas.read_csv(data_file, header=None)


    results = {}
    head(data, results)
    middle(data, results)
    variance(data, results)
    try:
        pca(data, results)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass
    try:
        mean_shift(data, results)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass
    try:
        dbscan(data, results)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass

    return render_template('index.html', **results)

if __name__ == "__main__":
    app.run()
