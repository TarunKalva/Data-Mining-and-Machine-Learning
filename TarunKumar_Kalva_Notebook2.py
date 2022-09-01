#!/usr/bin/env python
# coding: utf-8

# #### Notebook 2: ROT
# ROT is a very simple cipher that is used to information hiding (https://en.wikipedia.org/wiki/ROT13 (Links to an external site.)) . Read the wiki page to understand how the encoder works.
# 
# a. Create an “encode_rot()” function to encode any given strings using ROT algorithm. The input should contain a key and a string of text. The key can be any integers both negative and positive (-12: turn left 12 positions,  36: turn right 36 positions). Only alphabet letters are encoded.
# 
# The following two lines of your code will generate an output of “Ocejkpg ECP ngctp 2 !!!“.
# 
# clear_text=” Machine CAN learn 2 !!!”
# 
# encode_rot(clear_text, 28)
# 
# b. Create a decode_rot() to decode a ciphertext. The input only contains the ciphertext. The output contains the cleartext and the key that was used to encode text. The key will be between 0 and 25.  (hint: Compare your decoded clear text with a dictionary text file and decide which one has the most dictionary words.)
# 
# The following two lines will generate an output of
# 
#  The clear text is : “Data is like people, interrogate it hard enough and it will tell you whatever you want to hear.”
# The key is 16
# 
#  cipher_text= “Tqjq yi byau fuefbu, ydjuhhewqju yj xqht udekwx qdt yj mybb jubb oek mxqjuluh oek mqdj je xuqh.”
# 
# decode_rot(cipher_text)

# In[5]:


# Creating a list of capital letters
capital_letters=[]
for i in range(65,91):
    capital_letters.append(chr(i))
print(capital_letters)


# In[6]:


# Creating a list of small letters
small_letters=[]
for i in range(97,123):
    small_letters.append(chr(i))
print(small_letters)  


# In[20]:


# Creating a function to encode the given text
def encode_rot(txt,key):
    #txt='Machine, can learn'
    #key=2
    txt_ls=list(txt) #converting text to list
    #print(txt_ls)
    cipher_ls=[] # initialising the cipher text list
    for i in txt_ls:
        if i in capital_letters:
            k=capital_letters.index(i)+key # adding key to index of letter to rotate it to desired position
            if (k>len(capital_letters)-capital_letters.index(i)): 
# if the position of k exceeds letters list then we'll start counting from first position and same applies for small letters
                cipher_ls.append(capital_letters[k-26]) #appending letter to cipher text list
            else:
                cipher_ls.append(capital_letters[k])
        elif i in small_letters:
            k=small_letters.index(i)+key
            if(k>len(small_letters)-small_letters.index(i)):
                cipher_ls.append(small_letters[k-26])
            else:
                cipher_ls.append(small_letters[k])
        else:
            cipher_ls.append(i)
    #print(cipher_ls)  
    cipher_txt=''.join(cipher_ls) # joinig the elements in list to form a string
    return cipher_txt
    #capital_letters[capital_letters.index('A')-4]
    
#print(encode_rot('Machine CAN learn 2 !!!',28))
#Ocejkpg ECP ngctp 2 !!!


# In[12]:


# function to decode the cipher text
def decode_rot(cip_txt,key):
    cip_txt_ls=list(cip_txt) # converting the text to list 
    clr_txt_ls=[] # clear text list
    for i in cip_txt_ls:
        if i in capital_letters:
            k=capital_letters.index(i)+key # same logic used in encode is used to decode and key is adjusted in main code
            if (k>len(capital_letters)-capital_letters.index(i)):
                clr_txt_ls.append(capital_letters[k-26])
            else:
                clr_txt_ls.append(capital_letters[k])
        elif i in small_letters:
            k=small_letters.index(i)+key
            if (k>len(small_letters)-small_letters.index(i)):
                clr_txt_ls.append(small_letters[k-26])
            else:
                clr_txt_ls.append(small_letters[k])
        else:
            clr_txt_ls.append(i)
    clr_txt=''.join(clr_txt_ls) # clear text list elements joined to form clear text
    return(clr_txt)
#print(decode_rot('Tqjq yi byau fuefbu, ydjuhhewqju yj xqht udekwx qdt yj mybb jubb oek mxqjuluh oek mqdj je xuqh',10))


# In[42]:


# Main Program 
clear_text=input('Enter the text to be encoded: ')
key_value=int(input('Enter the key to encode and decode: '))
key_encode=key_value
#if key_value<26:
    #key_decode=abs(26-key_value)
#else:
    
if key_encode in range(-12,36):
    cipher_text=encode_rot(clear_text,key_encode) # calling encode_rot function
    print(cipher_text)
else:
    print('Please enter the key in between -12 and 35')


# In[44]:


# decoding main program
if key_value<0:
    key_decode=abs(key_value)
if key_value>0 and key_value<26:
    key_decode=26-key_value 
if key_value>26:
    temp_key=key_value-26
    key_decode=26-temp_key  
print(cipher_text)    
decoded_text=decode_rot(cipher_text,key_decode) #calling decode_rot fuction
print(decoded_text)


# In[ ]:




