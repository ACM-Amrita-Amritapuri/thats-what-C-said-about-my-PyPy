#Conditional Statement Questions
# 1) Number Guessing Game
import random
print("Number Guessing name")
flag=1
a=(random.randint(0,10))
x=int(input("Enter a Number"))
if a>x:
      print("Number is greater than",x);
elif a<x:
      print("Number is less than",x);
else:
      print("You Won")
      flag=0
if flag==1:    
   y=int(input("Enter a Number"))
   if a>y:
      print("Number is greater than",y);
   elif a<y :
      print("Number is less than",y);
   else:
      print("You Won")
      flag=0
if flag==1:    
  z=int(input("Enter a Number"))
  if a>z:
      print("Number is greater than",z);
  elif a<z :
      print("Number is less than",z);
  else:
      print("You Won")
      flag=0
if flag==1:    
  b=int(input("Enter a Number"))
  if b>a:
      print("Number is greater than",b);
  elif b<a :
      print("Number is less than",b);
  else:
      print("You Won")
      flag=0
    
if(flag==1):
 print("System Won . Number was ",a)

      
