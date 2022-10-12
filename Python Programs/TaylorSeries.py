def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

def taylorseries(x, n):
    if n == 0:
        return 1
    else:
        return ((x ** n) / fact(n)) + taylorseries(x, n - 1)

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
print("The Taylor series is: ", taylorseries(x, n))