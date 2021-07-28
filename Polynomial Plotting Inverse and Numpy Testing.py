# Group 4
# Python Implementation of the NTRU Algorithm
# Decryption File
# Sponsor: Yossi Har-Nov
#############################################################
# Importing libraries for testing purposes
from scipy.optimize import minimize
from pylab import figure, cm
import numpy as np
import matplotlib.pyplot as plt
import secrets
import time

emptyString = ""
spaceString = " "
#############################################################
def messageConversion():
    yOrN = 'Y'
    while yOrN == 'Y' or yOrN == 'y' or yOrN == 'yes' or yOrN == 'Yes':
        #Getting User Input
        plaintext = input("Please Enter a Message for Encryption ")

        #Initalizing Timing
        t0 = time.time()

        #ASCII Conversion
        asciiString = []
        for character in plaintext:
            asciiString.append((ord(character)))

        #Binary Conversion
        binString = []
        for integer in asciiString:
            binString.append(bin(integer).replace("0b", ""))
        ###########################################################################
        #Printing Output 
        print(asciiString)
        print("The binary is: ", spaceString.join(binString))
        binaryStr = []
        binaryStr = binaryStr.append(emptyString.join(binString))
        print("The length of the binary is: ", len(emptyString.join(binString)))
        t1 = time.time()
        total  = t1 - t0
        print ("The total time to encrypt the message was: ", total, "s")

        #Converting Original Message 
        textString = []
        for integer in asciiString:
            textString.append((chr(integer)))
        print("Original Message was: ", emptyString.join(textString), "\n")
        yOrN = input("Would you like to enter another message (Y/N)? ")

        p = np.poly1d([binaryStr])
        print(np.poly1d(p))
        print("The polynomial Evaluated at x = 2 is: ", p(2))
        print("This polynomial is a ",p.order,"th order polynomial")
#############################################################
messageConversion()
#############################################################
# Testing Poly1d to see how it works
p = np.poly1d([binaryStr])
print(np.poly1d(p))
print("The polynomial Evaluated at x = 2 is: ", p(2))
print("This polynomial is a ",p.order,"th order polynomial")
#############################################################

# Playing with graphing and finding polynomial inverse
def function(x):
    y = 1.0 * x**5.0 + 2.0 * x**2.0 + -1.0
    return y

x = np.arange(0.0, 3.0, 0.1)

y = function(x)

plotFig = figure(num = None, figsize =(12,10), dpi=80, facecolor = 'w', edgecolor = 'k')
plt.plot(x,y)
plt.title('Function f(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
#############################################################
# Finding the inverse of the above function
x = np.arange(np.min(y), np.max(y),0.1)

y = np.zeros(x.shape)

def diff(x, a):
    yt = function(x)
    return (yt - a)**2

for idx, x_value in enumerate(x):
    res = minimize(diff, 1.0, args=(x_value), method = 'Nelder-Mead', tol=1e-6)
    y[idx] = res.x[0]

fig = figure(num = None, figsize =(12,10), dpi=80, facecolor = 'w', edgecolor = 'k')

plt.plot(x,y)

plt.title(r'$f^{-1}(x)$')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
