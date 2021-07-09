#adapted from https://github.com/Waller-Lab/Angle_SelfCalibration/blob/master/Utilities/cart2Pol.m
import numpy as np
import numpy.matlib


"""returns a (293,2) array containg column vectors of 
inputs:
    XY:  (293,2) containing column vectors of kx, ky in pixel coords
    XYmid: (1,2) array containing middle positions
"""
def cart2Pol(XY,XYmid):

    #centD: circle centers distances from coordinate origin
    #theta: angle of circle centers

    centD = np.sqrt(np.sum((XY - np.matlib.repmat(XYmid, XY.shape[0],1))**2,axis=1))
    theta = np.arctan2(XY[:,0] - XYmid[0], XY[:,0] - XYmid[1])

    #reshape 1D row vectors into column vectors
    centD = centD[:,np.newaxis]
    theta = theta[:,np.newaxis]

    DTh = np.concatenate((centD,theta),axis=1)
    
    return DTh

    

