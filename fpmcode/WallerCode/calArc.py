from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import math
import numpy.matlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import cv2
from wrapTo180 import wrapTo180
from scipy import stats
import sys
np.set_printoptions(threshold=sys.maxsize)


'''
inputs:
    testDist: 1x41 of test circle center distances
    testTheta: 1x21 of theta to circle centers
    circleTheta: 1x129 of (-180,180)
'''
def calArc(rad, testDist, testTheta, circleTheta):
    numTh = len(testTheta) #number of test circle center theta
    numA= (circleTheta.shape[1]) #number of circle theta angles
    f = open("vals.out","w")

    #if the mean of distance to circle centers is less than the radius, this means that the circle probably crosses the origin
    if np.mean(testDist) <= rad:
        phi = numpy.degrees(np.arccos(np.mean(testDist)/rad))
    else:
        phi = 0
    theta_lower =(testTheta + phi-180) #lower bound
    theta_upper =(2*testTheta - theta_lower)#upper bound
    theta_lower_wrap = wrapTo180(theta_lower)
    theta_upper_wrap = wrapTo180(theta_upper)

    #these angle matrices correspond to the angles within (-180, 180) that meet within lower and upperbound criteria
    angleA = np.tile(circleTheta,[numTh, 1]) >= np.tile(theta_lower_wrap.T,[1, numA])
    angleB = np.tile(circleTheta,[numTh, 1]) <= np.tile(theta_upper_wrap.T,[1, numA])

    '''print("theta_upper: {}".format(theta_upper.shape))
    print("theta_lower: {}".format(theta_lower.shape))'''
    #print("theta_upper: {}".format(theta_upper))
    #print("theta_lower: {}".format(theta_lower))
    '''print("angleA shape: {}".format(angleA.shape))
    print("angleB shape: {}".format(angleB.shape))'''
    #these are logical index matrices we will select angles from.
    arcMat = angleA & angleB #angles within the circular range that are within lower and upper bound
    f.write("ARCMAT REEE: ")
    f.write(str(np.count_nonzero(arcMat)))

    wrapTheta = (np.tile(theta_lower.T, [1,numA])< -180) | (np.tile(theta_upper.T, [1, numA])>180)
    #print("wrapTheta: {}".format(wrapTheta))
    #wrapTheta = (np.matlib.repmat(theta_lower.T,1,numA) < -180) | (np.matlib.repmat(theta_upper.T,1,numA)>180)
    #print("wrapTheta shape: {}".format(wrapTheta.shape)
    #print((arcMat==1).sum())

    arcMat[wrapTheta] = angleA[wrapTheta]|angleB[wrapTheta]
    f.write("\n" + np.array_str(arcMat)+"\n")

    #print("arcMat: {}".format(arcMat))
    numAcap = np.sum(arcMat,axis=1)[:,np.newaxis]
    numA2 = stats.mode(numAcap)[0].item(0)
    difA = numAcap-numA2
    f.write("numA2: {}\n".format(numA2))
    f.write("num1s arcmat: {}".format((arcMat==1).sum()))
    '''print("numA2: {}".format(numA2))
    print("numAcap: {}".format(numAcap))
    print("difA: {}".format(difA))'''
    
    if np.any(difA<0):
        ind = np.where(difA<0)[0]
        for kk in range(ind.size):
            numAdd = abs(difA[ind[kk]])
            temp =arcMat[ind[kk],:][np.newaxis,:]
            dT = np.diff(temp.astype(int))
            even = np.floor(numAdd/2)
            odd = numAdd%2
            up = np.where(dT[0]<0)[0]
            bottom = np.where(dT[0]>0)[0]
            

            if up.size == 0:
                up=temp.size
            if bottom.size ==0:
                bottom= 1
            #print("(FIRST) up:{}. bottom: {}".format(up,bottom))
            upI = np.arange(up+1,up+even+odd+1)
            upI[upI>temp.size] = upI[upI>temp.size]-temp.size

            bottomI = np.arange(bottom,bottom-even,-1)
            bottomI[bottomI<1] = bottomI[bottomI<1]+temp.size
            upI = upI.astype(int)
            bottomI = bottomI.astype(int)
            #print("tempI shape: {}".format(temp.shape))
            #print("(FiRST)upI:{}. bottomI: {}".format(upI,bottomI))
            temp[0,upI] = 1
            temp[0,bottomI] = 1
            arcMat[ind[kk],:] = temp
            


    if np.any(difA>0):
        ind = np.where(difA>0)[0]
        #print("ind: {}".format(ind))
        #print(ind[0])
        for kk in range(ind.size):
            numDel = abs(difA[ind[kk]])
            temp=arcMat[ind[kk],:][np.newaxis,:]
            #print("before the chaos: ", (temp==1).sum())
            dT=np.diff(temp.astype(int)) #I have to cast as int array or else numpy thinks its all booleans and the diff() doesnt work properly
            even = np.floor(numDel/2)
            odd = numDel%2

            up = np.where(dT[0]<0)[0]
            bottom = np.where(dT[0]>0)[0]

            if up.size == 0:
                up = temp.size
            if bottom.size == 0:
                bottom = 1
                
            #print("(SECOND) up:{}. bottom: {}".format(up,bottom))
            upI = np.arange(up, up-even-odd, -1)
            upI[upI<1] = upI[upI<1]+temp.size

            bottomI = np.arange(bottom, bottom+even)
            bottomI[bottomI>temp.size] = bottomI[bottomI>temp.size]-temp.size
            upI = upI.astype(int)
            bottomI = bottomI.astype(int)
            #print("tempI shape: {}".format(temp.shape))

            #print("(SECOND)upI:{}. bottomI: {}".format(upI,bottomI))
            temp[0,upI] = 0
            temp[0,bottomI] = 0
            b=arcMat[ind[kk],:]
            arcMat[ind[kk],:]=temp
            #print("after the chaos: ", (temp==1).sum())

    #print(arcMat.shape)
    prevInd = 0;
    for i in range(0, 129, 34):
        f.write("cols {} to {}\n".format(i, i+33))
        f.write(np.array_str(arcMat[:,i:i+34].astype(int)))
        f.write("\n")


    f.write(str(np.count_nonzero(arcMat)))
    f.write(str((arcMat==0).sum()))
    f.close()
    #print("phi: ", phi)
    #print((arcMat==1).sum())

    arcMat = np.transpose(arcMat[:,:,np.newaxis], (2,1,0))
    return arcMat,numA2


        
#%%



    
    

