# Importing the packages
import numpy as np

# Array initialisation
    # Square brackets in the array syntax indicate the dimension of the array.
A = np.array([[3,2,-1],
              [2,5,3],
              [-5,2,-1]],dtype = float)
B = np.array([[8,9,0]],dtype = float)
X = np.zeros(3,dtype = float)

# Row echolon form - (concatenating the arrays)
M = np.concatenate((A,B.T),axis=1) #B.T -> B transpose

# Defining a function to display the elements upto 4 decimal places
def d(A):
    print()
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            print("%.4f"%A[i,j],end="\t\t")
        print()

# Original matrix in Reduced row echelon form    
d(M)  

# Forward Elimination Process
print("\n")
print("Forward Elimination Process:")
n = len(M) 
for i in range(n-1):  # 'i' specifies the pivot row
   
    for j in range(i+1,n):  # 'j' specifies which row is being modified
                            
       f = M[j,i]/M[i,i]  # 'f' is the multipliaction factor
       
       for k in range(n+1): # 'k' specifies the column
           M[j,k] = M[j,k] - (f*M[i,k])
           
# Displaying the modified matrix after each run of the outermost loop   
    d(M)
print("\n")    
# Back Substitution Process
print("Back Substitution Process:")
print("\n")

# Extracting matrices A and B from the matrix M
A = M[:,:-1]
B = M[:,-1]

# Calculating the last element of the solution matrix
X[-1] = B[-1]/A[-1,-1]

# Obtaining the final solution matrix 'X'
for i in range(n-2,-1,-1):
    s = 0
    for j in range(i+1,n):
        s += A[i,j]*X[j]
    
    X[i] = (B[i] - s)/A[i,i]
    
# Solution matrix
print("Solution Matrix is: ", X , sep="\n")
