import tkinter as tk
from tkinter import *
class screen():
    
    def __init__(self,ho):
        self.ho = ho
        self.usernameEntry = None
        self.passwordEntry = None
    
    def openScreen(self):
        global rootPage 
        rootPage= tk.Tk()
        rootPage.title("ENCODER")
        rootPage.geometry("500x500")
        # defination of labels
        self.userLabel = Label(rootPage, width=20, height=4, 
                  text="User Name  :", font="Ariel 12 bold")

        self.userLabel.place(x=10,y=30)
  

        self.userPassword = Label(rootPage, width=20, height=4, 
                  text="Password  :", font="Ariel 12 bold")

        self.userPassword.place(x=10,y=90)
        #---------------------------------------------------------

        # defination of entries
        self.usernameEntry = Entry(rootPage,width=15, font="bold")
        self.usernameEntry.place(x=185, y=60)

        self.passwordEntry = Entry(rootPage,width=15, font="bold", show="*")
        self.passwordEntry.place(x=185, y=120)
        #--------------------------------------------------------
       
        #defination of button
        self.loginButton = Button(rootPage,text="LOGİN", width=20, font="bold", command=self.ifOnclick)
        self.loginButton.place(x=160, y=285)
        #---------------------------------------------------------
        rootPage.mainloop()
        
    def ifOnclick(self):
        self.x= self.usernameEntry.get()
        self.y= self.passwordEntry.get()
        self.ho.setUser(self.x,self.y)
        self.ho.hashing()
        self.ho.userControl()
        
    
    
        
# PascalCase
# camelCase
# snake_case
# shish-kebab-case
# UPPER_PASCAL_CASE
    
        
    

            