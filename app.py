from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

with app.app_context():
   import routes
   import stats

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()
