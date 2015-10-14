from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pandas
from stats import generate_results

app = Flask(__name__)

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

    results = generate_results(data)

    return render_template('index.html', **results)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
