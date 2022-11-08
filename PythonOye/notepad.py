# begins module import statement
import sys
from tkinter import *
from tkinter import ttk
from tkinter import font, filedialog as fd
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
from turtle import undo
import webbrowser
from PIL import ImageTk

# End of module statement
# variable Declaration
statusBar_Flag=True
url=''
# Function for Tolevel Design for Help Button

#definition  function for NotePad
def new_file():
    global url
    url= ''
    scroltext.delete('1.0',END)

def open_file(event=None):
    global url
    url = fd.askopenfilename(initialdir=os.getcwd(), title='Select your Text Document',
                             filetypes=(('All Text(*.*)', '*.*'),('TempoPad(.txt)','*.txt')))
    try:
        with open(url, 'r') as f:
            scroltext.delete('1.0', END)
            scroltext.insert('1.0',f.read())
            root.title(os.path.basename(url + ' - Tempopad'))
    except FileNotFoundError:
        return
    except:
        return

def save_file(event=None):
    global url
    try:
        if(url):
            content = str(scroltext.get('1.0', END))
            with open(url,'w', encoding='utf-8') as f:
                f.write(content)
        else:
         save_as_file()
         root.title(os.path.basename(url + ' - Tempopad'))
    except FileNotFoundError:
        return
    except:
        return

def save_as_file(event=None):
    global url
    url = fd.asksaveasfile(initialdir=os.getcwd(), title='Save your Document',
                           filetypes=(('All files(*.*)', '*.*'), ('Text files(*.txt)', '*.txt')), mode='w',
                           defaultextension='.txt')
    content = str(scroltext.get('1.0', END))
    url.write(content)
    url.close()

#Exit App Function
def exit_file():
    fb = messagebox.askyesno('Exit Tempopad', 'Do you wan to exit?')
    if(fb):
        sys.exit(0)
    else:
        return

#Undo Function
def undo_file():
    scroltext.event_generate('<<Undo>>')
    
#Redo Function
def redo_file():
    scroltext.event_generate('<<Redo>>')
#Copy Function 
def copy_file():
    scroltext.event_generate('<<Copy>>')
#Paste Function 
def paste_file():
    scroltext.event_generate('<<Paste>>')
#Cut Function 
def cut_file():
    scroltext.event_generate('<<Cut>>')
#Select Delete Function 
def delete_file():
    scroltext.delete(1.0,END)
    scroltext.focus()
#Send Feedback Function 
def send_feedback():
    answer = messagebox.askyesno('Send Feedback','Do you like our project?')
    if(answer):
        fb = messagebox.askyesno('Send Feedback', 'Do you want to rate us?')
        if(fb):
            urls= 'https://facebook.com/tempodigitalculture'
            webbrowser.open_new(urls)
        else:
            return
    else:
        return

#Date and Time function 
def timeDate():
    dateString=datetime.today()
    today = datetime.strftime(dateString,'%d-%B-%Y %I:%M:%S %p')
    print(today)
    messagebox.showinfo("Today's Date",today)
#End of function for NotePad


def aboutHelp():
    aboutTk = Toplevel(root)
    aboutTk.transient(root)
    aboutTk.grab_set()
    aboutTk.title('About TempoPad')
    width = 400
    height = 300
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    aboutTk.geometry(f'{width}x{height}+{x}+{y}')
    aboutTk.resizable(0, 0)
    aboutTk.wm_iconbitmap('./icons8_notepad.ico')
    lblAbout = ttk.Label(aboutTk, text='About TempoPad', font=('arial', 20, 'bold'))
    lblAbout.pack(pady=10)
    message = 'This application is developed by Python Developer Team under JayTee Foundation. It is well-known that ' \
              'this app act as a guideline for young developer who wish to join the winning team for developing ' \
              'different application for mankind. This application for for personal use only. Any alteration or ' \
              'decompiling of this software is highly prohibited. Thanks. '
    lblTextAbout = ttk.Label(aboutTk, text=message, font=('arial', 12), wraplength=300, justify=CENTER)
    lblTextAbout.pack(pady=5)
    aboutTk.mainloop()

