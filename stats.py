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

def pca(data):
    remaining_variance = PCA().fit(data).explained_variance_ratio_
    index = range(1, len(remaining_variance)+1)
    remaining_variance = DataFrame({
        "Component": index,
        "Explained variance ratio": remaining_variance,
    }, dtype=object).T

    return {
        'table': remaining_variance.to_html(header=False,
            classes=['table', 'table-condensed', 'table-bordered']),
        'json': remaining_variance.to_json()
    }

def mean_shift(data):
    labels = MeanShift().fit(data.values).labels_
    return len(set(labels)) - (1 if -1 in labels else 0)

def dbscan(data):
    labels = DBSCAN().fit(data.values).labels_
    return len(set(labels)) - (1 if -1 in labels else 0)


def generate_results(data):
    results = {}

    try:
        results['pca'] = pca(data)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass
    try:
        results['mean_shift'] = mean_shift(data)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass
    try:
        results['dbscan'] = dbscan(data)
    except ValueError:  # Could be "Array contains NaN or infinity."
        pass

    return results
