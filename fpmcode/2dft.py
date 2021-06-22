from skimage import data
import matplotlib.colors as colors
import numpy as np
import matplotlib.pyplot as plt

im_cameraman=data.camera()

fig,ax = plt.subplots()
x = np.arange(-256,256) #setting up the dimensions of the image. We want 512  by 512 pixels
X,Y = np.meshgrid(x,x) #X and Y are both 512x512 2-dimensional matries in which they can provide a coordinate of a 512x512 array
him = ax.imshow(np.abs(im_ft), origin="bottom",norm=colors.LogNorm(),extent = [-256,255,-256,255])
fig.colorbar(him)ls

