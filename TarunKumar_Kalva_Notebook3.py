#!/usr/bin/env python
# coding: utf-8

# ### Notebook 3 : Histogram of top words
# 
# Find the top frequently used words in the book of “Sense and Sensibility”. The book is in the sense_andsensibility.txt file.
# 
# The words should not be case sensitive, meaning “Mother” and “mother” are considered the same word.
# Replace all the punctuation marks with a space.
# Use the “stopwords.txt” file to remove all the stop words in text. (Do NOT modify the stopwords.txt file)
# Create a histogram similar to the “histogram.jpg” file. The diagram should contain the ranking, the top 30 words, the number of times they appeared in the book. The number of stars will be the number of appearance divided by 10. For example, “mother” appears 263 times; there are 26 stars displayed.  (You may not have the exactly the same result as in the histogram.jpg)

# In[16]:


# taking file names as iput
fname=input('Enter the file name: ')
f2name=input('Enter the stop words file name: ')
# creating list to hold the words
file1_ls=[]
file2_ls=[]
new_file_ls=[]
# punctuations string which is used to remove punctuations from file
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

f = open(fname, "r") #opening file in read mode so we cannot alter it
f2 = open(f2name,'r')
a_string = f.read() #reading the file 
a2_string = f2.read()

file_without_punctuation = ""
file2_without_punctuation = ""

# reading through the characters in a_string to check for punctuations and discard them if found
for char in a_string:
    if char not in punctuations:
        file_without_punctuation = file_without_punctuation + char#punctuation free text is added to file_without_punctuation str
        
        
for char in a2_string:
    if char not in punctuations:
        file2_without_punction = file2_without_punctuation + char

new_file = open("file_without_punctuation.txt", "w") #opening a new file in write mode
new_file.write(file_without_punctuation) # writing string to file.

new_file = open("file2_without_punctuation.txt","w")
new_file.write(file2_without_punctuation)

# opening the new files without punctuations
fhand=open("file_without_punctuation.txt")
fhand2=open("file2_without_punctuation.txt")
di=dict() #dictionary to hold key value pairs of words and their counts

for lin in fhand:
    lin=lin.rstrip() #stripping spaces in right side of line
    wds=lin.split() # splitting the line into words 
    for w in wds:
        file1_ls.extend(wds) #extend the words into file1.ls list 
#print(new_file_ls)        
    #for w in wds:
    #   w=w.lower()
    #    if w in di:
    #        di[w]+=1
    #    else:
    #        di[w]=1
#print(di['sense']) '''

#Sense_and_Sensibility.txt
#stopwords.txt


# In[17]:


#same procedure which we followed for processing words from strig to list with first file
for lin in fhand2:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
        file2_ls.extend(wds)


# In[18]:


#discard the words in first list file1_ls which contain in the second list file2_ls
for i in file1_ls:
    if i in file2_ls:
        continue
    else:
        new_file_ls.append(i)


# In[19]:


print(len(new_file_ls)) #printing the number of elements in new_file_ls which is after discarding the words from 
# running through the dictionary to count the number of words present in dictionary
for i in new_file_ls:
    i=i.lower() #eliminating case sensitivity by converting all words to small letters.
    if i in di:
        di[i]+=1 # incrementing count if words is present
    else:
        di[i]=1 #else assigning value 1 to word


# In[20]:


#printing the dictionary
for k,v in di.items():
    print(k,':',v)


# In[21]:


#sorting the dictionary based on values in descending order
#used lambda function to select value as parameter
sorted_dict = {key:val for key,val in sorted(di.items(), key= lambda x:x[1], reverse=True)}
print(sorted_dict)


# In[23]:


#printing the top 30 items and stars by taking scaling parameter as 10,000
i=0
for k,v in sorted_dict.items():
    if (i==30):
        break
    else:
        p=int(v/10000)
        print(i+1,':',k,'(',v,')','*'*p)
        i+=1


# In[ ]:




