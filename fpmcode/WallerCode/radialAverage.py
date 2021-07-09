from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2
from wrapTo180 import wrapTo180
def radialAverage(img, radius, testRadius,testTheta, testDist):
    testTheta = wrapTo180(testTheta)
    xI,yI = np.meshgrid(np.arange(img.shape[1],np.arange(img.shape[0])))
    xMid = img.shape[1]//2
    yMid = img.shape[0]//2

    numTh=len(testTheta)
    numD = len(testDist)
    numR = len(testRadius)
    
    circleTheta = wrapTo180(np.arange(0,360+180/64,180/64))




