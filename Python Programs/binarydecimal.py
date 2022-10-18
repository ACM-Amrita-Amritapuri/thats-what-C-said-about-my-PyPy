print("Enter the Decimal Number: ")
decimalnum = int(input())
i = 0
binarynum = []
while decimalnum!=0:
    rem = decimalnum%2
    binarynum.insert(i, rem)
    i = i+1
    decimalnum = int(decimalnum/2)

i = i-1
print("\nEquivalent Binary Value is:")
while i>=0:
    print(end=str(binarynum[i]))
    i = i-1
print()
