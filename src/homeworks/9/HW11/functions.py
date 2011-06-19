import numpy as np
def func1(x):
	y = 1 - (1.0/2) * np.power(x, 1) + (1.0/4) * np.power(x, 2) - (1.0/8) * np.power(x, 3) + (1.0/16) * np.power(x, 4)
	return y

def func2(x):
	y = np.exp(0.5 * x)
	return y

def func3(x):
	y = np.sin(x)
	return y

def func4(x):
	y = np.exp(0.5 * x) * np.sin(2*x)
	return y

def func5(x):
	y = 1/(1 + np.power(x, 2))
	return y

