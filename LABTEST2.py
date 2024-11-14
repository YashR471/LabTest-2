#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
data=load_boston()
df=pd.DataFrame(data.data,columns=data.feature_names)
print(df)


# In[18]:


print(data.feature_names)


# In[29]:


print(df.mean())


# In[23]:


print(df.min())


# In[24]:


print(df.max())


# In[34]:




