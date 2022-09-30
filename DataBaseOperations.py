#!/usr/bin/env python
# coding: utf-8

# In[1]:


import DbConnector as db
import mysql.connector


# In[8]:


def createaccount(name,username,password):
    try:
        mydb =db.connector()
        mycursor = mydb.cursor()
        query="insert into user(name,username,password) values(%s,%s,%s)"
        data=(name,username,password)
        
        mycursor.execute(query,data)
        mydb.commit()
        return 1
    except Exception as e:
        
        return 0
    
       
    


# In[2]:


def login(username,password):
    try:
        mydb =db.connector()
        mycursor = mydb.cursor()
        query="SELECT * FROM user WHERE username=%s and password=%s"
        data=(username,password)
        mycursor.execute(query,data)
        myresult = mycursor.fetchall()
        return myresult
        
        
        
    except Exception as e:
        print(e)
        
    

