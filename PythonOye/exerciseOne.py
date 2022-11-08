# #Functions Declaratiion
# def registerDB(fname, username, password):
#     connect = mysql(host='locahost', database='dbname', user='root', password='')
#     cursor = connect.cursor()
#     sql = "INSERT INTO Table_name (`fullname`, `username`, `password`) VALUES(%s, %s, %s) "
#     if(cursor.execute(sql, (fname,username, password))):
#         messagebox.showinfo('Register', 'Registration is successful!')
#     else:
#         messagebox.showerror('Error', 'Error Occur during registration!')

# def clearBox():
#     txtName.set('')
#     txf(username != ""):
#         isTrueUsername = re.match(UsernamePattern, username)
#         if(isTrueUsername == None):
#             Msg('Username does not Match the format')
#         return
#     else:
#         registerDB(fullname,username, '')tUsername.set('')
# def Msg(msg):
#     messagebox.showwarning('UnMatch Pattern', msg)

# def Register():
#     fullname = str(txtName.get())
#     username = str(txtUsername.get())
#     FullnamePattern = "^[A-Za-z\-\s\']{3,50}$"
#     PhonePattern = "^[0-9]{11}$"
#     UsernamePattern = "^[a-zA-Z0-9]{6,}$"
#     PasswordPattern = "^[a-zA-Z0-9]{8,}$"
#     if(fullname != ""):
#         isTrue = re.match(FullnamePattern,fullname)
#         if(isTrue==None):
#            Msg('Fullname entered is Invalid')
#         return
#     eli
# configuring root width and height

import tkinter
from tkinter import ttk

width = 600
height = 350
from tkinter import *
from tkinter import ttk
from tkinter import font
import mysql.connector as mysql
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import re
root = Tk()
root.title('Class 21 Reunion')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)
txtName= StringVar()
txtUsername= StringVar()
ttk.Label(root, text='Hurray!,Hurray!,Hurray!:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtName).pack(side=TOP,ipady=5, pady=10)

ttk.Label(root, text='Reunion is Here:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)

btnClear=ttk.Button(root, text='REGISTER', ).pack(ipady=5, ipadx=5)
btnRegister=ttk.Button(root, text='LOGIN', ).pack(ipady=5, ipadx=5)

ttk.Label(root, text='NO Account?click register:', width=32).pack(side=TOP)
root.mainloop()