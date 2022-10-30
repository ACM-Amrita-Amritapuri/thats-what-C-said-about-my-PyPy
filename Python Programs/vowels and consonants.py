myvow=[]
mynonvow=[]
vowels = ['a','e','i','o','u']
n=input("enter a name or sentence:")
m=list(n.replace(" ","").lower())
for  i in range( len(m)):
    if m[i] in vowels:
        myvow.append(m[i])
    else:
        mynonvow.append(m[i])
print(set(myvow))
print(set(mynonvow))
