import numpy
import pandas

def middle(data, results):
    results['mean'] = data.mean().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])
    results['median'] = data.median().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

def variance(data, results):
    data_variance = data.var()
    results['variance'] = data_variance.to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

    results['sorted_variance'] = data_variance.sort_values().to_frame().T.to_html(
        index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

    results['covariance'] = data.cov().to_html(
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])
