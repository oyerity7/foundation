import  tkinter
from tkinter import ttk




Welcome=Tk()
Welcome.geometry('400x400')
Label(Welcome, text="welcome", font=("Arial",30)).pack()
    
Welcome.mainloop()

def ade():
  S=Surname.get()
  F=Firstname.get()
  O=Othernames.get()
  A=Age.get()
  G=Gender.get()
  C=Country.get()
  S=State.get()
  CN=CentreNo.get()
  E=ExamNo.get()
  EY=ExamYear.get()
  S1=Subject1.get()
  G1=Grade1.get()
  S2=Subject2.get()
  G2=Grade2.get()
  S3=Subject3.get()
  G3=Grade3.get()
  S4=Subject4.get()
  G4=Grade4.get()
  S5=Subject5.get()
  G5=Grade6.get()
  S6=Subject6.get()
  G6=Grade6.get()
  S7=Subject7.get()
  G7=Grade7.get()
  S8=Subject8.get()
  G8=Grade8.get()

  res =  S, F, O, A, G, C, S, CN, E, EY, S1, G1, S2, G2, S3, S4, G4, S5, G5, S6, G6, S7, G7, S8, G8
  return res

  



# def registerDB(Surname, Firstname, Othernames,Age,Gender,Country,State,Center_No ,Exam_No,Exam_Year, Subject1,Grade1, Subject2,Grade2 ,Subject3,Grade3 ,Subject4,Grade4,Subject5,Grade5,Subject6,Grade6,Subject7,Grade7,Subject8,Grade8): 
#   con= mysql.connect(host='locahost', database='oyebimpe_db', user='root', password='')
#   cursor = con.cursor()
#   sql = "INSERT INTO Table_name (`Surname`, `Firstname`, `Othernames`,`Age`,`Gender`,`Country`,`State`,`Center No` ,`Exam No`,`Exam Year`, `Subject 1`,`Grade 1`,`Subject 2`,`Grade 2` ,`Subject 3`,`Grade 3` ,`Subject4`,`Grade 4`,`Subject 5`,`Grade 5`,`Subject6`,`Grade 6`,`Subject7`,`Grade 7`,`Subject8`,`Grade 8`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s) "
#   value=(Surname,Firstname, Othernames,Age,Gender,Country,State,Center_No ,Exam_No,Exam_Year, Subject1,Grade1,Subjec2,Grade2 ,Subjec3,Grade3 ,Subject4,Grade4,Subjec5,Grade5,Subject6,Grade6,Subject7,Grade7,Subject8,Grade8)
#   cursor.execute(sql,value)
#   con.commit()
#   messagebox.showinfo("info","saved")



def Submit():
  messagebox.showinfo("Saved","You Have Successfully Registered.")

def Clear():
  Surname.set("")
  Firstname.set("")
  Othernames.set("")
  Age.set("")
  Gender.set("")
  Country.set("")
  State.set("")
  CentreNo.set("")
  ExamNo.set("")
  ExamYear.set("")
  Subject1.set("")
  Grade1.set("")
  Subject2.set("")
  Grade2.set("")
  Subject3.set("")
  Grade3.set("")
  Subject4.set("")
  Grade4.set("")
  Subject5.set("")
  Grade6.set("")
  Subject6.set("")
  Grade6.set("")
  Subject7.set("")
  Grade7.set("")
  Subject8.set("")
  Grade8.set("")




# initialize root element from TK
root = Tk()
root.title('Student Registration')

#configuring root width and height

width = 1050
height = 550
sw = root.winfo_screenwidth()
sh =root.winfo_screenheight()
x= sw//2 - width//2
y = sh//2 - height//2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0,0)
root.wm_iconbitmap('./icons8_notepad.ico')

#Variables  
cmbAge =StringVar()
cmbGender = StringVar()


# States in Nigeria 
statesElement = ( "Abia",
  "Adamawa",
  "Akwa Ibom",
  "Anambra",
  "Bauchi",
  "Bayelsa",
  "Benue",
  "Borno",
  "Cross River",
  "Delta",
  "Ebonyi",
  "Edo",
  "Ekiti",
  "Enugu",
  "FCT - Abuja",
  "Gombe",
  "Imo",
  "Jigawa",
  "Kaduna",
  "Kano",
  "Katsina",
  "Kebbi",
  "Kogi",
  "Kwara",
  "Lagos",
  "Nasarawa",
  "Niger",
  "Ogun",
  "Ondo",
  "Osun",
  "Oyo",
  "Plateau",
  "Rivers",
  "Sokoto",
  "Taraba",
  "Yobe",
  "Zamfara")
groupBox = ttk.LabelFrame(root,height=250, text='Bio-Data Record')
groupBox.grid(ipadx=10, ipady=10, pady=5,padx=10, row=0,sticky=N, column=0)


