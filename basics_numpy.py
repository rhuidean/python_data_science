L = list(range(10))
L2 = [str(c) for c in L]
print "{} {}".format(type(L[0]),type(L2[0]))

L3 = [True,"2",3.0,4]
print [type(item) for item in L3]

import numpy as np

# integer array:
print np.array([1,4,2,5,3])
print np.array([1,4,2,5,3],dtype='float32')

# multi-dimensional array vs list one-dimensional array
print np.array([range(i,i+3) for i in [2,4,6]])