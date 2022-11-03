n = int(input('Please Enter Number '))
a=[]
b=[]
while n > 0:
    # check even and odd
    if n % 2 == 0:
        a.append(n)
    else:
        b.append(n)
    # decrease number by 1 in each iteration
    n = n - 1
print(a)
print(b)
