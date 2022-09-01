#!/usr/bin/env python
# coding: utf-8

# # Find the minimum of a function f(x)
# 
# ### The model should automatically set the optimal learning rate gamma
# 
# 
# 
# 
# ### Find the minimum of 
# ## $$f(x) = x^4+200*(x+2000)^2+10000 $$  <br><br><br>

# In[1]:


#import python packages
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#define the x's range for plotting
x=np.arange(-120, 80, 0.1)


# In[3]:


#define f(x) based on the function 
def f(x): 
    return (x**4)+200*((x+2000)**2)+10000


# In[4]:


#plot x vs. f(x)
plt.plot(x,f(x))


# ### We can see that the minimun is between f(-50) and f(-100)

# In[5]:


#define the derivative of f(x) over x ---> f'(x)
def derivative(x):
    return 4*(x**3)+400*(x+2000)
    


# In[6]:


#define a function to find the minimum of f(x) 
def find_optimum(x_old,x_new,gamma,precisions):
    #store each update in x_search
    x_search = [x_new]

    
    #keep searchhing until the values converge within the precision
    
    #Type your code after "whhile"
    while abs(x_new-x_old) > precisions :   
        #use x_old to keep the x value before the update
        x_old = x_new
        
        #update x_new
        # Type your code after x_new =
        x_new = x_old - gamma*derivative(x_old)  
            
        #record the udpates
        x_search.append(x_new)
    
    #print out the result and plot the decreasing trend of f(x) vs iternations
    # Type your code here (multiple lines)
    print(len(x_search),'iterations')
    print('The local minimum occurs at',x_new)
    print('gamma =',gamma)
    x_search_array=np.array(x_search)
    plt.plot(x_search_array,f(x_search_array))


# In[7]:


#Test the find_optimum() function with the following parameters


x_old = 70 # This value doesn't matter, it's just a init value
x_new = 50 # This value doesn't matter
gamma = 0.000001  #the learning rate is critial, but we have to guess a value now
precision = 1e-12 #the precision decides when to stop the search
find_optimum(x_old,x_new,gamma,precision)  #call the function 


# In[8]:


#create a find_optimum function to automatically set gamma based on 
#t is the decrease rate of gamma

def adaptive_optimum(x_old, x_new, gamma, t, precision):
    
    #nextIter is the flag for continuing or stopping the loop
    nextIter = True
    
    #keep searching until nextIter is set to false
    while nextIter:
        
        #decrease the value of gamma in each iteration
        gamma *=t
        
        #create a local copy of x_old and x_new in each iteration
        #it's because we can want any change to x_new and x_old to 
        #affect the calculation in the next iternation 
        x_old_try = x_old 
        x_new_try = x_new 
        
        #try 10000 times to see if x converges
        for i in range(10000):
            #use x_old_try to keep the value of x before the update
            x_old_try = x_new_try          
            
            try:
                x_new_try= x_old_try - gamma * derivative(x_old_try)
                if (abs(x_new_try - x_old_try)< precision):
                    nextIter = False
                    print('Found gamma:',gamma)
                    print('The minimum is at :  x=',x_new_try)
                    print('The minimum of f(x) is :',f(x_new_try))
                    break
            # if there is an error, such as "value too large" error, stop the
            # iternation and try next gamma
            except:  
                #gamma=t*gamma
                break 


# In[9]:


x_old = 70 # This value does not matter 
x_new = 50 # This value does not matter either

#the precision is set to be very high
precision = 1e-12

#decrease rate of gamma
t=0.9

#we can start with a large positive gamma close to 1
gamma = 1

#call the function
adaptive_optimum(x_old, x_new, gamma, t, precision)


# In[ ]:




