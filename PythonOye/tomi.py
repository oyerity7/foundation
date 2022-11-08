import tkinter
from tkinter import ttk
from tkinter import *
from ttkthemes import THEMES, ThemedTk

def loginApp():
    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt = ThemedTk(theme='adapta', themebg=True)
    rt.title('Login - Computer Based Test')
    width = 375
    height = 442
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)

    logobg = PhotoImage(file='./img/tempo-120.png')

    #divide the root into two parallel row
    rt.rowconfigure(0,weight=1)
    rt.rowconfigure(1,weight=4)
    rt.columnconfigure(0,weight=1)

    #styling the content  
    style = ttk.Style()

    style.configure('frame_top.TFrame', background=__frameTop)
    style.configure('frame_bottom.TFrame', background=__frameBottom)
    style.configure('title.TLabel', background=__frameTop, foreground='#d70a0a', font=('roboto', 24, 'bold', 'underline'))
    style.configure('description.TLabel', foreground=__frameBottom, background='#fff', font=('roboto', 10)) 

    style.configure('formframe.TFrame',background=__frameBottom)
    style.configure('formLabel.TLabel',background=__frameBottom, foreground='#fff', font=('roboto', 12))

    style.configure('formEntry.TEntry', font=('roboto', 12))
    style.configure('register.TLabel', foreground='#fff', background=__frameBottom, font=('roboto', 9, 'normal'))
    style.configure('reg.TLabel', foreground='#34edd1', background=__frameBottom, font=('roboto', 9, 'underline', 'bold'), highlightedforeground='red' )
    style.configure('btn.TButton', font=('6'))

    #placing frame on the root window Tk
    frame_top= ttk.Frame(rt, style='frame_top.TFrame')
    frame_bottom = ttk.Frame(rt, style='frame_bottom.TFrame')

    #display the frames on the root windows using grid geometry
    frame_top.grid(row=0, column=0, sticky='WENS')
    frame_bottom.grid(row=1, column=0, sticky='WENS', ipadx=10)

    lblLogo = ttk.Label(frame_top, image=logobg)
    lblLogo.pack(pady=3)
    lblTitle = ttk.Label(frame_top, text='Sign In', style='title.TLabel')
    lblTitle.pack(side='top', pady=7)

    lblDescription = ttk.Label(frame_top, text='Please fill in all the boxes below. All field(s) are required.', style='description.TLabel', wraplength=300)
    lblDescription.pack(pady=2)

    #controls on frame Bottom 
    formFrame = ttk.Frame(frame_bottom, style='formframe.TFrame')
    formFrame.pack(pady=20, ipadx=10, ipady=10)

    lblExamNo = ttk.Label(formFrame, text='Exam No:',style='formLabel.TLabel')
    lblSurname = ttk.Label(formFrame, text='Surname:', style='formLabel.TLabel')
    lblOthername=ttk.Label(formFrame, text='Other names', style=formLabel.TLabel)
    lblDOB = ttk.Label(formFrame, text='DOB:', style='formLabel.TLabel')
    lblEmailaddress=ttk.Label(formFrame, text='Email ADDRESS', style=formLabel.TLabel)
    lblGender=ttk.Label(formFrame, text='Gender', style=formLabel.TLabel)
    lblExamNo.grid(row=0,column=0, columnspan=2, sticky='we', pady=5, padx=5)
    lblSurname=ttk.Label(formFrame, text='Surname', style=formLabel.TLabel)
    lblOthername=ttk.Label(formFrame, text='Other names', style=formLabel.TLabel)     
    lblDOB=ttk.Label(formFrame, text='DOB', style=formLabel.TLabel)
    lblEmailaddress=ttk.Label(formFrame,text='Email ADDRESS', style=formLabel.TLabel)



    #Entry control Widgets 
    txtExamNo = ttk.Entry(formFrame, justify='center', width=28,font=('arial', 12, 'bold'))
    txtPassword = ttk.Entry(formFrame,show='x', justify='center', width=28, font=('arial', 10, 'bold'))

    txtExamNo.grid(row=0, column=2, sticky='WE', pady=5, ipady=5)
    txtPassword.grid(row=1, column=2, sticky='WE', pady=5, ipady=5)

    txtSubmit = ttk.Button(formFrame, text='Sign In', style='btn.TButton')
    txtSubmit.grid(row=2,column=1,columnspan=2,sticky='E')

    rt.mainloop()