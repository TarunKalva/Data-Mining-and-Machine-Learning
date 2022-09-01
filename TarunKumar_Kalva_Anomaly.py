#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #importing numpy package as np


# In[2]:


fhand = open("anomaly_detection.txt") #opening the file
text=fhand.readlines() #reads one line at a time


# In[3]:


data_list=[] #initialising the list
for i in text:
    wds=i.split() #splitting with whitespaces
    data_list.extend(wds) #extending the words to list


# In[4]:


data_list_float = [float(i) for i in data_list] #converting the strings to float values
#print(data_list_float)


# In[5]:


data_array=np.array(data_list_float) #converting the list to numpy array
#print(data_array)


# In[6]:


#defining anomaly function
def anomaly(data_array):
    flag=1 #it is used to control the iterations of while loop
    data_array.sort() #sortiing the array 
    while flag == 1:
        flag=0 #changing the control to zero so that we can run the while loop when anomaly is found and run for updated array
        #run through the array 
        for i in range(len(data_array)):
            l_array=data_array[0:i] # takes elements left side of the indexed element
            r_array=data_array[i+1:] # takes elements right side of the indexed element excluding indexed element
            ex_array = np.concatenate((l_array,r_array)) # concatenate two arrays which doesn't have indexed element
            std_array=np.std(ex_array) # standard deviation of the concatenated list
            mean_array=np.mean(ex_array) # mean of the concatenated list
            #compare if difference of indexed element and mean is greater than 3 times of standard deviation
            if(abs(data_array[i]-mean_array)>std_array*3):
                print('Remove',data_array[i],'from the list because its',abs(data_array[i]-mean_array)/std_array,'times of standard deviation of the list without it.')
                print(data_array[i],'is removed from the list!')
                # remove the indexed element from the data_array and update the data_array with new data array
                data_array = np.delete(data_array,i)
                # change the flag to 1 so that we can check for anomalies again
                flag=1
                print(' '*50)
                #break the loop once we delete the element
                break
    print('No more anomaly is detected!') # No more anomalies are detected as there aren't any anomalies detected.


# In[7]:


# calling anomaly function passing data_array and print anomalies if found.
anomaly(data_array)


# In[ ]:




