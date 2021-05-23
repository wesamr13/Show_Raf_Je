#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_excel(r'C:\Users\VAIO\Desktop\Rafidi Jewlery\Book 1.xlsx')
df = df.set_index('ID')
def show(x):
    return df.loc[x,:]    
    


# In[8]:


x = int(input())
show(x)


# In[3]:


df


# In[ ]:




