num = int(input("Enter the Decimal Number: "))
i = 0
n = []
while num!=0:
    rem = num%2
    n.insert(i, rem)
    i = i+1
    num = int(num/2)

i = i-1
print("\nEquivalent Binary Value is:")
while i>=0:
    print(end=str(n[i]))
    i = i-1
print()
