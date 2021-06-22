import scipy.integrate as integrate
import numpy as np
import math
import matplotlib.pyplot as plt

def gaussian(x):
	return .1 * np.exp(-1  * x**2)
#discrete fourier transform of f(x) values.
def dft(fx):
	N = len(fx)
	n_row = np.linspace(0, N-1, N).reshape(1,N)
	n_col = n_row.reshape(N,1)
	a = np.exp(-2j * np.pi * n_row /N)
	a_large = np.repeat(a, repeats=N, axis=0)
	b = a_large ** n_col
	fx = fx.reshape(1,N)
	fx_row = np.repeat(fx, repeats=N, axis=0)
	B = fx_row * b
	fk = np.sum(B, axis=1)
	print(fk)
	return fk
#inverse discrete fourier transform of f(K) values
def dft_inverse(fk):
	N = len(fk)

	n_row = np.linspace(0, N-1, N).reshape(1,N)
	n_col = n_row.reshape(N,1)
	a = np.exp(-2j * np.pi * n_row /N)
	a_large = np.repeat(a, repeats=N, axis=0)
	b = a_large ** n_col
	fk = fk.reshape(1,N)
	fk_row = np.repeat(fk, repeats=N, axis=0)
	B = fk_row * b
	fx = np.sum(B, axis=1)
	return fx/N

#yet to implemented
def dft_inverse_mask(fk):
	N = len(fk)

	n_row = np.linspace(0, N-1, N).reshape(1,N)
	n_col = n_row.reshape(N,1)
	a = np.exp(-2j * np.pi * n_row /N)
	a_large = np.repeat(a, repeats=N, axis=0)
	b = a_large ** n_col
	fk = fk.reshape(1,N)
	fk_row = np.repeat(fk, repeats=N, axis=0)
	B = fk_row * b
	fx = np.sum(B, axis=1)
	return fx/N
#driver function for discrete fourier forward and reverse transform
#L: wavelength to be transformed (spatial/time domain is going from (-L/2, L/2)
#N: number of samples
#Note that L/N is going to be the sampling frequency. The frequency domain will have units of 
def shiftFunc(x,k_0):
	return np.exp(-2j * np.pi * x* k_0);
def runFourier(L,N, func):
	fs = N/L #sampling frequency
	func = np.vectorize(func)
	kval = np.linspace(-1/L, 1/L, N)
	xval = np.linspace(-L/2, L/2, N)
	yanalytic = func(xval)
	yshift = shiftFunc(xval,5*L)

	yfourier = dft(yanalytic)
	yfourier_shifted  = dft(yanalytic * yshift)
	yfourier_inverse = dft_inverse(yfourier)
	fig, ax= plt.subplots(4)
	ax[0].plot(xval, yanalytic,label="analytic")
	ax[1].plot(kval, np.abs(yfourier_shifted), 'g', label="fourier")
	ax[1].set(xlabel='x', ylabel='y',
	       title='Fourier transforms of Gaussian e^(-x^2)')
	ax[2].plot(xval, yfourier_inverse,label="inverse")
	ax[3].plot(xval, np.array([10+5j]*N),label="compl")

	plt.show()
	
runFourier(10,500, gaussian)
"""runFourier
   input: n = number of terms in fourier series
          wavelength = the period of the fourier series
          x_start = x position the graph should start at
          x_end = x position graph should end at
          func = function that the fourier series should expand on
   output: an nth order fourier series over f(x), plotted against f(x) via matplotlib
"""








