from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2
import random

def calCircEdge(FIdivG, I, radP, freqDTh, XYmid, xI, yI, sigmaG, rScan, thScan, dScan, calRad, con, wavelength):

    #unwrap circle center distance (KX/KY) and theta column vectors
    centD2 = freqDTh[:,0]
    theta2 = freqDTh[:,1]

    imSz = FIdivG.shape
    numImg = imSz[2]

    print("FIdivG.shape: {}".format(FIdivG.shape))
    print("number of brightfields: {}".format(numImg))

    offsetRad = np.arange(-rScan[0],rScan[0]+rScan[1],rScan[1]) #row vector of potential radii to test (-2,-1.5,...,2)
    offsetTh = np.arange(-thScan[0,0], thScan[0,0] + thScan[0,1],thScan[0,1]) #row vector of potential theta in degrees to test  (-5,-4.75,...,5) 
    offsetDi = np.arange(-dScan[0,0], dScan[0,0] + dScan[0,1],dScan[0,1])#row vector of potential circle center distances to test (-20,-19,...,20)
    done = False
    checkDone = False
    numIter = 0

    rad = radP
    radList = rad;

    r_tol = np.array([rScan[0]*1.1, rScan[1]*.9])
    PDindFR = np.linspace(0, int(rScan[0])-1,int(rScan[0]))
    print("rScan[0]: {}".format(rScan[0]))
    print("Calibrating Radius...")
    
    while not done:
        numIter += 1
        print("Iteration: {} ; Radius: {} pixels".format(numIter, rad))

        #radV: radius to test
        radV = offsetRad + rad
        
        #select 20 images at random from the set of brightfields
        if numImg > 20:
           imgI = np.array(random.sample(range(numImg), 20))


        else:
            imgI = np.linspace(0,numImg-1, numImg) 
        PDIfr = np.zeros(numImg)
        print("imgI: {}".format(imgI))
        for jj in range(numImg):
            centDV = offsetDi + centD2(imgI[jj]) #potential circle center distances. centD2 is the expected circle center, while offsetDi is the row vectors of scanning values.
            centDV[centDV<0] = [] #we can't work with negative indices!
            pixMean = radialAverage 


        done = True

    
    
