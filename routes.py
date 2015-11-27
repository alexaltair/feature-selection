from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from cStringIO import StringIO
import cPickle as pickle
from uuid import uuid4
import os, redis

import pandas
from stats import generate_results, covariance

app = Flask(__name__)

Bootstrap(app)

if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
else:
    r = redis.from_url(os.environ.get("REDIS_URL"))

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

    data_string = StringIO()
    pickle.dump(data_frame, data_string)
    uuid = str(uuid4())
    data_string.seek(0)
    r.set(uuid, data_string.read())
    data_string.close()

    results = generate_results(data_frame)
    return render_template('results.html', uuid=uuid, **results)


@app.route('/covariance', methods=['GET', 'POST'])
def covariance_route():
    uuid = request.form['data_uuid']
    data_string = StringIO(r.get(uuid))
    r.delete(uuid)
    data_frame = pickle.load(data_string)

    return covariance(data_frame)


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
