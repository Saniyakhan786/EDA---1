#!/usr/bin/env python
# coding: utf-8

# # install new libraries

# In[1]:


get_ipython().system('pip install pandas_profiling')
get_ipython().system('pip install sweetviz')


# In[2]:


# Import the libraries
import pandas as pd
import numpy as np
import pandas_profiling as pp
import sweetviz as sv


# In[4]:


# import dataset
data1 = pd.read_csv("C:/Users/saniyakhan/Downloads/data_clean.csv")


# In[5]:


data1


# In[6]:


data1.head()


# In[7]:


data1.tail()


# In[8]:


type(data1)             # it will show Data Structure


# In[10]:


data1.shape             # it will show number of rows and columns


# In[11]:


data1.dtypes             # it will show data type for columns


# # Data Type Conversion

# In[12]:


data1.info()                # it will show data types and extra counts


# In[13]:


data1


# In[14]:


data2 = data1.iloc[:,1:]          # to get rid of column(Unnamed:0)


# In[15]:


data2


# In[16]:


data = data2.copy()      # The method .copy() is used here so that any changes made in new DataFrame, 
                         # don't get reflected in the original one


# In[17]:


data                     # new data frame


# In[ ]:


# we will use method errors = Coerce to treat columns where data type was assigned as object due to ambiguity in data


# In[21]:


data['Temp C'] = pd.to_numeric(data['Temp C'],errors = 'coerce')     


# In[22]:


data.dtypes


# In[23]:


data['Month'] = pd.to_numeric(data['Month'],errors = 'coerce') 


# In[24]:


data.dtypes


# In[26]:


data['Wind'] = data['Wind'].astype('int64')      # to change the data type


# In[27]:


data.dtypes


# # Duplicates

# In[28]:


data[data.duplicated()].shape        # count of duplicated rows


# In[29]:


data


# In[30]:


data[data.duplicated()]                # it will print the duplicated rows


# In[32]:


data_cleaned1 = data.drop_duplicates()       # it will dro duplicate rows


# In[33]:


data_cleaned1


# In[34]:


data_cleaned1.shape


# # Drop Columns

# In[35]:


data_cleaned2 = data_cleaned1.drop('Temp C',axis = 1)


# In[36]:


data_cleaned2


# # Rename the columns

# In[37]:


data_cleaned3 = data_cleaned2.rename({'Solar.R': 'Solar'}, axis = 1)


# In[38]:


data_cleaned3


# # Outlier Detectcion

# In[39]:


data_cleaned3['Ozone'].hist()            # Histogram of Ozone


# In[40]:


data_cleaned3.boxplot(column = ['Ozone'])           # Box plot


# In[41]:


data_cleaned3['Ozone'].describe()                  # Descriptive Statistics


# In[42]:


data['Weather'].value_counts().plot.bar()           # Bar Plot


# In[ ]:




