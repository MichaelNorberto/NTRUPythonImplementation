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
        print(binString)
        binaryStr = []
        testStr = emptyString.join(binString)
        print(testStr.split)
        binaryStr.append(int(emptyString.join(binString)))
        print(binaryStr)
        print("The binary is: ", spaceString.join(binString))
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

        binaryStr = list(map(int, str(binaryStr[0])))
        print(binaryStr)
        binaryStr = np.squeeze(binaryStr)
        p = np.poly1d(binaryStr)
        print(np.poly1d(p))
        print("The polynomial Evaluated at x = 2 is: ", p(2))
        x = int(p(2))
        print("This polynomial is a ",p.order,"th order polynomial")

        q = 7
        y = pow(x, -1, q)
        print(y)
#############################################################
messageConversion()