def hide_statusBar():
    global statusBar_Flag
    if(statusBar_Flag):
        statusBar.pack_forget()
        statusBar_Flag=False

    else:
        scroltext.pack_forget()
        statusBar.pack(side=BOTTOM)
        statusBar_Flag=True
        scroltext.pack(side=TOP)


# initialize root element from TK
root = Tk()
root.title('Untitled - Tempopad')

# configuring root width and height

width = 800
height = 450
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)

# setting icon to the root window
icon = PhotoImage(file='./icons/icons8_notepad_48.png')
root.iconphoto(False, icon)
# adding menuBar to the root window
menuBar = Menu(root)
root.configure(menu=menuBar)

# Tool Bar Menu
toolBar = ttk.Label(root)
toolBar.pack(side=TOP, fill=X, expand=True)

# adding status bar element to the notepad
lblstatusBar= StringVar()

statusBar = Label(root, textvariable=lblstatusBar)
statusBar.pack(side=BOTTOM, fill=X, expand=TRUE)
lblstatusBar.set(True)
# addding scroltext to my rpoot window
text_editor= StringVar()
scroltext = ScrolledText(root, font=('Time new romans', 14),undo=True)
scroltext.pack(side=TOP, fill=X)

# adding menus to the menuBar window
fileMenu = Menu(menuBar, tearoff=0)
editMenu = Menu(menuBar, tearoff=0)
formatMenu = Menu(menuBar, tearoff=0)
viewMenu = Menu(menuBar, tearoff=0)
zoomMenu = Menu(viewMenu, tearoff=0)
helpMenu = Menu(menuBar, tearoff=0)

# Toobar Menu ICOn Initializing photoIcon
UnderlineIcon = PhotoImage(file='icons/underline_30px.png')
BoldIcon = PhotoImage(file='icons/bold_30px.png')
ItalicIcon = PhotoImage(file='icons/italic_30px.png')
LeftIcon = PhotoImage(file='icons/align_left_30px.png')
RightIcon = PhotoImage(file='icons/align_right_30px.png')
JustifyIcon = PhotoImage(file='icons/align_justify_30px.png')
CenterIcon = PhotoImage(file='icons/align_center_30px.png')

# File Menu Icon initializing photoIcon
newIcon = PhotoImage(file='icons/create_new-16.png')
openIcon = PhotoImage(file='icons/open_document-16.png')
newWindowIcon = PhotoImage(file='icons/windows8_tablet-16.png')
printIcon = PhotoImage(file='icons/print-16.png')
pagesetupIcon = PhotoImage(file='icons/page_overview_4-16.png')
exitIcon = PhotoImage(file='icons/exit-16.png')
saveIcon = PhotoImage(file='icons/save-16.png')
saveAsIcon = PhotoImage(file='icons/save_new-16.png')

# edit Menu icons initialization
undoIcon = PhotoImage(file='icons/edit/undo_16px.png')
cutIcon = PhotoImage(file='icons/edit/cut_16px.png')
copyIcon = PhotoImage(file='icons/edit/copy_16px.png')
pasteIcon = PhotoImage(file='icons/edit/paste_16px.png')
delIcon = PhotoImage(file='icons/edit/delete_16px.png')
searchIcon = PhotoImage(file='icons/edit/search_16px.png')
findIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
findNextIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
preIcon = PhotoImage(file='icons/edit/prev_16px.png')
replaceIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
gotoIcon = PhotoImage(file='icons/edit/forward_16px.png')
selectAllIcon = PhotoImage(file='icons/edit/checkmark_16px.png')
timeDateIcon = PhotoImage(file='icons/edit/schedule_16px.png')

# format Icons Initialization
wordwrapIcon = PhotoImage(file='icons/format/word_16px.png')
fontIcon = PhotoImage(file='icons/format/typography_16px.png')

