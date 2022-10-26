def Fibonacci(n):
    if n == 0:
        return 0
    elif n < 0:
        print("Incorrect input")
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print("Enter n: ")
num = int(input())
f = Fibonacci(num)
print("nth Fibonacci number is ",f)
