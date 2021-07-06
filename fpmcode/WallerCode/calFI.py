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
    FI = fftshift(fft2(I,axes=[1,0]),axes=[1,0]) #FT the image set
    avgFI = np.mean(np.abs(FI),2) #take the mean across all images
    print(radP)
    w_2NA=np.sqrt((xI-XYmid[0])**2 + (yI-XYmid[1])**2)>2*radP; #Outside 2NA support
    print(xI)
    mT = np.mean(w_2NA * avgFI) #the mean value outside the 2NA support
    avgFI2 = np.where(avgFI < 3*mT, 3*mT, avgFI)#if values are less than 3*mT then floor them to the mean.
    return avgFI2
    



    
    