groupBox2 = ttk.LabelFrame(root,height=250, text='Education/Olevel')
groupBox2.grid(ipadx=10, ipady=10, pady=5,padx=5, sticky=N, row=0, column=1)

groupBox3 = ttk.LabelFrame(root,height=250, text='Actions')
groupBox3.grid(ipadx=10, ipady=10, pady=5,padx=5, sticky=S+W, row=1, column=0, columnspan=2)



#creating Variables
Surname=StringVar()
Firstname=StringVar()
Othernames=StringVar()
Age=StringVar()
Gender=StringVar()
Country=StringVar()
State=StringVar()
CentreNo=StringVar()
ExamNo = StringVar()
ExamYear=StringVar()
Subject1=StringVar()
Grade1=StringVar()
Subject2=StringVar()
Grade2=StringVar()
Subject3=StringVar()
Grade3=StringVar()
Subject4=StringVar()
Grade4=StringVar()
Subject5=StringVar()
Grade5=StringVar()
Subject6=StringVar()
Grade6=StringVar()
Subject7=StringVar()
Grade7=StringVar()
Subject8=StringVar()
Grade8=StringVar()


#groupBox Element One 
#Surname Element
lblSurname = ttk.Label(groupBox, text='Surname', font=('', 13))
lblSurname.grid(row=0, column=0, padx=5)
txtSurname = ttk.Entry(groupBox, width=50,textvariable=Surname)
txtSurname.grid(row=0, column=1, columnspan=4, sticky=W+E, ipady=4,ipadx=5, pady=5)

#First Name Element
lblfirstname = ttk.Label(groupBox, text='Firstname', font=('', 13))
lblfirstname.grid(row=1, column=0, padx=5)
txtfirstname = ttk.Entry(groupBox, width=50,textvariable=Firstname)
txtfirstname.grid(row=1, column=1, sticky=W+E,columnspan=4, ipady=4,ipadx=5, pady=5)

#other Names Element
lblOthername = ttk.Label(groupBox, text='Othernames', font=('', 13))
lblOthername.grid(row=2, column=0, padx=5)
txtOthername = ttk.Entry(groupBox, width=50,textvariable=Othernames)
txtOthername.grid(row=2, column=1, sticky=W+E,columnspan=4, ipady=4,ipadx=5, pady=5)

#Age  Element
lblAge = ttk.Label(groupBox, text='Age', font=('', 13))
lblAge.grid(row=3, column=0, padx=5)
txtAge = ttk.Combobox(groupBox,state='readonly', textvariable=cmbAge)
txtAge['values'] = tuple( range(1,101))
    
