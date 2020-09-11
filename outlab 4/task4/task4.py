import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

def fn_plot1d(fn, x_min, x_max, filename):
	x = np.linspace(x_min, x_max, 100)
	y = fn(x)

	plt.plot(x, y)
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title(filename.split('.')[0])
	plt.savefig(filename)
	plt.close()

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
	x = np.linspace(x_min, x_max, 100)
	y = np.linspace(y_min, y_max, 100)

	X, Y = np.meshgrid(x, y)
	z = fn(X, Y)

	ax = plt.axes(projection="3d")
	ax.plot_surface(X, Y, z)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('f(x, y)')
	plt.title(filename.split('.')[0])
	plt.savefig(filename)
	plt.close()

def nth_derivative_plotter(fn, n, x_min, x_max, filename):
	x = np.linspace(x_min, x_max, 100)
	y = misc.derivative(fn, x, n=n)
	plt.plot(x, y)
	plt.xlabel('x')
	plt.ylabel('f<'+str(n)+'>(x)')
	plt.title(filename.split('.')[0])
	plt.savefig(filename)
	plt.close()

def h(x):
	return np.piecewise(x, [x > 0, x <= 0], [lambda x : np.exp(-1/(x**2)), 0])

def g(x):
	return h(2-x)/(h(2-x)+h(x-1))

def b(x):
	return g(np.abs(x))

def sinc(x, y):
	temp = np.sqrt(x**2+y**2)
	return np.piecewise(temp, [temp > 0, temp == 0], [lambda x: np.sin(x), 1])

fn_plot1d(b, -2, 2, 'fn1plot.png')
fn_plot2d(sinc, -1.5*np.pi, 1.5*np.pi, -1.5*np.pi, 1.5*np.pi, "fn2plot.png")
for i in range(1, 3):
	nth_derivative_plotter(b, i, -2, 2, "bd_"+str(i)+".png")