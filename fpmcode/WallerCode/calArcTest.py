#program to test calArc using specific parameters from vals.in
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
from calArc import calArc
fname = "/home/kevin/Harvey Mudd/biophotonics/Angle_SelfCalibration-master/data/LED_cheekCell_comp_misaligned_input.mat"

fname2 = "/home/kevin/Harvey Mudd/biophotonics/code/data/input_data_USAF.mat"
vals = open('vals.in', 'r')
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
lines = vals.readlines()
distV = np.array(lines[1].split()).astype(float)
thetaV = np.array(lines[2].split()).astype(float)
angleV = np.array(lines[0].split()).astype(float)

distV = distV[np.newaxis,:]
angleV = angleV[np.newaxis,:]
thetaV = thetaV[np.newaxis,:]
print("distV: " , distV)
print("angleV: " , angleV)
print("thetaV: " , thetaV)
arcMat, numA2 = calArc(radP,distV, thetaV, angleV) 
print(numA2)

