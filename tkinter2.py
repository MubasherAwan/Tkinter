# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:17:59 2023

@author: iammu
"""

import tkinter
from tkinter import ttk
from tkinter import messagebox

root = tkinter.Tk()
root.title("Inventry Management System")
root.geometry("925x525+230+100")
root.configure(bg ="lightblue")
root.resizable(0,0)

frame = tkinter.Frame(root)
frame.pack(pady=50)

loginFrame = tkinter.LabelFrame(frame)
loginFrame.grid(row=0,column=0)

loginText = tkinter.Label(loginFrame,text="LogIn")
loginText.grid(row=1,column=1,padx=200,pady=5)

entryFrame = tkinter.LabelFrame(frame)
entryFrame.grid(row=1,column=0,sticky="news")

user_name = tkinter.Label(entryFrame,text="User Name")
user_name.grid(row=0,column=0)

root.mainloop()