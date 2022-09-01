#!/usr/bin/env python
# coding: utf-8

# # Most effected countries due to covid 19

# ## Abstract
# In this project I'm going to show the most effected or severely effected countries due to covid-19 based on deaths in a country and GDP reduction happened in that particular year. Here first we are going to get data from Kaggle about the statistics of total cases, deaths, deaths/100 cases and so on for different countries and the GDP reduction data from global economic data and then we are going to take that data in dataframes and process it to find the most effected countries and then visusalize the data to show the top 5 countries which are most effected and percentage they occupy in the effectiveness percent in those top 5 effected countries.  

# ## Introduction
# covid-19 has been challenging situation for every country across the world and it is continuing to be even with the development of vaccines and taking precautions, we have lost so many lives in this pandemic which is our important parameter and countries got effected worstly as there is reduction of gross domestic product in entire world and we are going to take that as reference and find out which is most effected country due to the pandemic.

# ## Data Collection/Cleaning/Processing

# In[1]:


#importing required packages 
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[3]:


# Reading data from csv files that we've acquired from references mentioned below
df_people_data = pd.read_csv('country_wise_latest.csv')
df_gdp_data = pd.read_csv('GDP_reduction_countrywise.csv')


# In[4]:


# Renaming the columns in dataframe
df_people_data = df_people_data.rename(index=str,columns={'Country/Region':'Country'})


# In[5]:


df_people_data


# In[6]:


# sorting the values based on country name
df_gdp_data_sort_country = df_gdp_data.sort_values(by='Country')


# In[7]:


# dropping the duplicates in country column
df_gdp_data_sort_country = df_gdp_data_sort_country.drop_duplicates(subset=['Country'])


# In[8]:


df_gdp_data_sort_country


# For our analysis we only need the Deaths/100 cases, Deaths/100 recovered in df_people data and 2020 year in df_gdp

# In[9]:


# taking only required columns into another dataframe
df_people_data_required = df_people_data[['Country','Confirmed','Deaths','Deaths / 100 Cases','Deaths / 100 Recovered']]


# In[10]:


df_people_data_required


# In[11]:


df_gdp_data_sort_country_required = df_gdp_data_sort_country[['Country','2020']]


# In[12]:


# resetting the index for smoothening the process of analysis
df_gdp_data_sort_country_required = df_gdp_data_sort_country_required.reset_index()


# In[13]:


# dropping the index column as we have the new index
df_gdp_data_sort_country_required = df_gdp_data_sort_country_required.drop('index',axis=1)


# In[14]:


df_gdp_data_sort_country_required


# In[15]:


# merge the dataframes into one based on the column "country"
df_combined= pd.merge(df_people_data_required,df_gdp_data_sort_country_required,on=['Country'],how='inner')


# In[16]:


df_combined


# In[17]:


# filling out empty columns with 0
df_combined = df_combined.fillna(0)


# In[18]:


# renaming the 2020 index to gdp_reduction
df_combined = df_combined.rename(index=str,columns={'2020':'gdp_reduction'})


# In[19]:


# inversing the values in the gdp_reduction column for the basis of our analysis
df_combined['gdp_reduction'] = -df_combined['gdp_reduction']


# In[20]:


df_combined


# In[21]:


#df_combined.loc[df_combined['Deaths / 100 Cases']==min(df_combined['Deaths / 100 Cases'])]


# In[22]:


# plotting the scatter plot to see the density of the values which helps in our analysis
plt.scatter(df_combined['Country'],df_combined['Deaths / 100 Cases'])
plt.scatter(df_combined['Country'],df_combined['gdp_reduction'])
plt.grid()


# In[23]:


# we are taking the columns which we feel that are important for our analysis
df_combined_required = df_combined[['Country','Deaths / 100 Cases','gdp_reduction']]


# In[24]:


# We take Deaths/100 Cases and gdp_reduction as our measure to find most effected countries as the all countries
# have different population densities and geographic features. We are going to normalize the values on a scale of 
# 0 to 1, 1 being the highest and 0 being the lowest 
df_combined_required['Deaths / 100 Cases'] = df_combined_required['Deaths / 100 Cases']/max(df_combined_required['Deaths / 100 Cases'])
df_combined_required['gdp_reduction'] = df_combined_required['gdp_reduction']/max(df_combined_required['gdp_reduction'])


# In[25]:


df_combined_required


# In[26]:


max(df_combined_required['Deaths / 100 Cases'])


# In[27]:


