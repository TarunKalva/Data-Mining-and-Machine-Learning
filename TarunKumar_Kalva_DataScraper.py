#!/usr/bin/env python
# coding: utf-8

# In[1]:


#updated module 4 lectures and assignment

#Let's try BeautifulSoup library which is another solution for processing data from HTML pages. It has extended capacity of
#reganizing HTML tags and extracting data between tags
from bs4 import BeautifulSoup

#BeautifulSoup usually works with request package hand-in-hand. Requests will open a website as a channel as opening a file 
#for processing. 
import requests

#The following page contains the system vulnerabilities reported by NATIONAL VULNERABILITY DATABASE
#Let's take the content of the page out for processing
#https://nvd.nist.gov/vuln/search 

# convert string to time
# reference: https://docs.python.org/2/library/datetime.html  
from datetime import datetime as dt


# In[2]:


# Let's observe the url formation and create a query  

#Ask user to type in a search term
#Reference : https://www.w3schools.com/python/python_user_input.asp 
#Reference: https://docs.python.org/2/library/datetime.html  


##################################################
##################################################
###### Complete the code here ####################

#Ask user to input a search term, e.g. "splunk"
search_term = input("Enter a Search term:")

#Ask user to type in a minimum severity , e.g. "7.4"
min_severity = float(input('Type in a minimum severity value:'))

#Ask user to type in a start date in a predefined format, e.g. "10-02-2017"
start_date = dt.strptime(input('Type in a start publish date (MM-DD-YYYY):'),'%m-%d-%Y')

#Ask user to type in an end date in a predefined format, e.g. "12-31-2018"
end_date = dt.strptime(input('Type in a end publish date (MM-DD-YYYY):'),'%m-%d-%Y')

#Don't forget to convert the input strings to the right date types that will be used
#by the rest of the program.



##################################################
##################################################


# In[3]:


#let's explore the result based on the query
url = 'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query='+search_term+'&search_type=all&startIndex=0'

# Request content from web page
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'lxml')


#Observe the content of soup 
#print(soup)


# In[4]:


# Use a browser to open or download the page
# I used firebug, a FireFox/chrome plug in to analyze the page tag structure
# locate the division where the table is located in


#find the total number of the result 
total = soup.find('strong', {"data-testid": "vuln-matching-records-count"})

#show the number of results
#calculate the number of pages of the result. The default page layout is 20 results per page
##################################################
##################################################
###### Complete the code here ####################

#remove the comma: reference https://www.w3schools.com/python/ref_string_replace.asp

total=int(str(total.text))
n=total//20
if total%20 == 0:
    pages = n
else:
    pages = n+1
print('The search returned',total,'results. Use the following criteria to refine your search.')
print('There are',pages,'pages')
##################################################
##################################################



# In[5]:


#the next step is to extract data out from the query
#and store the data in variables or save them as a datafile or in a database
#We will store them in variables for now 


#create lists to store retrieved data

#vulnerability IDs
vul_ids =[]

#vulnerability summaries
summaries=[]

#severity levels
severities = []

#publish dates 
publish_dates = []

#the urls of individual vulnerbility description pages
#we don't see them from the survey page yet
urls = []






# In[6]:


# go throught the pages and populate the lists 
start_index=0
for page in range(pages):
    
    ##################################################
    ##################################################
    ###### Complete the code here ####################
    
    i=0
    
    url = 'https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query='+search_term+'&search_type=all&startIndex='+str(start_index)
    
    print('We are on page #'+str(page+1))
    
    print(url)
    
    response = requests.get(url)
    
    content = response.content
    
    soup = BeautifulSoup(content,'lxml')
    
    table = soup.find('table',{'data-testid':'vuln-results-table'})
    
    rows = table.findAll('tr')

    #in each row
    for tr in rows[1:]: #from 2nd row
        
        vul_ids.append(tr.find('th').text) #we retrieve vulnerability name
        
        summaries.append(tr.find('p').text) #we retrieve the discription of vulnerability
        
        if str(tr.find('em').text[0:-1])=='V3.x': #based on condition find whether severity is available or not
            
            severities.append(10.0) # if not available assign 10.0
            
        else:    
            #retrieving original severity score
            severities.append(float(tr.find('a',{'data-testid':'vuln-cvss3-link-'+str(i)}).text[0:3]))
        #stripping the date based on format    
        date=dt.strptime((tr.find('span',{'data-testid':'vuln-published-on-'+str(i)}).text[0:-9]),'%B %d, %Y; %I:%M:%S')
        #appending the converted date to publish_dates list
        publish_dates.append(date.strftime('%m-%d-%Y'))
        
        i+=1
        #taking the urls and append them to urls list
        urls.append('https://nvd.nist.gov'+tr.find('a')['href'])
        
    start_index+=20 #used to traverse through pages

  
        
        
        # some results may not contain a severity score
        # They show "not available" as the output
        # Find a way to bypass it. For example:
        # If the score is not available, assign the score to be 10
        # otherwise, take the real score

    ##################################################
    ##################################################


# In[7]:


##################################################
##################################################
###### Complete the code here ####################
count=1 # counter to count obtained results
for i in range(len(vul_ids)): #looping through the range of values available in lists
    if severities[i]>min_severity: # comparing if severity is greater than inputted severity value
        #comparing if the date is between the date range provided
        if start_date <= dt.strptime(publish_dates[i],'%m-%d-%Y') <= end_date: 
            #printing the required values
            print('No.',count)
            print('Vul_ID:',vul_ids[i])
            print('Severity:',severities[i])
            print('Publish Date:',publish_dates[i])
            print('For more information, visit',urls[i])
            print('-'*100)
            count+=1 #incrementing the counter
#Show the result in the format as in the sample answer below


            
##################################################
##################################################


# In[ ]:




