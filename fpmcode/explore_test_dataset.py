# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.io as sio

data_mat = 'test_dataset.mat'
data_mat_norm = os.path.normpath(data_mat)
data = sio.loadmat(data_mat_norm)

# Save dictionary elements to variables for easier manipulation
imseqlow = data['imseqlow'] #sequence of low resolution images (225 images, each 128x128 in size)
NA = data['NA'][0][0]
wlen = data['wlength'][0][0]

LED_x = data['LED_x'][0]
LED_y = data['LED_y'][0]

# calculate kx and ky vectors
LEDheight = 56
LEDgap = 4
arraysize = 15
k0 = 2*np.pi/wlen

r = NA*k0 # cutoff frequency

fig, ax = plt.subplots(1,1)
ax.axis('equal')
ax.set_xlabel('kx')
ax.set_ylabel('ky')

kx = []
ky = []

#print(LED_x)
for i in range(len(LED_x)):
    x_loc = LED_x[i] - (arraysize//2)
    print(x_loc * LEDgap)
#    print(x_loc)
    y_loc = LED_y[i] - (arraysize//2)
    kx_rel = -np.sin(np.arctan((x_loc*LEDgap)/LEDheight))
    ky_rel = -np.sin(np.arctan((y_loc*LEDgap)/LEDheight))
    kx_i = k0*kx_rel; ky_i = k0*ky_rel
    ax.plot(kx_i, ky_i, 'bo')
    kx.append(kx_i); ky.append(ky_i)
    circle1 = plt.Circle((kx_i, ky_i), r, facecolor = 'none', edgecolor = 'blue')
    #ax.add_patch(circle1)
    
ax.plot(kx,ky,'bo')
# find intersection between two circles
a = np.pi*(r**2)
c = kx[1] - kx[0] #dist between centers
q = 2*np.arccos(abs(c)/(2*r))
a_int = (r**2)*(q - np.sin(q))
print('area of circle =', a)
print('area of intersection =', a_int)
print('percent overlap =', a_int/a)
plt.show()
