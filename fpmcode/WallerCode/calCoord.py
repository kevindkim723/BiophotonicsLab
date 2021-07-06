#adapted from https://github.com/Waller-Lab/Angle_SelfCalibration/blob/master/Utilities/calCoord.m
import numpy as np

def calCoord(freqUV,imSz,dpix_c,mag,NA,wavelength):
    #imSz: square image width
    #freqUV: ?
    #dpix_c: sensor pixel size (not accounted for magnification)
    #mag: magnification of optical system
    #NA: NA
    #wavelength: wavelength of light used for imaging

    #256 * sensor_pixel_size/4
    con = imSz * dpix_c/mag

    #kx, ky vectors
    uCent = freqUV[:,0] 
    vCent = freqUV[:,1]
    #index of middle of image
    xMid = imSz//2 + 1 
    yMid = imSz//2 + 1
    #creates meshgrid of the pixel indexes within the image
    xpix = np.linspace(-(imSz//2), imSz//2, imSz)
    ypix = np.linspace(-(imSz//2), imSz//2, imSz)
    xI,yI = np.meshgrid(xpix, ypix)

    #new pixel indices in terms of kx, ky?
    #basically k-space coordinates in terms of pixels.
    xCent = xMid + uCent * con
    yCent = yMid + uCent * con

    freqXY=(xCent, yCent)
    XYmid = (xMid, yMid)

    #Radius of NA (in pixels)
    radP = NA * con / wavelength
    #k space coordinates (1/um)
    uI = (xI- xMid)/con
    vI = (yI- xMid)/con
    return freqXY, con, radP, xI, yI, uI, vI, XYmid;





    


