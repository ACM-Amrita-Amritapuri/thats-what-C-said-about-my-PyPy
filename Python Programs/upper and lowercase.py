countu,countl = 0,0
s1=input("enter a sentence:")
for i in range (len(s1)):
    if s1[i].isupper():
             countu+=1
    elif s1[i].islower():
        countl+=1
print(countu, countl)
