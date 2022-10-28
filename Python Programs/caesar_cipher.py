#Caesar Cipher
n=int(input("Enter shifting nubmer n "))
cipher=list(map(str,input("Enter the text").split()))
for i in range (0 , len(cipher)):
    a=cipher[i]
    b=ord(a)
    print(b)
    if(b==120):
        c= 97+n-3
        cipher[i]=chr(c)
    elif(b==121):
        c= 97+n-2
        cipher[i]=chr(c)
    elif(b==122):
        c= 97+n-1
        cipher[i]=chr(c)
    elif(a=='.'):
        cipher[i]="."
    else:
        b=ord(a)+n
        cipher[i]=chr(b)
print(cipher)    
        
