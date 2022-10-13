# Display Fibonacci Sequence up to n-th term

nterms = int(input("How many terms do you want?"))

n1, n2 = 0, 1

count = 0
if nterms <= 0:
    print("Please enter a positive integer.")

elif nterms == 1:
    print(f"Fibonacci Sequence up to {nterms} term: \n")
    print(n1)

else:
    print(f"Fibonacci Sequence up to {nterms} terms: \n")
    while count < nterms:
        print(n1)
        nth = n1 + n2 

        n1 = n2 
        n2 = nth 
        
        count +=1