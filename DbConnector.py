#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 


# In[20]:


def connector():
    mydb =mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456")
        
    return mydb


# In[ ]:





# In[ ]:




