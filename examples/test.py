import numpy 
from ctypesexample.summing import csum

array = numpy.arange(0, 100000000, 1, numpy.int32)
array_sum = csum(len(array), array)

print("sum of array: {}".format(array_sum))
