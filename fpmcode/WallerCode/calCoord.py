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
    uCent = freqUV(:,0) 
    vCent = freqUV(:,1)
    #index of middle of image
    xMid = imSz//2 + 1 
    yMid = imSz//2 + 1
    #creates meshgrid of the pixel indexes within the image
    xpix = np.linspace(-(imSz//2), imSz//2, imSz)
    ypix = np.linspace(-(imSz//2), imSz//2, imSz)
    xI,yI = np.meshgrid(xpix, ypix)

    #new pixel indices in terms of kx, ky?
    xCent = xMid + uCent * con
    yCent = yMid + uCent * con

    


