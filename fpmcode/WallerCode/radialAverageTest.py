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
from radialAverage import radialAverage
fname = "/home/kevin/Harvey Mudd/biophotonics/Angle_SelfCalibration-master/data/LED_cheekCell_comp_misaligned_input.mat"

fname2 = "/home/kevin/Harvey Mudd/biophotonics/code/data/input_data_USAF.mat"
vals = open('vals2.in', 'r')
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
jj = int(lines[0])
testR = np.array(lines[1].split()).astype(float)
distV = np.array(lines[2].split()).astype(float)
thetaV = np.array(lines[3].split()).astype(float)

#reshape
testR = testR[:, np.newaxis]
distV = distV[np.newaxis,:]
"""print("testRadii: " , testR)
print("distV: " , distV)
print("thetaV: " , thetaV)"""
print("jj: {}".format(jj))
print("radP: {}".format(radP))
print("testR shape: {}".format(testR.shape))
print("thetaV shape: {}".format(thetaV.shape))
print("distV shape: {}".format(distV.shape))

arcMat, numA2 = radialAverage(FIdivG[:,:,jj], radP, testR, thetaV, distV,jj)
vals.close()


