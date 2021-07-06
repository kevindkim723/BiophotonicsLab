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
    FI = fftshift(fft2(I,axes=[1,0]),axes=[1,0])
    avgFI = np.mean(np.abs(FI),2)
    w_2NA=np.sqrt((xI-XYmid[0])**2 + (yI-XYmid[1])**2)>2*radP; #Outside 2NA support
    mT = np.mean(w_2NA * avgFI)
    print(mT)
    avgFI2 = np.where(avgFI < mT, mT, avgFI)
    return avgFI2
    



    
    
