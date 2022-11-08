

import tkinter
from tkinter import ttk

width = 600
height = 700
from tkinter import *
from tkinter import ttk
from tkinter import font
import mysql.connector as mysql
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import re
root = Tk()
root.title('Registration form')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)
txtName= StringVar()
txtUsername= StringVar()

# ttk.Label(root, text='Affix PASSPORT:', width=24,).pack(side=TOP)
# ttk.Entry(root,width=16, textvariable=txtUsername).pack(side=TOP,ipady=50, pady=10)

ttk.Label(root, text='EXAMINATION NO:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtName).pack(side=TOP,ipady=5, pady=10)

ttk.Label(root, text='Surname:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)

ttk.Label(root, text='OTHER NAMES:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)
ttk.Label(root, text='Marital Status:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)

ttk.Label(root, text='email address:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)


ttk.Label(root, text='password:', width=20).pack(side=TOP)
ttk.Entry(root,width=35, textvariable=txtUsername).pack(side=TOP,ipady=5, pady=10)


ttk.Label(root, text='Affix PASSPORT:', width=24,).place(x= 400,y= 500)
ttk.Entry(root,width=30,font=('arial', 90, 'bold')).place(x= 430,y= 540)



btnClear=ttk.Button(root, text='REGISTER', ).pack(ipady=5, ipadx=5)

root.mainloop()
