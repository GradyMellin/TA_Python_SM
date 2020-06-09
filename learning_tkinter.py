
import tkinter
from tkinter import *


class ParentWindow(Frame):
     def __init__ (self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='#000')

        self.varFName = StringVar()
        self.varLName = StringVar()
        
        #Label First Name
        self.lblFName = Label(self.master, text = "First Name: ", font=("Helvetica",16), fg='green', bg='black')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))
        
        #Label Last Name
        self.lblLName = Label(self.master, text = "Last Name: ", font=("Helvetica",16), fg='green', bg='black')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        #Label Display
        self.lblDisplay = Label(self.master, text = "", font=("Helvetica",16), fg='green', bg='black')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        
        #Text Box First Name
        self.txtFName = Entry(self.master, text = self.varFName, font=("Helvetica",16), fg='black', bg='green')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        
        #Text Box Last Name
        self.txtLName = Entry(self.master, text = self.varLName, font=("Helvetica",16), fg='black', bg='green')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        #Buttons
        self.btnSubmit = Button(self.master, text='Submit', width= 10, height = 2, bg='black', fg='green', bd='5px', command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(10,0), pady=(30,0), sticky=NE)
        self.btnCancel = Button(self.master, text='Cancel', width= 10, height = 2, bg='black', fg='red', bd='5px', command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,100), pady=(30,0), sticky=NE)

     def submit(self):
          fn = self.varFName.get()
          ln = self.varLName.get()
          self.lblDisplay.config(text="Hello {} {}!".format(fn,ln))

     def cancel(self):
          self.master.destroy()









          

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
