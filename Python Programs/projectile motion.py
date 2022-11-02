import math
import matplotlib.pyplot as plt
V0=float(input("Enter the value of velocity initial: "))
g=9.8
delta_t=0.01
theta=[30,35,40,45,50,55,60]


for i in theta:
    V0x=V0*(math.cos(math.radians(i)))
    V0y=V0*(math.sin(math.radians(i)))
    X=[]
    Vy=[]
    Y=[]
    x=0
    y=0
    X.append(x)
    Y.append(y)
    while(y>=0):
        V0y=V0y-(g*delta_t)
        y=y+(V0y*delta_t)
        x=x+(V0x*delta_t)
        X.append(x)
        Y.append(y)
    plt.plot(X,Y)
    plt.xlabel("x direction")
    plt.ylabel("y direction")
plt.show()
