#pip install tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from forex_python.converter import CurrencyRates
#GUI
root = tk.Tk()
 
root.title("Currency converter:Geeks")
 
Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)
 
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency converter :GeeksForGeeks ',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
 
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
 
variable1.set("currency")
variable2.set("currency")
#function To For Real Time Currency Conversion
def convertnaira():
    if Amount1_field.get()=="":
        tkinter.messagebox.showinfo("Error","Enter amount")
        return
    if Amount1_field.get():
        print(Amount1_field.get())
        print(From.get())
        print(To.get())
        if From.get()=="NGN" and To.get()=="USD":
            print(Amount1_field.get())
            total=int(Amount1_field.get())/860
            Amount2.set(total)
        elif From.get()=="USD" and To.get()=="NGN":
            total=int(Amount1_field.get())*860
            Amount2.set(total)
        
        


 
# def RealTimeCurrencyConversion():

#     c = CurrencyRates()
 
#     from_currency = variable1.get()
#     to_currency = variable2.get()
 
#     if (Amount1_field.get() == ""):
#         tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
 
#     elif (from_currency == "currency" or to_currency == "currency"):
#         tkinter.messagebox.showinfo("Error !!",
#                                     "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
 
#     else:
#         new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
#         new_amount = float("{:.4f}".format(new_amt))
#         Amount2_field.insert(0, str(new_amount))
 
#clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 
From=StringVar()
To=StringVar()
Amount2=StringVar()
CurrenyCode_list =("INR", "USD", "CAD", "CNY", "DKK", "EUR","NGN")
# Currency_value=["INR", "USD", "CAD", "CNY", "DKK", "EUR","NGN"]

 
root.configure(background='#e6e5e5')
root.geometry("700x400")
 
Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)
 
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
 
# FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
# ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
 
# FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
# ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
FromCurrency_option=ttk.Combobox(root, values=CurrenyCode_list,textvariable=From,state='readonly',width=23)
ToCurrency_option=ttk.Combobox(root, values=CurrenyCode_list,textvariable=To,state='readonly',width=23)
# FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky="e",rowspan=1)
# ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky="e")
FromCurrency_option.place(relx=0.41,rely=0.32)
ToCurrency_option.place(relx=0.41,rely=0.38)



Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
 
Amount2_field = tk.Entry(root,textvariable=Amount2)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=convertnaira)
Label_9.grid(row=6, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
 
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)
 
 
root.mainloop()