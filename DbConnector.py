#!/usr/bin/env python
# coding: utf-8

# In[23]:


import mysql.connector


# In[21]:


def connector():
    mydb =mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="fitnessworld")
    return mydb
        
    

