#Frog Jumping
a=int(input())
b=int(input())
k=int(input())
x=0
for i in range(k):
    if (i%2==1):
        x=x-b
    else:
        x=x+a
print(x)
    