# View Icons Initialization
statusIcon = PhotoImage(file='icons/view/bar_chart_16px.png')
zoominIcon = PhotoImage(file='icons/view/zoom_in_16px.png')
zoomoutIcon = PhotoImage(file='icons/view/zoom_out_16px.png')
zoomDefaultIcon = PhotoImage(file='icons/view/view_16px.png')

# View Icons Initialization
viewHelpIcon = PhotoImage(file='icons/help/help_16px.png')
sendFeedbackIcon = PhotoImage(file='icons/help/feedback_16px.png')
aboutIcon = PhotoImage(file='icons/help/about_16px.png')

# adding menu items to the file  Menu
fileMenu.add_command(label='New', accelerator='Ctrl + N', underline=0, image=newIcon, compound=LEFT, command=new_file)
fileMenu.add_command(label='New Window', accelerator='Ctrl + Shift + N', underline=4, compound=LEFT,
                     image=newWindowIcon)
fileMenu.add_command(label='Open...', accelerator='Ctrl + O', underline=0, image=openIcon, compound=LEFT, command=open_file)
fileMenu.add_command(label='Save', accelerator='Ctrl + S', underline=0, image=saveIcon,command=save_file, compound=LEFT)
fileMenu.add_command(label='Save As...', accelerator='Ctrl + Shift + S',command=save_as_file, underline=5, compound=LEFT, image=saveAsIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Page Setup...', underline=8, image=pagesetupIcon, compound=LEFT)
fileMenu.add_command(label='Print...', accelerator='Ctrl + P', underline=0, compound=LEFT, image=printIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', compound=LEFT, image=exitIcon, underline=1, accelerator='Ctrl + Q',
                     command=exit_file)

# Edit Menu Items initialization
editMenu.add_command(label='Undo', accelerator='Ctrl + Z', image=undoIcon, compound=LEFT,command=undo_file)
editMenu.add_command(label='Redo', accelerator='Ctrl + Y', compound=LEFT,command=redo_file)
editMenu.add_separator()
editMenu.add_command(label='Cut',command=cut_file, accelerator='Ctrl + X', compound=LEFT, image=cutIcon)
editMenu.add_command(label='Copy',command= copy_file, accelerator='Ctrl + C', image=copyIcon, compound=LEFT)

editMenu.add_command(label='Paste',command=paste_file, accelerator='Ctrl + V', image=pasteIcon, compound=LEFT)
editMenu.add_command(label='Delete',command=delete_file, accelerator='Ctrl + Del', compound=LEFT, image=delIcon)
editMenu.add_separator()
editMenu.add_command(label='Search with bing', accelerator='Ctrl + E', image=searchIcon, compound=LEFT)

editMenu.add_command(label='Find', accelerator='Ctrl + F', image=findIcon, compound=LEFT)
editMenu.add_command(label='Find Next', accelerator='F3', compound=LEFT, image=findNextIcon)
editMenu.add_command(label='Find Prev', accelerator='Shift + F3', image=preIcon, compound=LEFT)

editMenu.add_command(label='Replace', accelerator='Ctrl + H', image=replaceIcon, compound=LEFT)
editMenu.add_command(label='Goto', accelerator='Ctrl + G', compound=LEFT, image=gotoIcon)
editMenu.add_separator()
editMenu.add_command(label='Select All', accelerator='Ctrl + A', image=selectAllIcon, compound=LEFT)
editMenu.add_command(label='Time/Date',command=timeDate, accelerator='F5', image=timeDateIcon, compound=LEFT)

# Format Menu Items initialization
formatMenu.add_checkbutton(label='Word Wrap', image=wordwrapIcon, compound=LEFT)
formatMenu.add_command(label='Font...', image=fontIcon, compound=LEFT)

# adding menu items to the View  Menu
viewMenu.add_cascade(label='Zoom', menu=zoomMenu)
show_status= StringVar()
show_status.set(True)
viewMenu.add_checkbutton(label='Status Bar', image=statusIcon, compound=LEFT, command=hide_statusBar,
                         variable=show_status,onvalue=True, offvalue=False)

# adding menu items to Zoom menu
zoomMenu.add_command(label='Zoom In', image=zoominIcon, compound=LEFT, accelerator='Ctrl + Plus')
zoomMenu.add_command(label='Zoom Out', image=zoomoutIcon, compound=LEFT, accelerator='Ctrl + Minus')
zoomMenu.add_command(label='Restored Default Zoom', image=zoomDefaultIcon, compound=LEFT, accelerator='Ctrl + 0')

# adding menu items to Help menu
helpMenu.add_command(label='View Help', image=viewHelpIcon, compound=LEFT, )
helpMenu.add_command(label='Send Feedback',command=send_feedback, image=sendFeedbackIcon, compound=LEFT)
helpMenu.add_command(label='About Tempopad', command=aboutHelp, image=aboutIcon, compound=LEFT)

# Cascading the menu Bar to the root windows
menuBar.add_cascade(label='File', underline=0, menu=fileMenu)
menuBar.add_cascade(label='Edit', underline=0, menu=editMenu)
menuBar.add_cascade(label='Format', underline=1, menu=formatMenu)
menuBar.add_cascade(label='View', underline=0, menu=viewMenu)
menuBar.add_cascade(label='Help', underline=0, menu=helpMenu)

# Setting the Tool bar menu 
# Font Style Element
fontElement = StringVar()
font_family = font.families()
fontBox = ttk.Combobox(toolBar, width=25, textvariable=fontElement, state='readonly')
fontBox['values'] = font_family
fontBox.current(font_family.index('Arial CE'))
fontBox.grid(row=0, column=0, ipady=3, padx=5, pady=5)

# Font SizeElement
sizeElement = StringVar()
fontSize = ttk.Combobox(toolBar, width=25, textvariable=sizeElement, state='readonly')
fontSize['values'] = tuple(range(8, 42, 2))
fontSize.current(2)
fontSize.grid(row=0, column=1, ipady=3, padx=5, pady=5)

# Toobar Buttons Element Initializing
btnUnderline = ttk.Button(toolBar, image=UnderlineIcon)
btnUnderline.grid(row=0, column=2, pady=5, padx=5)

btnBold = ttk.Button(toolBar, image=BoldIcon)
btnBold.grid(row=0, column=3, pady=5, padx=5)

btnItalic = ttk.Button(toolBar, image=ItalicIcon)
btnItalic.grid(row=0, column=4, pady=5, padx=5)

btnLeft = ttk.Button(toolBar, image=LeftIcon)
btnLeft.grid(row=0, column=5, pady=5, padx=5)

btnCenter = ttk.Button(toolBar, image=CenterIcon)
btnCenter.grid(row=0, column=6, pady=5, padx=5)

btnRight = ttk.Button(toolBar, image=RightIcon)
btnRight.grid(row=0, column=7, pady=5, padx=5)

btnJustify = ttk.Button(toolBar, image=JustifyIcon)
btnJustify.grid(row=0, column=8, pady=5, padx=5)

# Status Bar Element
lblEmpty = Label(statusBar, text='   ', width=50)
lblEmpty.grid(row=0,column=0)
Label(statusBar, text='Line:').grid(row=0, column=1)
lblLine =Label(statusBar, text='0').grid(row=0, column=2)
Label(statusBar, text='Col:').grid(row=0, column=3, padx=5)
Label(statusBar, text='100%').grid(row=0, column=4, padx=5)
Label(statusBar, text='Windows(CRLF)').grid(row=0, column=5, padx=5)
Label(statusBar, text='UTF-8').grid(row=0, column=6, padx=10)
# binding event to the root
root.bind_all('<Control-q>', quit)




#binding controls
root.bind('<Control o>',open_file)
root.bind('<Control n>', new_file)
root.bind('<Control s>', save_file)
root.bind('<Control-Shift-S>', save_as_file)
# compile and view notepad using mainloop
root.mainloop()
