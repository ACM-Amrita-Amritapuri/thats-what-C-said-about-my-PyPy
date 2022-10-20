# Factorial using recursion


def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

num = 5

if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of",num,"is",factorial(num))
