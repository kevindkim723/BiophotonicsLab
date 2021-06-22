# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:04:58 2021

@author: HMCBiophotonicsLab
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.io as sio

data_mat = 'input_data_USAF.mat'
data_mat_norm = os.path.normpath(data_mat)
data = sio.loadmat(data_mat_norm)

# Save dictionary elements to variables for easier manipulation
NAshift_x = data['NAshift_x'][0] # x component of NA shift of the illumination (+ means to the right in k space)
NAshift_y = data['NAshift_y'][0] # y component of NA shift of the illumination (+ means to down in k space)
NA = data['NA'][0][0]
wlen = data['wlength'][0][0]

k0 = 2*np.pi/wlen
r = NA*k0 # cutoff frequency

kx = NAshift_x*k0
ky = NAshift_y*k0

fig, ax = plt.subplots(1,1)
ax.axis('equal')
#him = ax.plot(kx, ky, 'bo')
xloc = np.tan(np.arcsin(-NAshift_x)) * 56
yloc = np.tan(np.arcsin(-NAshift_y)) * 56

him = ax.plot(xloc, yloc, 'bo')
ax.set_xlabel('kx')
ax.set_ylabel('ky')
plt.show()

for i in range(len(NAshift_x)): #len(NAshift_x)
    xloc = kx[i]
    #ax.add_patch(circle1)

    

# find intersection between two circles
a = np.pi*(r**2)
c = kx[2] - kx[1] #dist between centers
q = 2*np.arccos(c/(2*r))
a_int = (r**2)*(q - np.sin(q))
print('area of circle =', a)
print('area of intersection =', a_int)
print('percent overlap =', a_int/a)
