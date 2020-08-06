#!/usr/bin/env python
# coding: utf-8

# # Guessing a correct number selected by Computer in your range

# In[ ]:





# In[1]:


import random


# In[2]:


smaller = int(input(' your smaller number is :'))


# In[3]:


larger = int(input('your larger number is :'))


# In[4]:


mynumber = random.randint(smaller , larger)


# In[5]:


count = 0


# In[ ]:


while True :
    count += 1
    usernumber = int(input('Enter your guess'))
    if usernumber < mynumber :
        print("your number is too small")
    elif usernumber > mynumber :
        print ("your number is too large")
    else :
        print(" yay congratulations! you got it in" , count, "tries")


# In[ ]:




