L = list(range(10))
L2 = [str(c) for c in L]
print "{} {}".format(type(L[0]),type(L2[0]))

L3 = [True,"2",3.0,4]
print [type(item) for item in L3]

import numpy as np

# integer array
print np.array([1,4,2,5,3])
print np.array([1,4,2,5,3],dtype='float32')

# multi-dimensional array vs list one-dimensional array
print "range {}".format(np.array([range(i,i+3) for i in [2,4,6]]))
print "arange {}".format(np.arange(10))
print "arange {}".format(np.arange(0,20,2))
print "linspace {}".format(np.linspace(0,20,10))
 
# zeros array
print np.zeros(10,dtype=int)

# random
print np.random.random((3,3))
print np.random.random(6)
print np.random.randint(0,10,(3,3))
print np.random.normal(0,1,3)


# NumPy Array Attributes
x1 = np.random.random(size=(3,3))
print "ndim, shape, size, dtype, itemsize {} {} {} {} {}".format(x1.ndim,x1.shape,x1.size,x1.dtype,x1.itemsize)

# Array Indexing Front & Back
print x1[2][0]
print x1[-2][-1]

print x1[2][1] 
x1[2][1]=0.2
print x1[2][1]

# Array Slicing
x2 = np.arange(10)
print x2[5:]
print x2[4:7]
print x2[1::2]
print x2[5::-1]
print x2[::-1]

# ReShaping Arrays
grid = np.arange(1,10).reshape((3,3))

# Concatentation and Splitting
x = np.array([1,2,3])
grid = np.array([[9,8,7],[6,5,4]])
print np.vstack([x,grid])
y =np.array([[1],[1]])
print np.hstack([grid,y])



