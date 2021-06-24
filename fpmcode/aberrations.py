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
height = (kevin.shape[0])//2
x = np.arange(-width,width+1)
y = np.arange(-height,height)
x = np.linspace(-1,1,kevin.shape[1])
y = np.linspace(-1,1,kevin.shape[0])
X,Y = np.meshgrid(x,y)
a = np.arange(-256,256)
A,B = np.meshgrid(x,x)
r =.5
CTF = X**2+Y**2 < r**2
CTFTEST = A**2 + B**2 < r**2

spherical = (4*(X**2 + Y**2)**2-3*(X**2+Y**2))
print(f"max spherical = {np.max(spherical)}")
sphericalTEST =4*(A**2+B**2)**2-3*(A**2 + B**2)
fieldCurvatureTEST = (2*(A**2+B**2)-1)
astigTEST = (A**2 +B**2)*np.cos(2*np.arctan2(B,A))
astig = (X**2 +Y**2)*np.cos(2*np.arctan2(Y,X))
comaTEST = (3 * (A**2 + B**2)-2*(np.sqrt(A**2+B**2)))*np.sin(np.arctan2(B,A))

mask_astig = CTF * (np.exp(1j*2*np.pi*astig))
mask_spherical = CTF * (np.exp(1j*2*np.pi*spherical))
mask_sphericalTEST = np.exp(1j * 2*np.pi * sphericalTEST) * CTFTEST
mask_astigTEST = np.exp(1j * 2* np.pi*astigTEST) * CTFTEST
mask_fieldCurvatureTEST = CTFTEST * fieldCurvatureTEST
mask_comaTEST = comaTEST * CTFTEST

kevinfft = fftshift(fft2(kevin[:,:,1]))
fft_mask = kevinfft*mask_spherical

fig, ax = plt.subplots(2,4)
ax[0,0].imshow(np.abs(kevinfft), norm=colors.LogNorm())
ax[0,1].imshow(np.abs(ifft2(CTF * kevinfft)))
ax[0,2].imshow(np.abs(fft_mask),norm=colors.LogNorm())
ax[0,3].imshow(np.abs(ifft2(fft_mask)))



him =  ax[1,0].imshow(np.angle(mask_sphericalTEST))
plt.colorbar(him, ax= ax[1,0])
ax[1,1].imshow(np.angle(mask_astigTEST))
ax[1,2].imshow((mask_fieldCurvatureTEST))
ax[1,3].imshow(np.abs(mask_comaTEST))


ax[1,0].set_title("Spherical")
ax[1,1].set_title("Astigmatism")
ax[1,2].set_title("Field Curvature")
ax[1,3].set_title("Coma")




plt.show()
