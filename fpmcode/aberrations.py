from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import os
import scipy.io as sio
from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift
from zernike import RZern


kevin = io.imread("kevin.jpg")
width = kevin.shape[1]//2
height = kevin.shape[0]//2
x = np.arange(-width,width)
y = np.arange(-height,height)
X,Y = np.meshgrid(x,y)
a = np.arange(-256,256)
A,B = np.meshgrid(x,x)
r =50
CTF = X**2+Y**2 < r**2
CTFTEST = A**2 + B**2 < r**2

spherical = (4*(X**2 + Y**2)**2-3*(X**2+Y**2))
sphericalTEST =4*(A**2+B**2)**2-3*(A**2 + B**2)
fieldCurvatureTEST = (2*(A**2+B**2)-1)
astigTEST = (A**2 +B**2)*np.cos(2*np.arctan2(B,A))
astig = (X**2 +Y**2)*np.cos(2*np.arctan2(Y,X))
comaTEST = (3 * (A**2 + B**2)-2*(np.sqrt(A**2+B**2)))*np.sin(np.arctan2(B,A))

mask_astig = CTF*(np.exp(1j*astig))
mask_spherical = CTF * (np.exp(1j*spherical))
mask_sphericalTEST = sphericalTEST * CTFTEST
mask_astigTEST = astigTEST * CTFTEST
mask_fieldCurvatureTEST = CTFTEST * fieldCurvatureTEST
mask_comaTEST = comaTEST * CTFTEST




kevinfft = fftshift(fft2(kevin[:,:,0]))
fft_mask = kevinfft*mask_spherical




fig, ax = plt.subplots(1,8)
ax[0].imshow(np.abs(kevinfft), norm=colors.LogNorm())
ax[1].imshow(np.abs(ifft2(kevinfft)))
ax[2].imshow(np.abs(ifft2(fft_mask)))
ax[3].imshow(np.abs(fft_mask),norm=colors.LogNorm())
ax[4].imshow(np.abs(mask_sphericalTEST))
ax[5].imshow(np.abs(mask_astigTEST))
ax[6].imshow((mask_fieldCurvatureTEST))
ax[7].imshow(np.abs(mask_comaTEST))


ax[4].set_title("Spherical")
ax[5].set_title("Astigmatism")
ax[6].set_title("Field Curvature")
ax[7].set_title("Coma")


plt.show()
