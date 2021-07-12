from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2
from wrapTo180 import wrapTo180
from calArc import calArc
'''
radius: radius defined by optical system (radius we are trying to correct)
testRadius: column vector of test radii
testTheta: column vector of test thetas defined from the x axis to the circle center distances
testDist: column vector of test distances to the circle centers
'''
def radialAverage(img, radius, testRadius,testTheta, testDist,jj):
    f = open("vals.out", "a")
    '''I want to write out the 
    jj
    testTheta
    testDist
    testAngles
    (the parameters for calArc essentially because if the parameters are right, then the function should run succesfully...
    '''
    testTheta = wrapTo180(testTheta)[np.newaxis,:]
    xI,yI = np.meshgrid(np.arange(img.shape[1]),np.arange(img.shape[0]))
    xMid = img.shape[1]//2
    yMid = img.shape[0]//2

    numTh=len(testTheta)
    numD = len(testDist)
    numR = len(testRadius)
    
    circleTheta = wrapTo180(np.arange(0,360+180/64,180/64))
    circleTheta = circleTheta[np.newaxis,:]

    numA = circleTheta.shape[1]
    '''print("testRadius : {}".format(testRadius))
    print("numA shape: {}".format(numA))
    print("numTh shape: {}".format(numTh))
    print("numD shape: {}".format(numD))
    print("circleTheta shape: {}".format(circleTheta.shape))'''

    #rMat: 21x129x21x41 repeated matrix of the testRadii
    #aMat: 21x129x21x41 repeated matrix of angles from (-180,180)
    rMat = np.tile(testRadius[:,:,np.newaxis,np.newaxis],(1,numA,numTh,numD))#i swear this line took me so long...
    aMat = np.tile(circleTheta[:,:,np.newaxis,np.newaxis],(numR,1,numTh,numD))#i swear this line took me so long...
    #print("rMat shape: {}".format(rMat.shape))
    #print("aMat shape: {}".format(aMat.shape))

    #rcos, rsin vectors are respective x, y components of the edges of circles defined by testRadius vector (test radii)
    rcos = rMat * np.cos(aMat)
    rsin = rMat * np.sin(aMat)
    f.write("*" * 40)
    f.write("\n")
    f.write("image #: " + str(jj)+"\n")
    f.write("radius: " + str(radius)+"\n")
    f.write("circle Theta:\n")
    f.write(np.array_str(circleTheta))
    f.write("\n")
    f.write("test Dist:\n")
    f.write(np.array_str(testDist))
    f.write("\n")
    f.write("test Theta:\n")
    f.write(np.array_str(testTheta))
    f.write("\n")
    f.close()

    calArc(radius, testDist, testTheta, circleTheta)




