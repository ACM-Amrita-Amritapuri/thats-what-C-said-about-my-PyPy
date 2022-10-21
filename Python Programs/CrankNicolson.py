# Importing the packages
import numpy as np
import matplotlib.pyplot as plt

# 4 decimal places precision
np.set_printoptions(suppress=True,precision=4)

# Given data
x0 = 0
xn = 10
t0 = 0
tn = 10
del_x = 2
del_t = 0.1
k = 0.835
lamb = (k*del_t)/(del_x**2)

# x and T arrays
int_nodes = int((xn-x0)/del_x)-1
x = np.arange(x0,xn+del_x,del_x)
T = np.zeros_like(x, dtype=float)

T[0] = 100
T[-1] = 50


# Creating array A
A = np.identity(int_nodes, dtype=float)
for i in range(int_nodes):
    A[i,i] = 2*(1+lamb)
    for j in range(int_nodes):
        if abs(i-j)==1:
            A[i,j] = -lamb
        
print(A)
t = t0

while(t<tn):
    B = np.zeros(int_nodes, dtype=float)
    
    # First and last node values
    B[0] = 2*lamb*T[0] + 2*(1-lamb)*T[1] + lamb*T[2]
    B[-1] = 2*lamb*T[-1] + 2*(1-lamb)*T[-2] + lamb*T[-3]
    
    
    # Interior node values
    for j in range(1,int_nodes-1):
        B[j] = lamb*T[i-1] + 2*(1-lamb)*T[i+1] + lamb*T[i+1]
        
    
    # Solving and plotting for matrix T 
    T[1:-1] = np.linalg.solve(A,B)

    plt.plot(x,T,color="orange")
    plt.pause(0.2)
    
    # Plot labelling
    plt.title("--Development of Temperature with Time--")
    plt.xlabel("Length of my rod (in cm)")
    plt.ylabel("Temperature of my rod (in \u2103)") #\u2103 -> Degree Celsius 
    t += del_t
