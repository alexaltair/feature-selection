import numpy

def middle(data, results):
    results['mean'] = numpy.mean(data, axis=0)
    results['median'] = numpy.median(data, axis=0)
    return results
