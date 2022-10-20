#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import pandas


# In[3]:


from pandas import read_csv
path='Assignment 1\data.csv'
data=read_csv(path)
print (data.shape)


# In[20]:


from pandas import read_csv
url='Assignment 1\data.csv'
data=read_csv(url)
colnames = ['diagnosis','radius_mean','perimeter_mean','area_mean']
print (data.shape)


# In[21]:


description = data.describe()
print(description)


# In[22]:


print(data.shape)


# In[23]:


print(data.head(4))


# In[32]:


out = []
for i in data['diagnosis']:
    if i == 'B':
        out.append(0)
    else:
        out.append(1)
data['outcome'] = out
print(data['outcome'])


# In[34]:


print(data.groupby('outcome').size())


# In[35]:


import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
scatter_matrix(data[['radius_mean','texture_mean']])
plt.show()


# In[38]:


Cdata = data.drop(["Unnamed: 32", "diagnosis"], axis = 1)
scatter_matrix(Cdata)
plt.show()   


# In[40]:


from sklearn.preprocessing import StandardScaler
arr=Cdata.values                    
X=arr[:,0:8]                     
Y=arr[:,8]                       
scaler=StandardScaler().fit(X)            
rescaledX=scaler.transform(X)  
numpy.set_printoptions(precision=3)
print(rescaledX[0:2,:])
print(X[0:2,:])


# In[ ]:




