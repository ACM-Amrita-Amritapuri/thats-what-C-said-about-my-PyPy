print("Enter number of terms n: ")
n = int(input())
n1, n2 = 1, 1
term = 0

if n <= 0:
    print("Incorrect input: Please enter a positive number")
    
elif n == 1:
    print("Fibonacci series upto ",n,"is",n1)

else:
    print("Fibonacci series upto ",n,"is:")
    while term < n:
       print(n1,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       term += 1