from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2
from wrapTo180 import wrapTo180


'''
inputs:
    testDist:
    testTheta:
    circleTheta:
'''
def calArc(rad, testDist, testTheta, circleTheta):
    numTh = len(testTheta)
    numA= len(circleTheta)

    #if the mean of distance to circle centers is less than the radius, this means that the circle probably crosses the origin
    if np.mean(testDist) <= rad:
        phi = np.arccos(mean(testDist)/rad)
    else:
        phi = 0

