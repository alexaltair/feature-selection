from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import pandas
from sklearn import datasets
import stats
from stats import generate_results

import redis_conn

app = Flask(__name__)

Bootstrap(app)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def upload():
    data_file = request.files['file']

    if request.form['header'] == 'True':
        data_frame = pandas.read_csv(data_file)
    else:
        data_frame = pandas.read_csv(data_file, header=None)

    uuid = redis_conn.write_to_redis(data_frame)
    results = generate_results(data_frame)
    return render_template('results.html', uuid=uuid, **results)

@app.route('/sample', methods=['GET', 'POST'])
def sample():
    iris = datasets.load_iris()
    data_frame = pandas.DataFrame(iris.data, columns=iris.feature_names)

    uuid = redis_conn.write_to_redis(data_frame)
    results = generate_results(data_frame)
    return render_template('results.html', uuid=uuid, **results)


def return_route_function(result):
    def route_function():
        uuid = request.form['data_uuid']
        data_frame = redis_conn.read_from_redis(uuid)
        return getattr(stats, result)(data_frame)
    route_function.__name__ = result + '_route'
    return route_function

for result in ['covariance', 'sorted_variance']:
    app.add_url_rule(
        '/' + result,
        view_func=return_route_function(result),
        methods=['GET', 'POST'])


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
