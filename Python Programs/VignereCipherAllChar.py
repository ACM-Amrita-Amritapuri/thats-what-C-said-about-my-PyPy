import math
import random
import string
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '
    ,'1','2','3','4','5','6','7','8','9','0','~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','\\'
    ,'|','[',']','{','}','"',"'",';',':','/','?','.',',','>','<']
message = input("Enter the message to encrypt: ")
# message = message.lower()
inp = int(input("1) User input key\n2) random key\n>>> "))
if inp == 1:
    key = input("Enter the Key for encryption: ")
elif inp ==2:
    key = ''.join([random.choice(string.ascii_lowercase) for i in range(math.floor(len(message)/4))])
else:
    print("Wrong input")
    raise Exception("Either Give input 1 or 2")
def pseudokey():
    pseudokey.temp1 = []
    message1 = list(message)
    key1 = list(key)
    i = 0
    j = 0
    pseudokey.key = []
    while i < (len(message1)):
        pseudokey.key.append(key1[j])
        j = j+1
        i = i+1
        if j > len(key)-1:
            j = 0
    pseudokey.key = ''.join(map(str, pseudokey.key))
    for i1 in range(len(pseudokey.key)):
        pseudokey.temp1.append(alphabets.index(pseudokey.key[i1]))
pseudokey()
message = list(message)
temp = []
for j in range(len(message)):
    temp.append(alphabets.index(message[j]))
class encryptclass():
    def __init__(self):
        self.temp = []
        self.temp2 = []
        self.encrypt = []
        self.decrypt =[]
        self.decrypttemp = []
    def encryption(self):
        for x in range(len(temp)):
            self.temp.append((temp[x]+pseudokey.temp1[x])%95)
        for x1 in range(len(self.temp)):
            self.encrypt.append(alphabets[self.temp[x1]])
        self.encrypt1 = ''.join(map(str,self.encrypt))
        print("Ciphertext is : \n",self.encrypt1)
class decryptclass(encryptclass):
    def decryption(self):
        for y in range(len(self.temp)):
            self.decrypttemp.append(alphabets.index(self.encrypt[y]))
            self.temp2.append((self.decrypttemp[y]-pseudokey.temp1[y])%95)
        for y1 in range(len(self.temp2)):
            self.decrypt.append(alphabets[self.temp2[y1]])
        self.decrypt = ''.join(map(str, self.decrypt))
        print("Plaintext is : \n",self.decrypt)

Vignerecipher = decryptclass()
Vignerecipher.encryption()
dec = int(input("Press '0' to decrypt: "))
if dec == 0:
    Vignerecipher.decryption()
else:
    raise Exception("Use right key to decrypt...")


""" Here by this implementation we can encrypt every char including numbers, space, and even symbols too """