#Program to print Floyd's Triangle

row = int(input("Enter the Number of Rows: "))

n = 1
i = 0
while i < row:
    j = 0
    while j < i+1:
        print(n, end=" ")
        n = n+1
        j = j+1
    print()
    i = i+1
