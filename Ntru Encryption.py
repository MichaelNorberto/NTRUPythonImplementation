from GoBetweenFile import *
userSelection = input("Would You Like to Generate a Public and Private Key Set, or Encrypt a Message (Generate/Encrypt)? ")

if (userSelection == 'Encrypt' or userSelection == 'encrypt' or userSelection == 'E' or userSelection == "e"):
    message = messageConversion()
    #M = polynomialMap(message)
    #R = randomPolynomial()
    #publicKey = input("Please enter the public key you wish to use for encryption" )
    #q = input("Please enter the value for q that you wish to use (this should belong to the publicKey entered above")
    #e = (R * publicKey + M) % q
elif (userSelection == 'Generate' or userSelection == 'generate' or userSelection == 'g' or userSelection == 'G':
    valueGenerate()
    #f = fGenerate()
    #g = gGenerate()
    #fp = invertModuloP(f)
    #fq = invertModuloQ(f)
    #h = (p * fq * g) % q
    #print("Your Public key is: ", h)
    #print("Your Private key is: ", fp)
   
    
