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

freqXY, con, radP, xI, yI, uI, vI, XYmid = calCoord(freqUV, imSz, dpix_c,mag, NA, wavelength)
freqDTh=cart2Pol(freqXY, XYmid)

sigmaG = 2
FIdiv, FIdivG, FI, w_2NA = calFI(I,xI,yI,XYmid, radP,sigmaG)



fig,ax = plt.subplots(1,1)
twins= (np.abs(np.log(FIdivG[:,:,69])))
a,b = gradientImage(twins)
him = ax.imshow(twins)
print(freqXY[0].shape, "FREQ")
plt.show()
calDF(FI,XYmid)



