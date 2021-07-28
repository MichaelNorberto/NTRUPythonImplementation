#  Implementation of Quantum-Safe Encryption in Software
#   Group 4 Engineering Design 2
#   Professor: Hanqi Zhuang
#   Sponsor: Yossi Har-Nov

#Fetching Required Libraries
import secrets
import time
###########################################################################
emptyString = ""
spaceString = " "
###########################################################################
#Prime Checker for Extremely Large Numbers Using Miller-Rabin Primality Test
def tryComposite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def isPrime(n, _precision_for_huge_n=16):
    if n in knownPrimes:
        return True
    if any((n % p) == 0 for p in knownPrimes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(tryComposite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))

    # otherwise
    return not any(tryComposite(a, d, n, s) 
                   for a in knownPrimes[:_precision_for_huge_n])
 
knownPrimes = [2, 3]
knownPrimes += [x for x in range(5, 1000, 2) if isPrime(x)]
###########################################################################
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
###########################################################################    
def valueGenerate():
    #Generating Cryptographically Secure Prime Value for N
    t2 = time.time()
    flag = 1
    while (flag == 1):
            N = int(secrets.randbits(1171))
            if (isPrime(N) == False):
                    flag = 1
            else:
                    flag = 0   
    t3=time.time()
    total = t3 - t2
    if flag == 0:
        print("The Prime Value Generated for N is: ",N, ". Generated in: ", total, "s")
###########################################################################
    #Generating Cryptographically Secure Prime Value for p
    t4 = time.time()
    flag = 1
    while (flag == 1):
            p = int(secrets.randbits(3))
            if (isPrime(p) == False):
                    flag = 1
            else:
                    flag = 0   
    t5=time.time()
    total = t5 - t4
    if flag == 0:
        print("The Prime Value Generated for p is: ",p,". Generated in: ", total, "s")
###########################################################################
    #Generating Cryptographically Secure Prime Value for q
    t6 = time.time()
    flag = 1
    while (flag == 1):
            q = int(secrets.randbits(2048))
            if (isPrime(q) == False):
                    flag = 1
            else:
                    flag = 0   
    t7=time.time()
    total = t7 - t6
    if flag == 0:
        print("The Prime Value Generated for q is: ",q, ", Generated in: ", total, "s")
###########################################################################
messageConversion()
valueGenerate()
########################################################################### 
########################################################################### 
########################################################################### 
#Generating Cryptographically Secure Values of N
##t2 = time.time()
##
##flag = 1
##while (flag == 1):
##    num =  int(secrets.randbits(25))
##    for i in range (2, num):
##        if (num % i) == 0:
##            flag = 1
##            break
##    else:
##            flag = 0
##t3 = time.time()
##
##total = t3-t2
##if (flag == 0):
##    N = num
##    print("N is: ", N, "The to Generate N was, ",total, "s")
##
###Generating Cryptographically Secure Values of p
##t4 = time.time()
##flag = 1
##while (flag == 1):
##    num =  int(secrets.randbits(15))
##    for i in range (2, num):
##        if (num % i) == 0:
##            flag = 1
##            break
##    else:
##            flag = 0
##t5 = time.time()
##
##total = t5-t4
##if (flag == 0):
##    p = num
##    print("p is: ", p, "The to Generate p was, ",total, "s")    
##
###Generating Cryptographically Secure Values of q
##t6 = time.time()
##flag = 1
##while (flag == 1):
##    num =  int(secrets.randbits(25))
##    for i in range (2, num):
##        if (num % i) == 0:
##            flag = 1
##            break
##    else:
##            flag = 0
##t7 = time.time()
##
##total = t7-t6
##if (flag == 0):
##    q = num
##    print("q is : ", q, "The to Generate q was, ",total, "s") 


###########################################################################    
# Function to convert Decimal number
# to Binary number
##def decimalToBinary(n):
##    return bin(n).replace("0b", "")

##   
### Driver code
##if __name__ == '__main__':
##    yOrN = 'Y'
##    while yOrN == 'Y' or yOrN == 'y' or yOrN == 'yes' or yOrN == 'Yes':
##        userVal = int(input("Enter a Value for Conversion: "))
##        convertedVal = decimalToBinary(userVal)
##        print(decimalToBinary(userVal))
##        print(int(convertedVal, 2))
##        yOrN = input("Would You Like to Enter Another Value? ")
