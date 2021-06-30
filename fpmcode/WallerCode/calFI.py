from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
#I: images (intensity) 250x250x293. Interpret as imSeqLowRes
#xI: 2-d array of the X pixel indices (from meshgrid)
#yI: 2-d array of the Y pixel indices (from meshgrid)
#XYmid: tuple containing middle indices of image
#radP: radius of the NA (in pixels)
#sigmaG: sigma=2 within gaussian filtering

def calFI(I,xI, yI,XYmid, radP, sigmaG):
    FI = fftshift(fft2(I))
    avgFI = np.mean(np.abs(FI),2)
    



    
    
