from pylab import figure, cm

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = 1.0 * x**5.0 + -1
    return y

x = np.arange(0.0, 3.0, 0.1)

y = function(x)

fig = figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')

plt.plot(x,y)

plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('y')

#plt.grid()

plt.savefig("function.png", bbox_inches='tight')

plt.show()

from scipy.optimize import minimize

x = np.arange(np.min(y),np.max(y),0.1)

y = np.zeros(x.shape)

def diff(x,a):
    yt = function(x)
    return (yt - a )**2

for idx,x_value in enumerate(x):
    res = minimize(diff, 1.0, args=(x_value), method='Nelder-Mead', tol=1e-6)
    y[idx] = res.x[0]

fig = figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')

plt.plot(x,y)

plt.title(r'$f^{-1}(x)$')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig("function_inverse.png", bbox_inches='tight')

plt.show()
