#!/usr/bin/env python
# coding: utf-8

# ## Scikit Learn Assignment

# In[1]:


#import the needed packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# read in app_usage data into vpn_df


vpn_df=pd.read_csv("app_usage.csv")


# In[3]:


#oberve the data
#RemoteAccess is the target, we will build a model that 
#takes all other columns as X to predict remote VPN usage

#look at the shape of the dataframe
print(vpn_df.shape)

#look at the column names
print(vpn_df.columns)

#show the first 5 records
print(vpn_df.head(5))


# In[4]:


#Visualize data

#1. See the distribtuion of Remote VPN Access


## Create a histogram of VPN usage close to the display below
## the answers may va                                  
#ax = sns.distplot(vpn_df['RemoteAccess'],kde=False)
#ax.set(xlabel='VPN Access',ylabel='Numbers')
plt.hist(vpn_df['RemoteAccess'],color='lightsteelblue')
plt.grid()
plt.xlabel('VPN Access')
plt.ylabel('Numbers')
plt.show()


# In[5]:


#2. See the correlation heat map


## Create a correlation heatmap close to the display below  
## the answers may vary                                  
corgrp=vpn_df.corr()
#print(corgrp['CRM'],corgrp['CloudDrive'])
f,ax = plt.subplots(figsize=(10,6))
sns.heatmap(corgrp,vmax=1,square=True,annot=True,cmap='coolwarm')
f.tight_layout()


# In[6]:


#We determine that this is supervised machine learning problem
#Linear Regression can be a good model
from sklearn import linear_model


# In[7]:


#The function takes X, y and retrun the trained model and R squared
def train_model(X,y):
    model = linear_model.LinearRegression()
    model.fit(X, y)
    R_2 = model.score(X,y)
    return model, R_2
#create a function to calculate Adjusted R_square
# n is the number of sample, p is the number features
def cal_adjusted_R(R_2, p, n):
    R_adjusted = R_2-(1-R_2)*(p/(n-p-1))
    return R_adjusted


# In[8]:


#R_2_array stores the R squared of all the features
R_2_array = np.array([])
#selected_columns=[]
#Calcuate the R_squared 
for col_name in vpn_df.columns:
    if col_name == 'RemoteAccess':
        continue
    else:    
        #selected_columns.append(col_name)
        # add your code here: 
        
        ## call the train_model() function to calculate R squared   ####
        X=vpn_df[[col_name]]
        y=vpn_df[['RemoteAccess']]
        model,R2=train_model(X,y)
        R_2_array = np.append(R_2_array,R2)
        print(col_name,': ',R2)
        
        #################################################################
      
        

################################################################
## sorted_R_2_index stores the index numbers of R_2_array   ####
## in descending order of the R_2 values                    ####        
sorted_R_2_index = np.argsort(R_2_array)[::-1]       
#################################################################


#print out the sorted indexes 
print("The order of index numbers are : \t", sorted_R_2_index)


# In[9]:


#gradually build up our model and add R squared and adjusted R to the output

for i in range(len(sorted_R_2_index)):
    
    #the selected_features should be the top i most associated features
    selected_features = []
    
    #take the top 1 to ith features as X
    for j in range(i+1):
        
            #append a new column based on the sorted R value
            #take your time to digist this line
            selected_features.append(vpn_df.columns[sorted_R_2_index[j]])
            
    #verify we got the right features
    print(selected_features)
    
    # X
    X_feature = vpn_df[selected_features]
    
    # y
    target = vpn_df[['RemoteAccess']]
    
    # train the model
    model, R_2 = train_model(X_feature, target)
    
    #calculate adjusted R
    R_adjusted = cal_adjusted_R(R_2, i+1, vpn_df.shape[0])
    
    #print the output
    print("R2: ", R_2, "\t Ajusted R2: ", R_adjusted, "\n")


# In[10]:


#let's build the model with all the features

y = vpn_df['RemoteAccess']
X = vpn_df.drop('RemoteAccess', 1)

from sklearn import linear_model

#create a linear regression model from linear_model package 
model=linear_model.LinearRegression()

#Train the model with our data (X, y)
model.fit(X,y)

#Display the parameters
print('Intercept: \n', model.intercept_)
print('Coefficients: \n', model.coef_)

#use R squared to see how much variation is explained by the trained model
print('R_squared: \n', model.score(X,y))


# In[11]:


# Should we reduce the number of features? 
from IPython.display import IFrame
IFrame('http://abbottanalytics.blogspot.com/2004/12/find-correlated-variables-prior-to.html', width=1200, height=300)


# In[12]:


# 1. after reading the above article, you decide to keep only one feature to represent 
# all the features that have correlation higher than 0.9 to it. 
##################################################################################
## modify the following code to remove the features you feel necessary
X = vpn_df.drop(['CloudDrive','ERP','ITOps','Webmail','Recruiting','HR1','OTHER'], 1)
# we manually removed the highly correlated features and less correlated features to target
#################################################################################

print(X)
# 2. we use Lasso to further penalize models with more features
from sklearn.linear_model import Lasso

# in Lasso, the score is still R squared 
best_score = 0

# Lasso has a parameter alpha used to adjust the level of penalizing the 
# number of features. A bigger alpha will produce less features. 
# We initiate the best alpha to 0 
best_alpha = 0 
R_2_list=[]
alpha_list=[]

# let's fine tune alpha to find the model we need 
for alpha in np.linspace(1,0.2, 1000):
    
    #create a linear regression (Lasso) model from linear_model package 
    model=Lasso(alpha=alpha,normalize=True, max_iter=1e5)

    #Train the model with our data (X, y)
    model.fit(X,y)
    R_2 = model.score(X,y)
    alpha_list.append(alpha)
    R_2_list.append(R_2)
    

   
    #Find a model that uses exactly 3 features. 
    #Output the score of this model (R squared) and   
    # corresponding alpha value. 
    
 
            
#print(alpha_list)
ind=R_2_list.index(max(R_2_list))
#print(R_2_list)
best_score=R_2_list[ind]
best_alpha=alpha_list[ind]
print("The best R of my 3-feature model is:\t\t", best_score)
print("The alpha I used in Lasso to find my model is: \t", best_alpha)

    #use R squared to see how much variation is explained by the trained model
    #print('R_squared: \n', model.score(X,y))


# ### Summarize how you eliminated some features. Which 3 features are in your model. Compare the R squared value of your model with one using all the features, explain why your model is a reasonably better model. 

# In[13]:


##### Write your summary here
print("My summary: I have eliminated the featutres based on highest correlation between the feautures and in my model we can see CRM has correlation values of 0.98,0.96,0.93 and 0.95 with CloudDrive, ERP, ITOps and Webmain so I used CRM to represent these features and removed them from data frame, now we are left with HR1, Expenses, HR2, OTHER and recruiting. In the remaining features HR1, OTHER and Recruiting and least correlated when compared to CRM, Expenses and HR2 and we can observe there is a decrease in Adjusted R2 value when these features are added. So, I've eliminated those and kept CRM, Expenses, HR2 as most significant features of my model. The R2 value I got for my 3 feature model is 0.999937 which explains the relation 99.9937% while the all feauture model has 0.93928 R2 value which explains 93.928% change in target and that is the reson why my model is better than all feature model.")
print("the 3 features in my model are: CRM, Expenses, HR2 ")

