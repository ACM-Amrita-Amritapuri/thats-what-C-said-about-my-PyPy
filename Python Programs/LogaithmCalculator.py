# Logarithmic calculator
import math

print("For natural log, press 1")
print("For log with base 2, press 2")
print("For log with base 10, press 3")
print("For other bases, press 4")

op=int(input("Enter selection: "))
n = float(input("Enter number: "))

if op==1:
    l = math.log(n)
    print ("Natural log of ",n," is ",l)
    
if op==2:
    l = math.log2(n)
    print ("log2(",n,") is ",l)
    
if op==3:
    l = math.log10(n)
    print ("log10(",n,") is ",l)
    
if op==4:
    base = int(input("Enter base value: "))
    l = math.log(n,base)
    print ("log base ",base,"of",n," is ",l)
    