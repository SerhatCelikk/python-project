import hashlib
from Constant import const as c
from tkinter import messagebox

class encode():
    def __init__(self):
        self.username = None
        self.password = None
        
    def setUser(self, username, password):
        self.username = username
        self.password = password
    
    def hashing(self):
        self.userHash = hashlib.sha256(self.username.encode("utf-8"))
        self.passHash = hashlib.sha256(self.password.encode("utf-8"))
    # defination of userControl func.
    def userControl(self):
        if self.userHash.hexdigest() == c.usernameHash and self.passHash.hexdigest() == c.passwordHash:
            messagebox.showinfo("Giriş yapıldı", "successful")
        else:
            messagebox.showinfo("Tekrar deneyiniz!!", "incorrect")
    #---------------------------------------------------------
