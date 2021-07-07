import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2, ifftshift, fftshift
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.ndimage.filters import gaussian_filter


"""
kMeans2Cluster: performs a K-means cluster on a 1 dimensional array into 2 clusters

input:
    X: a 1 dimensional array 
output: 
    a 1 dimensional array consisting of 1's and 2's that delineate clusters 
    in which indices of 1's and 2's correspond to elements within X.
"""
def kMeans2Cluster(X):
    start = 0
    end = len(X)-1
    centroid_1 = np.random.choice(X)
    centroid_2 = np.random.choice(X)
    while(centroid_2 == centroid_1):
        centroid_2 = np.random.choice(X)
    newcentroid_1, newcentroid_2 = calcCentroid(X, centroid_1,centroid_2)
    while (newcentroid_1 != centroid_1 and newcentroid_2 != centroid_2):
        centroid_1 = newcentroid_1
        centroid_2 = newcentroid_2
        newcentroid_1,newcentroid_2 = calcCentroid(X, centroid_1,centroid_2)
    Y = np.zeros(len(X))
    for i in range(len(X)):
        dist_c1 = abs(X[i]-centroid_1)
        dist_c2 = abs(X[i] -centroid_2)
        if dist_c1 < dist_c2:
            Y[i] = 1
        else:
            Y[i] = 2
    return Y,newcentroid_1,newcentroid_2;

"""
helper function that calculates new centroid based off of previous centroids

X: input dataset
centroid_1: previous centroid 1
centroid_2: previous centroid 2
"""

def calcCentroid(X, centroid_1, centroid_2):
    y1 = []
    y2 = []
    for i in range(len(X)):
        dist_c1 = abs(X[i]-centroid_1)
        dist_c2 = abs(X[i] -centroid_2)
        if dist_c1 < dist_c2:
            y1.append(X[i])
        else:
            y2.append(X[i])
    c1 = np.mean(y1)
    c2 = np.mean(y2)
    return c1, c2
        

print(kMeans2Cluster([4.0, 4.1, 4.2, -50, 200.2, 200.4, 200.9, 80, 100, 102]))
        


