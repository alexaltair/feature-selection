# Feature Selection
A web app providing one-click analysis on a CSV.

Available on Heroku at https://pure-reaches-1719.herokuapp.com.

Upload a CSV to get statistical and machine learning analysis. The data is assumed to be numerical. The rows of the CSV are the data points, and the columns are the features. Row header optional; column header not supported.

Uses [numpy](https://github.com/numpy/numpy), [pandas](https://github.com/pydata/pandas) and [scikit-learn](https://github.com/scikit-learn/scikit-learn) on the backend

# Running the app

Create a virtual env if you prefer.

Install the requirements with `pip install -r requirements.txt`.

Run `python routes.py`. The app should be served at `http://localhost:5000/`.
