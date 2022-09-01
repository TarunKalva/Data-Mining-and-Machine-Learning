#!/usr/bin/env python
# coding: utf-8

# # Polynomial Feature Selection Assignment 
# 

# In[1]:


#import packages
import time
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# ### 1. Import Data

# In[2]:


#Read in data from a data file to data_df in DateFrame format

## Type your code here to import data from poly_data.csv to data_df

data_df= pd.read_csv('poly_data.csv')



#verify the dataframe is imported correctly 
print(data_df.head(6))


# ### 2. Observe Data

# In[3]:


#joint plot (or scatter plot) of X1 and y
sns.jointplot(data_df['X1'], data_df['y'])


# In[4]:


#joint plot (or scatter plot) of X2 and y
sns.jointplot(data_df['X2'], data_df['y'])


# In[5]:


#joint plot (or scatter plot) of X1 and X2
sns.jointplot(data_df['X1'], data_df['X2'])


# ### Based on observing the above 3 diagrams and the p-values displayed, we found both X1 and X2 have close correlation with y. X1 and X2 are independent from each other. 

# ### 3. Split the Data

# In[6]:


# split the data into training and testing datasets
# the percentage of training data is 75%

#split point 
percentage_for_training = 0.75

#type your code here
#number of training data 
#########################################################
number_of_training_data = int(len(data_df)*percentage_for_training)
#########################################################


#create training and testing datasets
train_df  = data_df[0:number_of_training_data]
test_df = data_df[number_of_training_data:]
print(train_df.shape)
print(test_df.shape)


# ### 4. Create Polynomial Features

# In[7]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#set the degree to 3, you can try a larger number if you like
#for degree = 3, we will generate 9 features. 
#open the link below to understand what these features are 
#http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html  
polynomial_features = PolynomialFeatures(degree=3)


# In[8]:


X_poly = polynomial_features.fit_transform(data_df[['X1','X2']])

#type your code here to
#extract X for training and testing from the data frames
#########################################################
X_train = polynomial_features.fit_transform(train_df[['X1','X2']])
X_test =  polynomial_features.fit_transform(test_df[['X1','X2']])
#########################################################


# ### 5. Create and Train a Linear Regression Model

# In[9]:


# mse() calculates mean square error of a model on given X and y
def mse(X, y, model):
    return  ((y-model.predict(X))**2).sum()/y.shape[0]


# In[10]:


# use all the features to train the linear model 
lm = LinearRegression()
lm.fit(X_train, train_df['y'])
train_mse = mse(X_train, train_df['y'], lm)
print("Training Data Set's MSE is: \t", train_mse)
test_mse = mse(X_test, test_df['y'], lm)
print("Testing Data Set's MSE is : \t", test_mse)


# ### 6. Use Lasso in Linear Regression to Penalize Large Number of Features

# In[11]:


#import lasso
#lasso is controlled by a parameter alpha.
#by fine tuning this parameter, we can control the number of features

from sklearn.linear_model import Lasso
#Train the model, try different alpha values.
Lasso_model = Lasso(alpha=0.15,normalize=True, max_iter=1e5, )
Lasso_model.fit(X_train, train_df['y'])
        


# In[12]:


#see the trained parameters. Zero means the feature can be removed from the model
Lasso_model.coef_


# In[13]:


#let's see the train_mse and test_mse from Lasso when 
#alpha = 0.15

train_mse = mse(X_train, train_df['y'], Lasso_model)
print("Training Data Set's MSE is: \t", train_mse)
test_mse = mse(X_test, test_df['y'], Lasso_model)
print("Testing Data Set's MSE is : \t", test_mse)


# In[14]:


#let's try a large range of values for alpha first
#create 50 alphas from 100 to 0.00001 in logspace
alphas = np.logspace(2, -5, base=10, num=50)
alphas


# In[15]:


#use arrays to keep track of the MSE of each alpha used. 
train_mse_array =[]
test_mse_array=[]

#try each alpha
for alpha in alphas:
    
    #create Lasso model using alpha
    Lasso_model = Lasso(alpha=alpha,normalize=True, max_iter=1e5, )
    Lasso_model.fit(X_train, train_df['y'])
    
    #Calculate MSEs of train and test datasets 
    train_mse = mse(X_train, train_df['y'], Lasso_model)
    test_mse = mse(X_test, test_df['y'], Lasso_model)
    
    #add the MSEs to the arrays
    train_mse_array.append(train_mse)
    test_mse_array.append(test_mse)
    


# In[16]:


#plot the MSEs based on alpha values
#blue line is for training data
#red line is for the testing data
plt.plot(np.log10(alphas), train_mse_array)
plt.plot(np.log10(alphas), test_mse_array, color='r')


# ### There is something interesting between 0 and 1 in the above diagram. 0 mean 10^0=1 While 1 means 10^1 = 10  so, we will look closely within this range to find the optimal alpha value
# 

# In[17]:


# We can try a smaller search space now (a line space between 1 and 10)
alphas = np.linspace(1, 10, 1000)
train_mse_array =[]
test_mse_array=[]
dif_train_test=[]
### Type your code here 
## find train and test MSEs based on the alphas
## create the diagram below in which the blue line is train_mse_array
## the red line is test_mse_array
## Also, print out the alpha where the lines meet and the correponding 
## train_mse and test_mse
for alpha in alphas:
    
    Lasso_model = Lasso(alpha=alpha,normalize=True, max_iter=1e5, )
    Lasso_model.fit(X_train, train_df['y'])
    
    train_mse = mse(X_train, train_df['y'], Lasso_model)
    test_mse = mse(X_test, test_df['y'], Lasso_model)
    
    train_mse_array.append(train_mse)
    test_mse_array.append(test_mse)
    
    dif_train_test.append(abs(train_mse-test_mse))

#print(best_alpha,TRME, TEME)
index=dif_train_test.index(min(dif_train_test))
#print(train_mse_array[index],test_mse_array[index],alphas[index])
print('The optimal alpha is',alphas[index])
print('Train MSE is',train_mse_array[index])
print('Test MSE is',test_mse_array[index])
plt.plot(alphas, train_mse_array)
plt.plot(alphas, test_mse_array, color='r')
plt.grid()



# ### By observing a smaller range of alpha, we can clearly see how the MSEs change as we change the model and features. Use the diagram to explain the trends of the two lines and summarize what you learned so far. 

# In[18]:


## type your code here to describe the above diagram and what you learned 
## so far about feature and model selection ( about 200 words )

print("We can see that train mean square error and test mean square error change in opposite direction as the features are added because of underfitting and overfitting of model as the features increase the train data will try to fit every point in train data set and if we use that model with test data the mean square error increases as the model tries to fit that point which causes the increase in MSE, and the point where the MSEs of both the models meet can be defined as perfect model and the prediction can be accurate based on the model and here we used LASSO model where we should find the alpha value which is best suited to determine the perfect model and we got it as 3.5585585585585586 which avoids the overfitting or underfitting of model. Visualization part helps us to verify the results that we got pretty much easily and helps in identifying the perfect model easily, addition to that it is easily understood by people. In this module we have learnt how to do feature selection based on lasso model and how model is penalized as the features are added which results in overfitting of the model and we should be careful in underfitting the model which can happen due to penalization of Lasso model. One more concept that I learnt is about Bias and Variance tradeoff and in ideal situations bias and variance will be low but in real world one compromises another and we should be careful in selecting the model based on the requirements.")


# In[ ]:




