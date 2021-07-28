# Group 4
# Python Implementation of the NTRU Algorithm
# Decryption File
# Sponsor: Yossi Har-Nov
#############################################################
# Importing the GoBetweenFile for utilities and information
from GoBetweenFile import *
#############################################################
userPrivateKey = input("Would you like to pull your MasterKey information file in to decrypt a message? ")

if userPrivateKey == 'Yes' or userPrivateKey == 'Y' or userPrivateKey == 'yes' or userPrivateKey == 'y':
    with open("NTRUKeyInformation.txt", "r+") as file:
        keys = file.readlines()
    file.close()
    e = input("Please Enter the Message You Wish to Decrypt With Your Private Key ")
    #a = (f * e) % q
    #b = a % p
    #M =(fq * b) % p
    #decryptedMessage = reverseConversion()
    #print("The Original Message was: ", decryptedMessage)
else:
    fq = input("Please Enter Your Private Key")
    encryptedMessage = input("Please Enter the Message You Wish to Decrypt With Your Private Key ")
    #a = (f * e) % q
    #b = a % p
    #M =(fq * b) % p
    #decryptedMessage = reverseConversion()
    #print("The Original Message was: ", decryptedMessage)
