import numpy

def middle(results):
    results['mean'] = numpy.mean(results['data'], axis=0)
    results['median'] = numpy.median(results['data'], axis=0)
    return results
