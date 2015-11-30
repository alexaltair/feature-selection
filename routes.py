from flask import current_app, request, render_template

import pandas
from sklearn import datasets

import redis_conn


# Many more routes defined dynamically in stats.py

@current_app.route('/')
def root():
    return render_template('index.html')

@current_app.route('/results', methods=['GET', 'POST'])
def upload():
    data_file = request.files['file']

    if request.form['header'] == 'True':
        data_frame = pandas.read_csv(data_file)
    else:
        data_frame = pandas.read_csv(data_file, header=None)

    uuid = redis_conn.write_to_redis(data_frame)
    return render_template('results.html', uuid=uuid)

@current_app.route('/sample', methods=['GET', 'POST'])
def sample():
    iris = datasets.load_iris()
    data_frame = pandas.DataFrame(iris.data, columns=iris.feature_names)

    uuid = redis_conn.write_to_redis(data_frame)
    return render_template('results.html', uuid=uuid)
