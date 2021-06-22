import scipy.integrate as integrate
import numpy as np
import math
import matplotlib.pyplot as plt


def integrand(x):
	return x**2

def sin(x):
	return np.sin(x)
def an(x,n,lam, func):

	k = 2*math.pi / lam
	return func(x) * math.cos(n*k*x)

def bn(x,n,lam,func):

	k = 2*math.pi / lam
	return func(x) * math.sin(n*k*x)

def fourierSeries(n,lam, xval,func):
	origx = xval
	X = np.zeros(np.shape(xval))
	k = 2*math.pi / lam
	A0 = 2/lam * integrate.quad(func, 0, lam)[0]
	for i in range(1,n):
		A_n = 2/lam * integrate.quad(an, 0 ,lam, args=(i,lam, func))[0]
		B_n = 2/lam * integrate.quad(bn, 0 ,lam, args=(i,lam,func))[0]
		X = np.cos(origx * k * i) * A_n + np.sin(origx *k *i) * B_n + X
	return X + A0/2	

"""runFourier
   input: n = number of terms in fourier series
          wavelength = the period of the fourier series
          x_start = x position the graph should start at
          x_end = x position graph should end at
          func = function that the fourier series should expand on
   output: an nth order fourier series over f(x), plotted against f(x) via matplotlib
"""
def runFourier(n, wavelength, x_start, x_end, func):
	xval = np.linspace(x_start, x_end, 10000)
	yfourier = fourierSeries(n, wavelength, xval,func)
	yanalytic = func(xval)
	fig, ax= plt.subplots()
	ax.plot(xval, yfourier, label="fourier")
	ax.set(xlabel='x', ylabel='y',
	       title='Fourier Series of y=x^2')
	ax.plot(xval, yanalytic,label="analytic")

	ax.grid()
	ax.legend()


	plt.show()
runFourier(100, 20, 0, 20, integrand )







