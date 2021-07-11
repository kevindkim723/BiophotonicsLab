import numpy as np

def wrapTo180(a):
	return np.where(abs(a) > 180, -np.sign(a) * (180-abs(a)%180), a)

