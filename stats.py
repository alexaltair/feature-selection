import numpy
import pandas

def middle(data, results):
    results['mean'] = data.mean().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])
    results['median'] = data.median().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])

def variance(data, results):
    results['variance'] = data.var().to_frame().T.to_html(index=False,
        classes=['table', 'table-condensed', 'table-bordered', 'table-striped'])
