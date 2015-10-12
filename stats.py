from pandas import Series, DataFrame
from sklearn.decomposition import PCA

def middle(data, results):
    results['mean'] = data.mean().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])
    results['median'] = data.median().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

def variance(data, results):
    data_variance = data.var()
    results['variance'] = data_variance.to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

    results['sorted_variance'] = data_variance.sort_values().to_frame().T.to_html(
        index=False,
        classes=['table', 'table-condensed', 'table-bordered'])

    results['covariance'] = data.cov().to_html(
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

def pca(data, results):
    remaining_variance = PCA().fit(data).explained_variance_ratio_
    index = range(1, len(remaining_variance)+1)
    remaining_variance = DataFrame({
        "Component": index,
        "Explained variance ratio": remaining_variance,
    }, dtype=object)

    results['pca'] = remaining_variance.T.to_html(header=False,
        classes=['table', 'table-condensed', 'table-bordered'])
