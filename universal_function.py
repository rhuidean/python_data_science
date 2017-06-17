import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
	### create a output bucket
	output = np.empty(len(values))

	### populate the bucket np array
	for i in range(len(values)):
		output[i] = 1.0/ values[i]
	return output

values = np.random.randint(1,10,size=5)
print compute_reciprocals(values)