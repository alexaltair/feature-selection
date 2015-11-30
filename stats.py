import json

from pandas import Series, DataFrame
from sklearn.decomposition import PCA
from sklearn.cluster import MeanShift, DBSCAN

from results_routes import result_route

@result_route
def preview(data, n=10):
    return data.iloc[:n].to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

@result_route
def mean(data):
    return data.mean().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

@result_route
def median(data):
    return data.median().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

@result_route
def variance(data):
    return data.var().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

@result_route
def sorted_variance(data):
    return data.var().sort_values().to_frame().T.to_html(
        index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

@result_route
def covariance(data):
    return data.cov().to_html(
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

@result_route
def pca(data):
    remaining_variance = PCA().fit(data).explained_variance_ratio_
    index = range(1, len(remaining_variance)+1)
    remaining_variance = DataFrame({
        "Component": index,
        "Explained variance ratio": remaining_variance,
    }, dtype=object).T

    return json.dumps({
        'html': remaining_variance.to_html(header=False,
            classes=['table', 'table-condensed', 'table-bordered']),
        'json': remaining_variance.to_dict()
    })

@result_route
def mean_shift(data):
    labels = set(MeanShift().fit(data.values).labels_)
    num_labels = len(labels) - (1 if -1 in labels else 0)
    return json.dumps(num_labels)

@result_route
def dbscan(data):
    labels = set(DBSCAN().fit(data.values).labels_)
    num_labels = len(labels) - (1 if -1 in labels else 0)
    return json.dumps(num_labels)
