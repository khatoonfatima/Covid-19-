#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[41]:


data=pd.read_csv(r"C:\Users\khato\Downloads\covid19-in-italy\covid19_italy_region.csv")


# In[42]:


data.head()


# In[43]:


data.tail()


# In[44]:


data.columns


# In[45]:


data.describe() #It will describe the statistical values 


# In[46]:


data.isnull().sum()


# # Relating the variables with Scatterplot
# 

# In[51]:


sns.relplot(x='TestsPerformed', y='TotalPositiveCases',data=data)


# In[54]:


sns.relplot(x='NewPositiveCases', y='Recovered',data=data)


# In[59]:


data.columns


# In[62]:


sns.relplot(x='CurrentPositiveCases',y='HomeConfinement',kind='line',data=data)


# In[63]:


data.columns


# In[64]:


sns.catplot(x='Recovered',y='TotalPositiveCases',data=data)


# In[ ]:




