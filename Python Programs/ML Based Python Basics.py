#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[144]:


#1. Create two vectors using numpy and check how many values are equal in in the two vectors
import numpy as np
a = np.array ([1,6,7,9])
b = np.array([1,0,6,9])
np.sum(a == b)


# In[158]:


#2. Matrix creation using numpy
#a. Create a matrix M with 10 rows and 3 columns and populate with random values. 
import random
M = np.random.randint(10, size = (10,3))
print(M)

#b. Print size of M.
print(M.shape)

#c. Print only number of rows of M
print(M.shape[0])

#d. Print only number of columns of M
print(M.shape[1])

#e. Write a simple loop to modify third column as follows:
#If sum of first two columns is divisible by 4, Y should be 1 else 0. 
for i in range(10):
    if np.sum(M[i,0:2])%4 == 0:
        M[i,2:3] = 1
    else:
        M[i,2:3] = 0
M


# In[159]:


#3. Create a pandas dataframe ‘df’ from the created matrix M and name the columns as X1, X2 and Y
import pandas as pd
col = ['X1','X2','Y']
df = pd.DataFrame(M, None, col)
df


# In[160]:


#4. Plot X1 and X2 using scatter plot. Color (X1,X2) red if corresponding Y is 1 else blue
import matplotlib.pyplot as plt
col = df.Y.map({0:'b', 1:'r'}) 
df.plot.scatter(x='X1', y='X2', c=col)
plt.show()


# In[161]:


#5. a. For two columns X1, X2, find squared error : (x1 – x2)^2
MSE = np.square(np.subtract(df['X1'],df['X2']))
print(MSE)

# b. Find sum of the squared error
TSE = np.sum(MSE)
print(TSE)


# In[162]:


#6. Find euclidean distance between first two rows of matrix M.
#Compare result with inbuilt function numpy.linalg.norm(a-b) where a is first row and b is second row.
from numpy import linalg as LA
a = df['X1'][0:2]
b = df['X2'][0:2]
LA.norm(a - b)


# In[179]:


#Create a vector V with two random values.
#Find the Euclidean distance between each row of M with V.
#Store the distance in a vector and print
v = np.random.rand(3)
v
f = np.array([])
for i in range(10):
    a = df.iloc[i]
    b = v
    d = LA.norm(a - b)
    f = np.append(f,d)
print(f)


# In[174]:


#8. Manipulate matrix
#Create a matrix A with 10 rows and 2 columns.
#Add a new column to a matrix. (Use np.column_stack)
#Add a new row to a matrix(Use np.vstack)
A = np.random.randint(10,size = (10,2))
C = np.random.randint(10,size = (10,1))
B = np.random.randint(10,size = (1,3))
A = np.column_stack((A,C))
print(A)
A = np.vstack((A,B))
A


# In[182]:


#9. Create a matrix M’ with two columns X1’, X2’ and populate with random values.
#Find the Euclidean distance between each row of M’ with each row of M
#Store the distance in a matrix Dist with 3 columns. First column is the row id of M, second column is the row id of M’, and the third column is distance value

M1 = np.random.randint(10, size = (10,2))
dist = np.empty((0,3))
print(dist)
for i in range(10):
    for j in range(10):
        row = np.array([i,j,np.linalg.norm(M[i,:2]-M1[j,:2])]);dist = np.vstack((dist,row))
dist


# In[185]:


#10. Sort Dist matrix based on last column.
#Use(print(a[a[:,n].argsort()])) where a is the matrix and n is the column based on which you need to sort
from sklearn.metrics.pairwise import euclidean_distances
euclidean_distances(M[:,:2], M1)
dist = dist[dist[:,2].argsort()]
dist


# In[187]:


#11. Get initial k rows from sorted matrix
k = int(input('Enter the k value - '))
dist[0:k,:]


# In[188]:


#12. Find the number of 1s and number of 0s in k rows found above. Print 1 if the number of 1s are more else print 0.
count_1 = np.count_nonzero(dist[0:k,:] == 1)
count_0 = np.count_nonzero(dist[0:k,:] == 0)
1 if count_1 > count_0 else 0


# In[ ]:




