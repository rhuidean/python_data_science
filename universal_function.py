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

''' advanced ufunc features '''
x = np.arange(5)
y = np.empty(5)
np.multiply(x,10, out=y)
print y

y = np.zeros(10)
np.power(2,x,out=y[::2])
print y

''' Aggregations '''
L = np.random.random(100)
print sum(L)
print np.sum(L)
print "{} {}".format(min(L),max(L))
print "{} {}".format(np.min(L),np.max(L))