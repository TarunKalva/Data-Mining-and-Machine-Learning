#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[16]:


df_math = pd.read_clipboard(header=None)


# In[20]:


df_science = pd.read_clipboard(header=None)


# In[26]:


df_reading = pd.read_clipboard(header=None)


# In[21]:


df_science.head()


# In[22]:


df_math.head()


# In[27]:


df_reading.head()


# In[28]:


df_math=df_math.rename(index=str, columns={0:"Rank",1:"Country",2:"Score"})


# In[29]:


df_science=df_science.rename(index=str,columns={0:"Rank",1:"Country",2:"Score"})


# In[30]:


df_reading=df_reading.rename(index=str,columns={0:"Rank",1:"Country",2:"Score"})


# In[31]:


temp = pd.merge(df_math,df_science,on='Country',how='outer')


# In[32]:


df = pd.merge(temp,df_reading,on='Country',how='outer')


# In[33]:


df.head()


# In[34]:


del df['Rank_x']


# In[35]:


del df['Rank_y']


# In[36]:


del df['Rank']


# In[37]:


df.head()


# In[38]:


df=df.rename(index=str,columns={"Score_x":"math_score","Score_y":"science_score","Score":"reading_score"})


# In[39]:


df.head()


# In[40]:


df=df.fillna(0)


# In[41]:


df['math_score']=df['math_score'].apply(int)


# In[42]:


df['science_score']=df['science_score'].apply(int)


# In[43]:


df['reading_score']=df['reading_score'].apply(int)


# In[44]:


df['Average']=(df['math_score']+df['science_score']+df['reading_score'])/3.0


# In[45]:


df.head()


# In[46]:


plt.hist(df['Average'],label='Average',color='r')
plt.hist(df['math_score'],label='Math_score',color='b')
plt.title('Programme for International Students Assessment')
plt.xlabel('Average and Math Score')
plt.ylabel('counts')
plt.legend()
plt.grid()
plt.show()


# In[64]:


def find_outlier(column):
    column_ls=[]
    mean=df[column].mean()
    std=df[column].std()
    for i in range(len(df[column])):
        value=df[column][i]
        
        if (abs(mean-value)>1.8*std):
            column_ls.append(df['Country'][i])          
    print('The outliers in',column,'are',column_ls)        


# In[66]:


column=input('Enter the column name: ')
if column not in df.columns:
    print('Invalid Column') 
else:    
    find_outlier(column)


# In[65]:


find_outlier('Average')
find_outlier('math_score')
find_outlier('science_score')
find_outlier('reading_score')


# In[ ]:




