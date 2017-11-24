from scipy import stats
import numpy as np


def counting(runs):

	n = [0]
	n1 = [0]
	for i in range(1, runs):
		n.append(i)
		t = stats.uniform.rvs(0, 1, 1)
		p = np.power(2, n1[i-1])
		p = 1/p
		if t <= p:
			n1.append(n1[i-1]+1)
		else:
			n1.append(n1[i-1])
	return n, n1


sums = [0 for t in range(20)]
for j in range(1000):
	n, temp = counting(20)
	for t in range(20):
		sums[t] = sums[t]+temp[t]
for t in range(20):
	sums[t] = sums[t]/1000
print(sums)