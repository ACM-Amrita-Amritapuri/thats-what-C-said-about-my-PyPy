
n=int(input("ENTER THE NUMBER : "))
num=n
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if n==rev:
    print("Number is a Palindrome")
else:
    print("Number is not a palindrome")
