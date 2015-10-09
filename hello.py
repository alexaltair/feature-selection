import os
from flask import Flask

from sklearn import datasets

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return str(datasets.load_iris().data)

if __name__ == "__main__":
    app.run()
