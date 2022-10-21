####### Calculator #######

#Developer : Akhil S Kumar
#Date Created : 9/06/2019
#https://www.github.com/akhil-s-kumar

print("Hello friend, Can you introduce your name please? ")
name=input()
print('Hello', name, 'Tell me the operation you want to do?')
cont = "y" or "Y"
while cont.lower() == "y" or cont.upper() == "Y": 
 print("For addition press 1")
 print("For differnce press 2")
 print("For product press 3")
 print("For Division press 4")
 print("For power press 5")
 print("For remainder press 6")
 n=int(input("Enter your option: "))

 if n is 1:
  x=float(input("Enter the first number: "))
  y=float(input("Enter the second number: "))
  z=x+y
  print("The sum of the number is {0}".format(z))

 elif n is 2:
  x=float(input("Enter the first number: "))
  y=float(input("Enter the second number: "))
  z=x-y
  print("The difference of the number is {0}".format(z))

 elif n is 3:
  x=float(input("Enter the first number: "))
  y=float(input("Enter the second number: "))
  z=x*y
  print("The product of the number is {0}".format(z))

 elif n is 4:
  x=float(input("Enter the first number: "))
  y=float(input("Enter the second number: "))
  z=x/y
  print("The division of the number is {0}".format(z))

 elif n is 5:
  x=float(input("Enter the base number: "))
  y=float(input("Enter the power number: "))
  z=x**y
  print("The power of the number is {0}".format(z))
 elif n is 6:
  x=float(input("Enter the divident: "))
  y=float(input("Enter the divisor: "))
  z=x%y
  print("The remainder of the number is {0}".format(z))

 else:
  print("Press the correct operant")

 cont = input("Do you want to continue? (y/n)")
 if cont == "n":
    break