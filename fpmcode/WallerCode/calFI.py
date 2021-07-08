from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2

#I: images (intensity) 250x250x293. Interpret as imSeqLowRes
#xI: 2-d array of the X pixel indices (from meshgrid)
#yI: 2-d array of the Y pixel indices (from meshgrid)
#XYmid: tuple containing middle indices of image
#radP: radius of the NA (in pixels)
#sigmaG: sigma=2 within gaussian filtering

"""Program steps
    1) convert images into intensity valued fourier spectrum
    2) take the mean across all spectrum images-- this results in a "mean spectrum"
    3) take the mean value outside the 2NA support in the mean spectrum
    4) from the mean spectrum, floor out the noise outside the 2NA support (any pixels outside 2NA support with values less than 3*mean Imag
    5)  divide out the modified mean spectrum from all the FT images
    6)  from those images, convolve them with Gaussian Kernel std.dev 2 pixels"""

def calFI(I,xI, yI,XYmid, radP, sigmaG):
    FI = fftshift(fft2(I,axes=[1,0]),axes=[1,0]) #FT the image set
    avgFI = np.mean(np.abs(FI),2) #take the mean across all images
    w_2NA=np.sqrt((xI-XYmid[0])**2 + (yI-XYmid[1])**2)>=2*radP; #Outside 2NA support
    mT = np.mean(avgFI[w_2NA]) #the mean value outside the 2NA support
    avgFI2 = np.where(avgFI < 3*mT, 3*mT, avgFI)#if values are less than 3*mT then floor them to the 3*mT (essentially getting rid of noise outside the 2NA support).
    FIdiv = FI/np.tile(avgFI2[:,:,np.newaxis], [1,1, FI.shape[2]])

    FIdivG = cv2.GaussianBlur(np.abs(FIdiv),ksize=(0,0),sigmaX=2,borderType=cv2.BORDER_REPLICATE)#convolving with the Gaussian Kernel with std.dev = 2 pixels
    return FIdiv, FIdivG, FI, w_2NA
    



    
    