txtAge.grid(row=3, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

# Gender Element
lblGender = ttk.Label(groupBox, text='Gender', font=('', 13))
lblGender.grid(row=3, column=2, padx=5)
txtGender = ttk.Combobox(groupBox,state='readonly', textvariable=cmbGender)
txtGender['values'] = ('male','female','armiphrodite')
txtGender.grid(row=3, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)

# Country Element
lblCountry = ttk.Label(groupBox, text='Country', font=('', 13))
lblCountry.grid(row=4, column=0, padx=5)
txtCountry = ttk.Combobox(groupBox,state='readonly', textvariable='')
txtCountry['values'] = ('Nigeria', 'Ghana', 'Cameroun', 'United State of America', 'Morocco','Other')
txtCountry.grid(row=4, column=1,sticky=E+W, columnspan=4, ipady=4,ipadx=5, pady=5)

# State Element
lblstate = ttk.Label(groupBox, text='State', font=('', 13))
lblstate.grid(row=5, column=0, padx=5)
txtState = ttk.Combobox(groupBox,state='readonly', textvariable='')
txtState['values'] = statesElement
txtState.grid(row=5, column=1,sticky=E+W,columnspan=4, ipady=4,ipadx=5, pady=5)


#GroupBox 2 Element 
lblcenter = ttk.Label(groupBox2, text='Center No', font=('', 13))
lblcenter.grid(row=0, column=0, padx=5)
txtcenter = ttk.Entry(groupBox2, textvariable='')
txtcenter.grid(row=0, column=1,sticky=E+W,columnspan=4, ipady=4,ipadx=5, pady=5)

#Exam no and Year 
lblexamNo = ttk.Label(groupBox2, text='Exam No', font=('', 13))
lblexamNo.grid(row=1, column=0, padx=5)
txtExamNo = ttk.Entry(groupBox2, textvariable='')
txtExamNo.grid(row=1, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblExamYear = ttk.Label(groupBox2, text='Exam year', font=('', 13))
lblExamYear.grid(row=1, column=2, padx=5)
txtExamYear = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtExamYear['values'] = tuple(range(1950,2023))
txtExamYear.grid(row=1, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)

#Subject and Grade 
lblsubject1 = ttk.Label(groupBox2, text='Subject 1', font=('', 13))
lblsubject1.grid(row=2, column=0, padx=5)
txtsubject1 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject1['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject1.grid(row=2, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade1 = ttk.Label(groupBox2, text='Grade 1', font=('', 13))
lblgrade1.grid(row=2, column=2, padx=5)
txtgrade1 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade1['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade1.grid(row=2, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)


lblsubject2 = ttk.Label(groupBox2, text='Subject 2', font=('', 13))
lblsubject2.grid(row=3, column=0, padx=5)
txtsubject2 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject2['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject2.grid(row=3, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade2 = ttk.Label(groupBox2, text='Grade 2', font=('', 13))
lblgrade2.grid(row=3, column=2, padx=5)
txtgrade2 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade2['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade2.grid(row=3, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)



lblsubject3 = ttk.Label(groupBox2, text='Subject 3 ', font=('', 13))
lblsubject3.grid(row=4, column=0, padx=5)
txtsubject3 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject3['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject3.grid(row=4, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade3 = ttk.Label(groupBox2, text='Grade 3', font=('', 13))
lblgrade3.grid(row=4, column=2, padx=5)
txtgrade3 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade3['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade3.grid(row=4, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)




lblsubject4 = ttk.Label(groupBox2, text='Subject 4', font=('', 13))
lblsubject4.grid(row=5, column=0, padx=5)
txtsubject4 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject4['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject4.grid(row=5, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade4 = ttk.Label(groupBox2, text='Grade 4', font=('', 13))
lblgrade4.grid(row=5, column=2, padx=5)
txtgrade4 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade4['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade4.grid(row=5, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)


lblsubject5 = ttk.Label(groupBox2, text='Subject 5', font=('', 13))
lblsubject5.grid(row=6, column=0, padx=5)
txtsubject5 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject5['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject5.grid(row=6, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade5 = ttk.Label(groupBox2, text='Grade 5', font=('', 13))
lblgrade5.grid(row=6, column=2, padx=5)
txtgrade5 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade5['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade5.grid(row=6, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)


lblsubject6 = ttk.Label(groupBox2, text='Subject 6', font=('', 13))
lblsubject6.grid(row=7, column=0, padx=5)
txtsubject6 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject6['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject6.grid(row=7, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade6 = ttk.Label(groupBox2, text='Grade 6', font=('', 13))
lblgrade6.grid(row=7, column=2, padx=5)
txtgrade6 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade6['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade6.grid(row=7, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)



lblsubject7 = ttk.Label(groupBox2, text='Subject 7', font=('', 13))
lblsubject7.grid(row=8, column=0, padx=5)
txtsubject7 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtsubject7['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject7.grid(row=8, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade7 = ttk.Label(groupBox2, text='Grade 7', font=('', 13))
lblgrade7.grid(row=8, column=2, padx=5)
txtgrade7 = ttk.Combobox(groupBox2,state='readonly', textvariable='')
txtgrade7['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
txtgrade7.grid(row=8, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)




lblsubject8 = ttk.Label(groupBox2, text='Subject 8', font=('', 13))
lblsubject8.grid(row=9, column=0, padx=5)
txtsubject8 = ttk.Combobox(groupBox2,state='readonly', textvariable=Subject8)
txtsubject8['values'] = ('Mathematics','English Language', 'French', 'Geography', 'Commerce','Physics','Chemistry','Agricultural Science','Economics','Yoruba', 'Igbo', 'Computer','Tie & Dye','Goverment','Biology','Financial Accounting','Literature in English','Physical and health Education')
    
txtsubject8.grid(row=9, column=1,sticky=E+W, ipady=4,ipadx=5, pady=5)

lblgrade8 = ttk.Label(groupBox2, text='Grade 8', font=('', 13))
lblgrade8.grid(row=9, column=2, padx=5)
txtgrade8 = ttk.Combobox(groupBox2,state='readonly', textvariable=Grade8)
txtgrade8['values'] = ('A1','B2','B3','C4','C5','C6','D7','E8','F9')
    
txtgrade8.grid(row=9, column=3,sticky=E+W, ipady=4,ipadx=5, pady=5)

# Buttons Element Element
saveImg =PhotoImage(file='./icons/save-16.png')
btnSubmit = ttk.Button(groupBox3, text='Submit Record', image=saveImg, compound=LEFT,command =Submit)
btnSubmit.pack(ipady=5, ipadx=5,side=LEFT, padx=5)

cancelImag =PhotoImage(file='./icons/edit/delete_16px.png')
btnClear = ttk.Button(groupBox3, text='Clear Record', image=cancelImag, compound=LEFT,command=Clear )
btnClear.pack(ipady=5, ipadx=5,padx=5, side=LEFT)


root.mainloop()