import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.ndimage.filters import gaussian_filter
from kMeansCluster import kMeans2Cluster
'''
    Uses a K-Means clustering algorithm to seperate brightfield images
    from darkfield images by parsing the DC component of fourier spectrum.
'''

#input: FI: set of n fourier spectrum images
#       XYmid: tuple containing middle pixel index of fourier spectrum image
#output: DF: array of size n where 1 denotes image at ith index is darkfield, and 0 at ith index indicates a brightfield.
def calDF(FI, XYmid):
    DC=np.squeeze(abs(FI[XYmid[1],XYmid[0],:]))
    print(XYmid[1], XYmid[0])
    print(FI.shape[0])
    print(DC[0])
    
    npix = np.size(FI[:,:,1])
    minBF=2000 #heuristic value (establishes the DC term for brightfields)
    if min(DC/npix) > minBF:
        DFI = np.zeros(np.size(DC))
        print("daisy")
    else:
        Kidx, c1,c2 = kMeans2Cluster(DC)
    DF = np.zeros(FI.shape[2])
    if c1 < c2 :
        DF = 1-Kidx
    else:
        DF = Kidx
    print("DF: ", np.count_nonzero(DF==1))
    print("BF: ", np.count_nonzero(DF==0))
    print("Indices: ",np.where(DF == 0))


    
    return DF

