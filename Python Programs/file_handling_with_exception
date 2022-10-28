n = int(input("Enter value for n: "))
name = input("Enter name of file / path")
lineCounter = 0
try:
 with open(name,'r') as f:
    for line in f:
        lineCounter += 1
        if lineCounter <= n:
            print(line, end='')
except FileNotFoundError as e:
    print(e)
except OSError as e: 
    print(e)
