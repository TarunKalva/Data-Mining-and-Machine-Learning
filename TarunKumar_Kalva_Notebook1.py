#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1: Prime Numbers
# Write a Jupyter Notebook to find the 9991th to 10000th prime numbers.
# Display the numbers to the notebook
# Output the numbers to a data file called prime.txt.
# Demonstrate that you used “continue” and “break” to improve efficiency and explain why

# In[39]:


# function definition to check prime number and return True if it is prime or return false
# 1 is considered neither prime nor composite
def isprime(num):
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False


# In[45]:


n= int(input('Enter the nth prime number require: '))
j=1 #used as numbers to reach the inputted range
i=0 #used as counter which counts number of primes
while i<n:
    if isprime(j)==True:
        #print(j)
        if i==n-1:
            break #used break so that loop breaks when counter equals entered number thus improving effeciency
        else:
            j+=1
        i+=1 # incrementing when the number is prime
    else:
        j+=1
#print(j)
fhand=open('prime.txt','a') #opening a prime.txt file in append mode
fhand.write('\n'+str(j)) #writing to file prime.txt
fhand.close()


# In[ ]:
