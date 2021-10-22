import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift
import os
from calCoord import calCoord
from calFI import calFI
from calDF import calDF
import scipy.io as sio
from old import gradientImage
from cart2Pol import cart2Pol
from calCircEdge import calCircEdge
f = open("vals.out","w")
f.truncate(0)
f.close()
fname = "/home/kevin/Harvey Mudd/biophotonics/Angle_SelfCalibration-master/data/LED_cheekCell_comp_misaligned_input.mat"
fname2 = "/home/kevin/Harvey Mudd/biophotonics/code/data/input_data_USAF.mat"
data_fname = os.path.normpath(fname)
data_fname2 = os.path.normpath(fname2)
data = sio.loadmat(data_fname,struct_as_record=False,squeeze_me=True)
data2 = sio.loadmat(data_fname2)
metadata = data['metadata']
mag=metadata.objective.mag*metadata.objective.system_mag
NA = metadata.objective.na
dpix_c = metadata.camera.pixel_size_um;
wavelength = metadata.illumination.wavelength_um;
freqUV = metadata.source_list.na_design/wavelength
I = data['data']
#I = data2['imseqlow']
imSz = len(I[:,:,125])


rScan = np.array([5,.5])
thScan = np.array([[10,1],[5,.5]])
dScan = np.array([[20,1],[5,.5]])
calRad =1

freqXY, con, radP, xI, yI, uI, vI, XYmid = calCoord(freqUV, imSz, dpix_c,mag, NA, wavelength)
print("RADP:{}".format(radP))
sigmaG = 2
cart2Pol(freqXY, XYmid)
FIdiv, FIdivG, FI, w_2NA = calFI(I,xI,yI,XYmid, radP,sigmaG)
DF = calDF(FI, XYmid)
freqDTh = cart2Pol(freqXY, XYmid)

calCircEdge(FIdivG[:,:,np.where(DF!=1)[0]], I, radP, freqDTh[np.where(DF!=1)[0],:], XYmid, xI, yI, sigmaG, rScan, thScan, dScan, calRad, con, wavelength)
