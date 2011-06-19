import numpy as np
import matplotlib.pyplot as plt
from functions import *
from ps10 import *

def myPlot(f, x):
	y = f(x)
	plt.plot(x, y)
	plt.show()


def plotPoly(f, x, x_p):
	y_p = interpolate(f, x, x_p)
	plt.plot(x_p, y_p)
	plt.show()



i = np.arange(0, 21)
x_equal = i/2.0 - 5
x_cos = 5 * np.cos(i*np.pi/20)

func = func5
x = x_equal

j = np.arange(0, 41)
x_p = j/4.0 - 5
myPlot(func, x_p)
plotPoly(func, x, x_p)


