# Importing the packages
import numpy as np

# Array initialisation
A = np.array([[3,2,-1],
              [2,5,3],
              [-5,2,-1]], dtype=float)

B = np.array([8,9,0], dtype=float)

U = A.copy()
D = np.zeros_like(B)
X = np.zeros_like(B)

n = len(A)

L = np.identity(3, dtype=float)

# Defining a function to display the elements upto 4 decimal places
def d(A):
    print()
    for i in range(n):
        for j in range(n):
            print("%.4f"%A[i,j],end="\t\t")
        print()

print("\n\n")

# Forward Elimination Process
print("Forward Elimination Process: ")
print('\n')

for i in range(n-1): # 'i' specifies the pivot row
   
    for j in range(i+1,n): # 'j' specifies which row is being modified
   
       f = U[j,i]/U[i,i]   # 'f' is the multiplication factor
       
       
       L[j,i] = f          # Elements are filled below the principal diagonal of the Lower Triangular Matrix L
       
       for k in range(n):
           U[j,k] = U[j,k] - (f*U[i,k])  # 'k' specifies the column
           
 
# Display of matrix A and the decomposed matrices L and U
print("A =")
d(A)
print("\nU =")
d(U)
print("\nL =")
d(L)

# Verification of A = L x U
print("\n\nVerification of  A = L x U ")
P = np.matmul(L,U)
d(P)
print("\nA = ")
d(A)

# Solving for matrices D and X
D = np.linalg.solve(L,B)
X = np.linalg.solve(U,D)

# Solution matrices
print("\nD = ",D,end="\n\n")
print("Solution matrix is:\n",X)
