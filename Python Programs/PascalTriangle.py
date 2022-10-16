import math as m

def fac(n,x):
    form = int((m.factorial(n)/(m.factorial(x)*(m.factorial(n-x)))))
    return form

n = int(input('Enter the highest power of the expansion here: '))
for i in range(n+1):
    for j in range(n+1,i+1,-1):
        print(end='\t')
    for k in range(i+1):
        print(fac(i,k),end='\t\t' )
    print()
    
