import sympy as sym
from sympy import GF
import secrets
import time

emptyString = ""
spaceString = " "

N = 503
p = 3
q = 251

#############################################################
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
binaryStr = []
testStr = emptyString.join(binString)
binaryStr.append(int(emptyString.join(binString)))
print("The binary is: ", spaceString.join(binString))
print("The length of the binary is: ", len(emptyString.join(binString)))
t1 = time.time()
total  = t1 - t0
print ("The total time to convert the message was: ", total, "s")

t2 = time.time()
mutatedList = []
mutationRate = 0.325
binaryStr = list(map(int, str(binaryStr[0])))
for integer in binaryStr:
    if secrets.SystemRandom().uniform(0.0000,1.0000) < mutationRate:
        integer = integer - (integer * 2)
        mutatedList.append(integer)
    else:
        mutatedList.append(integer)
print(mutatedList)
#############################################################
mutationRate = 0.4
fList = []
gList = []
rList = []
def generateF(N):
    for i in range (0,N):
        threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
        if threshold >= 0.5:
            if threshold <= mutationRate:
                fList.append(-1)
            fList.append(1)
        elif threshold < 0.5:
            if threshold <= mutationRate:
                fList.append(-1)
            fList.append(0)
    return fList

for i in range (0,N):
    threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
    if threshold >= 0.5:
        if threshold <= mutationRate:
            gList.append(-1)
        gList.append(1)
    elif threshold < 0.5:
        if threshold <= mutationRate:
            gList.append(-1)
        gList.append(0)

for i in range (0,N):
    threshold = secrets.SystemRandom().uniform(0.000000000,1.0000000)
    if threshold >= 0.5:
        if threshold <= mutationRate:
            rList.append(-1)
        rList.append(1)
    elif threshold < 0.5:
        if threshold <= mutationRate:
            rList.append(-1)
        rList.append(0)
#############################################################
def make_poly(N, coeffs):

    x = sym.Symbol('x')
    coeffs = list(reversed(coeffs))
    y = 0
    if len(coeffs) < N:
        for i in range(len(coeffs)):
            y += (x**i)*coeffs[i]
        y = sym.poly(y)
        return y
    else:
        for i in range(N):
            y += (x**i)*coeffs[i]
        y = sym.poly(y)
        return y

f = generateF(N)
g = gList
m = mutatedList
r = rList


f_poly = make_poly(N,f)
g_poly = make_poly(N,g)
m_poly = make_poly(N,m)
r_poly = make_poly(N,r)


x = sym.Symbol('x')

flag = 1
while flag == 1:
    try:
        Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric = False))
        break
    except ValueError:
        f = generateF(N)
        f_poly = make_poly(N,f)
        Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric = False))
        flag = 1

flag = 1
while flag == 1:
    try:
        Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric = False))
        break
    except ValueError:
        f = generateF(N)
        f_poly = make_poly(N,f)
        Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric = False))
        flag = 1
        
#Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric = False))
#Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric = False))

print('\nf =',f_poly)
print('\nFp =',Fp)
print('\nFq =',Fq)
print("\ng = ", g_poly)
print("\nr=", r_poly)
print("\nm=", m_poly)
print("\n===============================================")
h = p*((Fq.mul(g_poly)))

h = sym.polys.polytools.trunc(h, q)
#h = sym.polys.polytools.div(h, x**N -1)

print("\nPublic Key = ", h)

e = r_poly.mul(h) + m_poly
e = sym.polys.polytools.trunc(e, q)
print("\nThe Encrypted Message is: ", e)
t3 = time.time()
total = t3 - t2
print("\nTotal Encryption Time was: ", total, "s")
print("=========================================")
print("\nBeginning Decryption Process...")
t4 = time.time()
a = f_poly.mul(e)
a = sym.polys.polytools.trunc(a,q)
print("\na = ", a)
b = sym.polys.polytools.trunc(a,p)
print("\nb = ", b)
c = Fp.mul(b)
c = sym.polys.polytools.trunc(m_poly, p)
print("\nThe Original Message is: ", c)

decryptList = []
correctedList = []
decryptList = c.all_coeffs()
print("\n", decryptList)
for integer in decryptList:
    integer = abs(integer)
    correctedList.append(integer)

finalBinaryString = emptyString.join(str(n) for n in correctedList)
n = 7
asciiBinaryList = [finalBinaryString[i:i+n] for i in range(0, len(finalBinaryString), n)]
print("\n", asciiBinaryList)
asciiString = ""
for integer in asciiBinaryList:
    asciiVal = int(integer, 2)

    asciiCharacter = chr(asciiVal)

    asciiString += asciiCharacter

print("\nThe Original Message Was: ",asciiString)
t5 = time.time()
total = t5 - t4
print("\nThe Total Decryption Time was: ", total, "s")
