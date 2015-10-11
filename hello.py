from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from sklearn import datasets

app = Flask(__name__)
app.config['DEBUG'] = True

Bootstrap(app)

@app.route('/')
def hello():
    data = datasets.load_iris().data
    return render_template('index.html', data=data)

@app.route('/results', methods=['GET', 'POST'])
def upload():
    csv = request.files['file'].read()
    return render_template('index.html', data=csv)

if __name__ == "__main__":
    app.run()
