#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import loginui as log
import DataBaseOperations as datab
def create_user():
    if name.get()=="":
        tk.messagebox.showinfo(title="Empty Field", message="Fill The Empty Field!!!")
        
    else:
        
        
        account_status=datab.createaccount(name.get(),username.get(),user_password.get())
        if account_status==1:
            msg.set("Account Created Successfully")
            window.destroy()
            loginform()
            
            
            
        else:
            
            msg.set("Please Check Your Data")
            
        
        
def loginform():
    
    log.loginform()

def close_window(windowsform):
    windowsform.destroy()
    
    
    
def createaccount():
            windowsform = tk.Tk()
            windowsform.title('Create Account')
            windowsform.geometry("400x400")
            windowsform.maxsize(400,400)
            windowsform.config(bg='#293A4B')
            global username
            global name;
            global user_password
            global msg;
            global window;
            name = tk.StringVar()
            username = tk.StringVar()
            user_password=tk.StringVar()
            window=windowsform
            msg=tk.StringVar()
            ################################
            label_name=tk.Label(windowsform,text="NAME",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()
            name_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold',textvariable=name).pack()
            label_username=tk.Label(windowsform,text="USER NAME",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()

            username_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold',textvariable=username).pack()

            label_password=tk.Label(windowsform,text="PASSWORD",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()

            password_textbox = tk.Entry(windowsform,show="*",width=50,font='Helvetica 10 bold',textvariable=user_password).pack()

            create_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Create Account",bg="orange",command=lambda:[create_user()]).place(x=70,y=150)
            login_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Login Account",bg="orange",command=lambda:[windowsform.destroy(),loginform()]).place(x=70,y=190)
            label_message=tk.Label(windowsform,text="",bg="#293A4B",foreground="orange",
                                    font='Helvetica 15 bold',textvariable=msg).place(x=60,y=250)
            ###############################

            
            windowsform.mainloop()
            
createaccount()


# In[ ]:





# In[ ]:




