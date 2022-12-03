import numpy
from ctypesexample.summing import csum, add

array = numpy.arange(0, 100000000, 1, numpy.int32)
array_sum = csum(len(array), array)

print("sum of array: {}".format(array_sum))


a = [1.2, 2.0, 4.0]
b = [2.0, 3.2, 3.2]
print(add(a, b))
