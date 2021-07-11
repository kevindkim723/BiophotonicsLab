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
    testDist: 1x41 of test circle center distances
    testTheta: 1x21 of theta to circle centers
    circleTheta: 1x129 of (-180,180)
'''
def calArc(rad, testDist, testTheta, circleTheta):
    numTh = len(testTheta) #number of test circle center theta
    numA= len(circleTheta) #number of circle theta angles

    #if the mean of distance to circle centers is less than the radius, this means that the circle probably crosses the origin
    print("testDist: {}".format(testDist))
    if np.mean(testDist) <= rad:
        phi = numpy.degrees(np.arccos(np.mean(testDist)/rad))
    else:
        phi = 0
    print("phi: {}".format(phi))
    theta_lower = wrapTo180(testTheta + phi-180) #lower bound
    theta_upper = wrapTo180(2*testTheta - theta_lower)#upper bound
    print("theta_lower shape: {}".format(theta_lower.shape))

    angleA = np.tile(circleTheta,[numTh, 1]) >= np.tile(theta_lower.T,[1, numA])
    angleB = np.tile(circleTheta,[numTh, 1]) <= np.tile(theta_upper.T,[1, numA])

    print("theta_upper: {}".format(theta_upper))
    print("theta_lower: {}".format(theta_lower))
    #print("angleA shape: {}".format(angleA))
    #print("angleB shape: {}".format(angleB))
    #arcMat = angleA == angleB
    #print("arcMat shape {}:".format(arcMat))


    
    

