f=open("rosalind_ini5.txt","r")
x=f.readlines()
for i in range (len(x)):
    if i%2==1:
        print(x[i].strip("\n"))