# now the values are normalized, so we can take the percentage and create other column to add the calculated value
# I'm going to 60% of Deaths and 40% of gdp_reduction to provide more importance to life rather than economy
df_combined_required['effected_value'] = 0.6*df_combined_required['Deaths / 100 Cases']+0.4*df_combined_required['gdp_reduction']


# In[28]:


df_combined_required


# In[29]:


# least affected country is printed out here
print('The least affected country is')
df_combined_required.loc[df_combined_required['effected_value']==min(df_combined_required['effected_value'])]['Country']


# In[30]:


# most affected country is printed out here
print('The most affected country is')
df_combined_required.loc[df_combined_required['effected_value']==max(df_combined_required['effected_value'])]['Country']


# In[31]:


# assigning ranks to the country based on the effected value in descending order
df_combined_required['Ranking'] = df_combined_required['effected_value'].rank(ascending=0)


# In[32]:


# sorting the values based on ranking
df_combined_final = df_combined_required.sort_values('Ranking')


# In[33]:


df_combined_final.head()


# In[34]:


df_combined_final.tail()


# # Visualization
# Research Question - Which country has been effected by covid-19 the most and what factor played a major role for it's situation?
# Hypothesis - We can see that Yemen and Libya are severely affected countries but the deaths and cases are very low when compared to the next in the list which are United Kingdom, Italy and Belgium where cases, deaths, economic crisis has been severe and this is because Yemen, Libya are developing and small countries which often get unnotioced to the world. However covid-19 has spread like wildfire across the globe it is important to consider data from all the countries and provide medical or financial support to the ones needed.

# In[35]:


# Here we are extracting the top 5 countries which got most affected
Deaths_ls=[]
Country_ls=[]
gdp_ls=[]
dp100c=[]
ev=[]
for i in df_combined_final.head()['Country']:
    Deaths_ls.append(int(df_combined.loc[df_combined['Country']==i]['Deaths']))
    Country_ls.append(df_combined.loc[df_combined['Country']==i]['Country'])
    gdp_ls.append(float(df_combined.loc[df_combined['Country']==i]['gdp_reduction']))
    dp100c.append(float(df_combined.loc[df_combined['Country']==i]['Deaths / 100 Cases']))
    ev.append(float(df_combined_final.loc[df_combined_final['Country']==i]['effected_value']))


# In[36]:


# Printing out the values to verify
print(Deaths_ls)
coun_ls=list(np.concatenate(np.array(Country_ls)))
print(coun_ls)
print(gdp_ls)
print(dp100c)
print(ev)


# In[37]:


# thid function is used to return the percentage occupied by specific country in our pie chart
def values(val):
    return val


# In[38]:


# plottin pie chart of total deaths
plt.figure(figsize=(18,18))
plt.title('Total Deaths')
plt.pie(Deaths_ls,labels=coun_ls,autopct=values)
plt.show()


# Here there are more deaths occured in United Kingdom than any other country in top 5 ranked effected countries followed by italy and belgium but still they are not most effected, there are two more countries stand above the UK, italy and belgium.

# In[39]:


# plotting pie charts of 'gdp reduction', 'Deaths per 100 Cases', 'Most effected countries'
plt.figure(figsize=(10,10))
plt.title('GDP Reduction')
plt.pie(gdp_ls,labels=coun_ls,autopct=values)
plt.show()
plt.figure(figsize=(10,10))
plt.title('Deaths per 100 Cases')
plt.pie(dp100c,labels=coun_ls,autopct=values)
plt.show()
plt.figure(figsize=(10,10))
plt.title('Most effected countries')
plt.pie(ev,labels=coun_ls,autopct=values)
plt.show()


# We can see that in above two pie diagrams Yemen has most deaths but Libya has its GDP decreased a lot, since we have given more emphasis to life than GDP, so Yemen is ranked number 1 in most effected country than comes Libya in 2nd place. United Kingdom came in 3rd place as it has almost equal reduction in both the cases but less than Yemen and Libya, since it is developed country it has been emphasized a lot in the news. Then comes Italy and Belgium in 4th and 5th place due to same criteria

# # Summary 
# Since the focus was more on China and United States in the beginning of pandemic, other countries were not looked at granular level. Here I have provided a visual to show how developing nations also got affected due to this pandemic and to our surprise we have found that Yemen, Libya came on top rather than UK, Italy, Belgium or any other european countries which have followed these two developing nations. We have used data from kaggle and gfmag to obtain data on Economic adversity and Personal loss and my analysis supports above statement on developing nations being unnoticed and denied of support on various issues. 

# ## References
# https://www.gfmag.com/global-data/economic-data/countries-lowest-gdp-growth

# https://www.kaggle.com/datasets/imdevskp/corona-virus-report
