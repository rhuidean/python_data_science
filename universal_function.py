import timeit
import numpy as np
np.random.seed(0)


def compute_reciprocals(values):
	output = np.empty(len(values))

	for i in range(len(values)):
		output[i] = 1.0/ values[i]
	return output


big_array = np.random.randint(1,10,size=50)
print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

x=np.arange(4)
print x
print("x /2 =",x/2)
print("x //2 =",x//2)

x=np.arange(1,6)
print x

print np.add.reduce(x)
print np.multiply.reduce(x)
print np.multiply.accumulate(x)