#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import createaccount as account
import DataBaseOperations as database

def loginfuction(user_name,user_password):
    login_data=database.login(user_name,user_password)
    if len(login_data)==0:
        tk.messagebox.showinfo(title="Invalid", message="Invalid Login")
    elif len(login_data)==1:
        tk.messagebox.showinfo(title="Empty Field", message="Login!!!")
    
    
    

def loginform():
    windowsform = tk.Tk()
    windowsform.title('Login Account')
    windowsform.geometry("400x400")
    windowsform.maxsize(400,600)
    windowsform.config(bg='#293A4B')
    username=""
    password=""
    msg=""
    username=tk.StringVar()
    password=tk.StringVar()
    
    label_username=tk.Label(windowsform,text="USER NAME",bg="#293A4B",foreground="white",
                            font='Helvetica 10 bold').pack()

    username_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold',textvariable=username).pack()

    label_password=tk.Label(windowsform,text="PASSWORD",bg="#293A4B",foreground="white",
                            font='Helvetica 10 bold').pack()

    password_textbox = tk.Entry(windowsform,show="*",width=50,font='Helvetica 10 bold',textvariable=password).pack()

    login_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Login Account",bg="orange",command=lambda:loginfuction(username.get(),password.get())).place(x=70,y=110)
    create_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Create Account",bg="orange",command=lambda:[windowsform.destroy(),account.createaccount()]).place(x=70,y=140)
    label_message=tk.Label(windowsform,text="",bg="#293A4B",foreground="orange",
                                    font='Helvetica 15 bold',textvariable=msg).place(x=60,y=250)

    windowsform.mainloop()

loginform()


# 

# In[ ]:




