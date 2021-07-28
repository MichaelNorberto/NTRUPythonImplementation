#Fetching Required Libraries
import secrets
import time

#Prime Checker for Extremely Large Numbers Using Miller-Rabin Primality Test
count = 0

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
    if n < 25205434148462237:
        return not any(tryComposite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17, 19))
    if n < 30060685970742138749:
        return not any(tryComposite(a, d, n, s) for a in(2,3,5,7,11,13,17,19,23))
    if n < 1075470776033649441998656802141:
        return not any(tryComposite(a, d, n, s) for a in(2,3,5,7,11,13,17,19,23,29,31,37))
    
    # otherwise
    return not any(tryComposite(a, d, n, s) 
                   for a in knownPrimes[:_precision_for_huge_n])
 
knownPrimes = [2, 3]
knownPrimes += [x for x in range(5, 1000, 2) if isPrime(x)]

t8 = time.time()
integerList = []
timeList = []
for i in range(1,20):
    t6 = time.time()
    flag = 1
    while (flag == 1):
            q = int(secrets.randbits(2048))
            if (isPrime(q) == False):
                    flag = 1
            else:
                    flag = 0
                    integerList.append(q)
    t7=time.time()
    total = t7 - t6
    timeList.append(total)
    average = (sum(timeList)) / (len(timeList))
    if flag == 0:
        count += 1
        print("The Prime Value Generated for q is: ",q, ", Generated in: ", total, "s")
        print(count, "numbers have been generated so far")
        
t9 = time.time()
runTotal = t9 - t8
print("The Total Runtime of this was: ", runTotal,"s")
def duplicateCheck(integerList):
    if len(integerList) == len(set(integerList)):
        return False
    else:
        return True
print(duplicateCheck(integerList))
print("The Average Generation time was: ", average)
