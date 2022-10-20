#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import pandas
myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['a','b']
colnames = ['f1','f2','f3']
mydataframe = pandas.DataFrame(myarray, index = rownames, columns = colnames)
print(mydataframe)


# In[2]:


myarray = numpy.array([['a','sandhya',9.6],[4,'shreya',6.5]])
rownames = ['r1','r2']
colnames=['f1','f2','f3']
mydataframe = pandas.DataFrame(myarray, index = rownames, columns=colnames)
print(mydataframe)


# In[4]:


from pandas import read_csv
path='Assignment 1\diabetes.csv'
data=read_csv(path)
print (data.shape)


# In[5]:


from pandas import read_csv
url='Assignment 1\diabetes.csv'
data=read_csv(url)
colnames=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
print (data.shape)


# In[6]:


description = data.describe()
print(description)


# In[7]:


print(data.shape)


# In[8]:


print(data.head(4))


# In[10]:


print(data.groupby('Outcome').size())


# In[11]:


import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
scatter_matrix(data[['Pregnancies','Glucose']])
plt.show()


# In[12]:


scatter_matrix(data)      
plt.show()
data.hist()                       
plt.show()    


# In[13]:


from sklearn.preprocessing import StandardScaler
arr=data.values                    
X=arr[:,0:8]                     
Y=arr[:,8]                       
scaler=StandardScaler().fit(X)            
rescaledX=scaler.transform(X)  
numpy.set_printoptions(precision=3)
print(rescaledX[0:2,:])
print(X[0:2,:])


# In[14]:


myarray=numpy.array([1,3,-10,4,5,7,-4,-2,10])
mydataframe = pandas.DataFrame(myarray)
print(mydataframe)


# In[15]:


mydataframe.plot(kind='bar')
plt.show()


# In[16]:


from sklearn import preprocessing
fl_x=mydataframe.values.astype(float)

#fl_x=mydataframe[['f1']].values.astype(float)   #If specific feature name is to be converted 

min_max_scaler=preprocessing.MinMaxScaler()
X_scaled=min_max_scaler.fit_transform(fl_x)
df_normalized=pandas.DataFrame(X_scaled)
print(df_normalized)
df_normalized.plot(kind='bar')
plt.show()


# In[ ]:




