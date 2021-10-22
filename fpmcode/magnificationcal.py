from skimage import io
from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
from matplotlib import colors
import os
import math
import matplotlib.pyplot as plt
import numpy as np


target = io.imread("magtest.jpg")
print(target.shape)
fig, ax = plt.subplots(1,2)
img=  ax[0].imshow(target)
xval = np.linspace(1000,1250,251)
print(xval)
yval = target[:,:,0][target.shape[0]-1,1000:1251]
ax[1].set(xlabel='pixel', ylabel='phase',
       title='intensity vs  pixel positions')
ax[1].plot(xval, yval,label="across equator of image")


ax[1].grid(which='minor')
ax[1].minorticks_on()
ax[1].legend()
ax[1].axvline(x=1050,color='k')
ax[1].axvline(x=1082,color='k')



plt.show()




