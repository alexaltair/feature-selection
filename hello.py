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
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def upload():
    data_file = request.files['file']

    # This feels dirty, but I get handed the open file object
    header = numpy.array(data_file.readline().strip())
    # Set the file reading position to zero so the numpy loading works as expected.
    data_file.seek(0)

    data = numpy.genfromtxt(data_file, dtype=float, skip_header=1, delimiter=",")

    results = {}
    results['header'] = header
    results['preview'] = head(data)
    results = middle(data, results)
    return render_template('index.html', **results)

if __name__ == "__main__":
    app.run()
