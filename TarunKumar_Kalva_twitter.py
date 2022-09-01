#!/usr/bin/env python
# coding: utf-8

# ## Live monitoring of twitter data

# In[113]:


from twython import TwythonStreamer


# In[114]:


tweets=[]
class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        #if data['user']['lang']=='en':
        tweets.append(data)
        print("Received tweet #",len(tweets))
        if len(tweets)>=300:
            self.disconnect()
    def on_error(self,status_code,data):
        print(status_code,data)
        self.disconnect()    


# In[115]:


api_key='KPdw6ACVarBAFRDDcTTOr7yA3'
api_secret='lWHMz5QifvT0xIezqVRv7uDu8u2c19KoosrRIYcCv5I0BOzrTT'
access_token='1282747697028636672-RN9xQb0GvT5dQA2w996YKfBVFZW2mh'#'1493379114086060035-Frvr6QCa9RGrHoP5uNiaaFrWu6C4ZT'
acess_token_secret='c4Vn1hjiGdFlCler2zJI9Sl7VLNK30m5pKfJPieJBxq0A'#'kttC1TPakD5ESqLLEgp0qbHJIgCnoCzQuaMJsWKXUyT2Y'


# In[116]:


stream=MyStreamer(api_key,api_secret,access_token,access_token_secret)


# In[117]:


stream.statuses.filter(track='phone')


# In[118]:


tweets[0]['user']['screen_name']


# In[119]:


followers_count_list=[]
names=[]
for i in range(len(tweets)):
    followers_count_list.append(tweets[i]['user']['followers_count'])
    names.append(tweets[i]['user']['screen_name'])


# In[120]:


max(followers_count_list)


# In[121]:


import numpy as np


# In[122]:


ar=np.array(followers_count_list)


# In[126]:


print(np.mean(ar))
print(np.std(ar))
print(np.var(ar))
print(np.max(ar))
print(np.min(ar))
#count=0
#print(ar[2]==2212)
#for i in range(len(ar)):
#    if ar[i]==8:
#        count+=1
#print(count)        


# In[124]:


import matplotlib.pyplot as plt


# In[125]:


plt.plot(ar)
plt.title('Followers')
plt.xlabel('Tweet numbers')
plt.ylabel('followers Count')
plt.grid() #plt.show()


# My Graph states the followers_count of the users who have tweeted with word 'phone' in it, I've taken the data set of 300 tweets and in those the maximum number of followers for a person who tweeted are 143410 who might be a celebrity where the minimum is 0 which shows that he can be new user. On an average there are 2799 followers and the standard deviation is 12527 which is very high which shows that data variance is higher and data points are spread out across the graph. We have plotted a line graph to show how data is moving.

# In[ ]:




