import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift
import os
import scipy.io as sio
fname = "/home/kevin/Harvey Mudd/biophotonics/Angle_SelfCalibration-master/data/LED_cheekCell_comp_misaligned_input.mat"
data_fname = os.path.normpath(fname)
data = sio.loadmat(data_fname,struct_as_record=False,squeeze_me=True)
metadata = data['metadata']
NA = metadata.objective.na
dpix_c = metadata.camera.pixel_size_um;
wavelength = metadata.illumination.wavelength_um;
freqUV = metadata.source_list.na_design/wavelength
I = data['data']
print(I.shape)
fig,ax = plt.subplots(1,1)
him=ax.imshow(np.abs(fftshift(fft2(I[:,:,0],axes=[0,1]),axes=[1,0])),norm=colors.LogNorm())
plt.show()


