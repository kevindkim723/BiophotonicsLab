import numpy as np

def wrapTo180(a):
	return np.where(a > 180, 180-a%360, a)

print(np.arange(0,5,1))