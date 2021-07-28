from GoBetweenFile import *
userSelection = input("Would You Like to Generate a Public and Private Key Set, or Encrypt a Message (Generate/Encrypt)? ")

if (userSelection == 'Encrypt' or userSelection == 'encrypt' or userSelection == 'E' or userSelection == "e"):
    message = messageConversion()
    #M = polynomialMap(message)
    #R = randomPolynomial()
    userFile = input("Would you like to use a public key file (i.e. NTRUPublicKeyInformation.txt) (Y/N) ")
    if userFile == 'Y' or userFile == 'y' or userFile == 'yes' or userFile == 'yes'):
        with open("NTRUPublicKeyInformation.txt", "r+") as public:
            publicKey = public.readlines()
        public.close()
    else:
        publicKey = input("Please enter the public key you wish to use for encryption" )
    #q = input("Please enter the value for q that you wish to use (this should belong to the publicKey entered above")
    #e = (R * publicKey + M) % q

elif (userSelection == 'Generate' or userSelection == 'generate' or userSelection == 'g' or userSelection == 'G'):
    valueGenerate()
    #f = fGenerate()
    #g = gGenerate()
    #fp = invertModuloP(f)
    #fq = invertModuloQ(f)
    #h = (p * fq * g) % q
    print("Your Public key is: ", h)
    print("Your Private key is: ", fp)
    saveInfo = input("Would you like to save your keys and other values (Y/N)? ")
    separateFiles = input("Would you like to save your public key and private key into separate files (Y/N)? ")
      if ((saveInfo == 'Y' or saveInfo == 'y' or saveInfo == 'yes' or saveInfo == 'yes') and (separateFiles == 'N' or separateFiles == 'No' or separateFiles == 'n' or separateFiles == 'no')):
          print("Generating File ")
          with open("NTRUKeyInformation.txt", "w+" ) as f:
                f.write("Your Public Key is: " + h)
                f.write("\n")
                f.write("Your Private Key is: ", fp)
                f.write("\n")
                f.write("Your f Function is: ", f)
                f.write("\n")
                f.write("Your g Function is: ", g)
            f.close()
            print("Information Successfully Saved in File: NTRUKeyInformation.txt ")
    elif ((saveInfo == 'Y' or saveInfo == 'y' or saveInfo == 'yes' or saveInfo == 'yes') and (separateFiles == 'Y' or separateFiles == 'Yes' or separateFiles == 'y' or separateFiles == 'yes')):
        print("Generating Files ")
        with open("NTRUPublicKeyInformation.txt", "w+") as public:
            public.write("Your Public Key is: ", h)
        public.close()
        with open("NTRUPrivateKeyInformation.txt", "w+") as private:
            private.write("Your Private Key is: ", fp)
            private.write("\n")
            private.write("Your f Function is: ", f)
            private.write("\n")
            private.write("Your g Function is: ", g)
        private.close()
    else:
        break
            
          
          
   
    
