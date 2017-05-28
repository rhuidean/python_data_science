import numpy as np

### Generate 100 random numbers between 0 and 1
L = np.random.random(100)
print type(L)
print "{} {}".format(sum(L),np.sum(L))

### Compare the compile timing
big_array = np.random.rand(1000000)
print big_array[0]
