import numpy as np

def wrapTo180(a):
        b= np.where(abs(a) > 180, -np.sign(a) * (180-abs(a)%180), a)
        return np.where(b == -180,0,b)

print(wrapTo180(360))
