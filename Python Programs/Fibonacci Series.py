#Program for Fibonacci series 
num=int(input("Enter any number :"))
n1=0
n2=1
sum=0
if num<=0:
 print("Please enter a number greater than zero.")
else:
 for i in range(0, num):
  print(sum, end=" ")
  n1=n2
  n2=sum
  sum=n1+n2
  

