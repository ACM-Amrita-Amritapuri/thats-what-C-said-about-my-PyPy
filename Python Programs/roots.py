import math
def roots( a, b, c): 
    d = b * b - 4 * a * c
    if d == 0: 
        print("Real and same roots") 
        print('x1,x2 = '+str(-b / (2 * a)))
    elif d > 0: 
        d=math.sqrt(d)
        print("Real and different roots ") 
        print('x1 = '+str((-b + d)/(2 * a))) 
        print('x2 = '+str((-b - d)/(2 * a))) 
    else:
        d=math.sqrt(abs(d))
        print("Complex roots") 
        print('x1 = '+str(complex(- b / (2 * a), d/ (2 * a))))
        print('x2 = '+str(complex(- b / (2 * a), -d/ (2 * a))))
  
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
if a!=0:
    roots(a, b, c)