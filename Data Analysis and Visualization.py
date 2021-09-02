#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Libraries


# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import pandas_profiling as pp
import sweetviz as sv


# # DATA CLEANING STEPS

# In[ ]:


# THESE STEPS ARE DONE IN THE PREVIOUS NOTEBOOK


# In[2]:


data1 = pd.read_csv("C:/Users/saniyakhan/Downloads/data_clean.csv")


# In[3]:


data1


# In[4]:


data2 = data1.iloc[:,1:]


# In[5]:


data2


# In[6]:


data = data2.copy() 


# In[7]:


data


# In[8]:


data['Temp C'] = pd.to_numeric(data['Temp C'],errors = 'coerce')


# In[9]:


data.dtypes


# In[10]:


data['Month'] = pd.to_numeric(data['Month'],errors = 'coerce')


# In[11]:


data['Wind'] = data['Wind'].astype('int64')


# In[12]:


data.dtypes


# In[13]:


data[data.duplicated()].shape 


# In[14]:


data


# In[15]:


data[data.duplicated()] 


# In[16]:


data_cleaned1 = data.drop_duplicates()


# In[17]:


data_cleaned1


# In[18]:


data_cleaned2 = data_cleaned1.drop('Temp C',axis = 1)


# In[19]:


data_cleaned2


# In[20]:


data_cleaned3 = data_cleaned2.rename({'Solar.R': 'Solar'}, axis = 1)


# In[21]:


data_cleaned3


# In[ ]:


# HERE DATA CLEANING STEPS GETS OVER 


# # Treat Missing Values and Impute the Missing
# 

# # Heatmap

# In[22]:


cols = data_cleaned3.columns 
colours = ['#000099', '#ffff00'] 


# In[23]:


sns.heatmap(data_cleaned3[cols].isnull(),
            cmap=sns.color_palette(colours))


# In[24]:


data_cleaned3[data_cleaned3.isnull().any(axis=1)].head()


# In[25]:


data_cleaned3.isnull().sum()


# In[ ]:


# Mean Imputation


# In[26]:


mean = data_cleaned3['Ozone'].mean()
print(mean)


# In[ ]:


# Missing value imputation for categorical vlaue


# In[27]:


obj_columns = data_cleaned3[['Weather']]


# In[28]:


obj_columns.isnull().sum()


# In[29]:


# Missing value imputation for categorical vlaue


# In[30]:


obj_columns = obj_columns.fillna(obj_columns.mode().iloc[0])


# In[31]:


obj_columns.isnull().sum()


# In[32]:


data_cleaned3.shape


# In[33]:


obj_columns.shape


# In[34]:


data_cleaned4 = data_cleaned3.iloc[:,:7] 


# In[35]:


data_cleaned4.head() 


# In[36]:


data_cleaned4 = pd.concat([data_cleaned4,obj_columns],axis=1)


# In[37]:


data_cleaned4.shape


# In[38]:


data_cleaned4.head()


# In[39]:


data_cleaned4.isnull().sum()


# # Data Analysis and Visualization

# In[ ]:


# Import Library for Visualization


# In[40]:


import seaborn as sns


# In[ ]:


# Create the Default Pairplot


# In[41]:


sns.pairplot(data_cleaned3)


# In[ ]:


# Correlation


# In[42]:


data_cleaned3.corr()

