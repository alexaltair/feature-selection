from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from cStringIO import StringIO
import cPickle as pickle
import os, redis
import pandas
from stats import generate_results

app = Flask(__name__)

Bootstrap(app)

# r = redis.from_url(os.environ.get("REDIS_URL"))
r = redis.StrictRedis(host='localhost', port=6379, db=0)

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


    mystring = StringIO()
    pickle.dump(data, mystring)
    mystring.seek(0)
    r.set('mykey', mystring.read())
    mystring.close()

    data = StringIO(r.get('mykey'))
    r.delete('mykey')
    data = pickle.load(data)


    results = generate_results(data)
    return render_template('index.html', **results)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
