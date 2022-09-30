#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import loginui as log

def validate_form():
    if name.get()=="":
        tk.messagebox.showinfo(title="Empty Field", message="Fill The Empty Field!!!")
        
    else:
        print(name.get())
        
def loginform():
    
    
    log.loginform()
    
    
def createaccount():
            windowsform = tk.Tk()
            windowsform.title('Create Account')
            windowsform.geometry("400x400")
            windowsform.maxsize(400,600)
            windowsform.config(bg='#293A4B')
            global username
            global name;
            name = tk.StringVar()
            username = tk.StringVar()
            user_password=tk.StringVar()
            ################################
            label_name=tk.Label(windowsform,text="NAME",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()
            name_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold',textvariable=name).pack()
            label_username=tk.Label(windowsform,text="USER NAME",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()

            username_textbox = tk.Entry(windowsform,width=50,font='Helvetica 10 bold').pack()

            label_password=tk.Label(windowsform,text="PASSWORD",bg="#293A4B",foreground="white",
                                    font='Helvetica 10 bold').pack()

            password_textbox = tk.Entry(windowsform,show="*",width=50,font='Helvetica 10 bold').pack()

            create_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Create Account",bg="orange",command=validate_form).place(x=70,y=150)
            login_account=tk.Button(windowsform,width=30,font='Helvetica 10 bold',text="Login Account",bg="orange",command=lambda:[windowsform.destroy(),loginform()]).place(x=70,y=190)
            ###############################

            
            windowsform.mainloop()
            
createaccount()


# In[ ]:





# In[ ]:




