from skimage import io
from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
from matplotlib import colors
import os
import math
import matplotlib.pyplot as plt
import numpy as np


kevin = io.imread("kevin.jpg")
kevinstar = io.imread("kevinstar.png")
print(kevin.shape)
kevinfft = fftshift(fft2(kevin[:,:,2]))
fig, ax = plt.subplots(1,2)
img=  ax[0].imshow(np.abs(kevinfft), norm=colors.LogNorm())
img=  ax[1].imshow(np.abs(ifft2(ifftshift(kevinstar))))

plt.show()




