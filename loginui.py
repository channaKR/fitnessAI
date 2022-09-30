#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import createaccount as account

def loginform():
    windowsform = tk.Tk()
    windowsform.title('Login Account')
    windowsform.geometry("400x400")
    windowsform.maxsize(400,600)
    windowsform.config(bg='#293A4B')

    label_username=tk.Label(windowsform,text="USER NAME",bg="#293A4B",foreground="white",
                            font='Helvetica 10 bold').pack()

    username_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold').pack()

    label_password=tk.Label(windowsform,text="PASSWORD",bg="#293A4B",foreground="white",
                            font='Helvetica 10 bold').pack()

    password_textbox = tk.Entry(windowsform,show="*",width=50,font='Helvetica 10 bold').pack()

    login_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Login Account",bg="orange").place(x=70,y=110)
    create_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Create Account",bg="orange",command=lambda:[windowsform.destroy(),account.createaccount()]).place(x=70,y=140)


    windowsform.mainloop()

loginform()


# In[ ]:




