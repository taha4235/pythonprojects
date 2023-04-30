from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import subprocess
import threading
import time
from tkinter import messagebox
root = Tk()
root.title("login to start shop")
root.geometry("500x500+450+40")
frame1 = Frame(root, background="#fff")
frame1.place(x=0, y=0, width=500, height=300)
images = PhotoImage(file="statin.png")
root.iconbitmap("taha.ico")
frame2 = Frame(root)
frame2.place(x=0, y=300, width=500, height=200)
labelimage = Label(frame1, image=images)
labelimage.place(x=0, y=0, width=500, height=300)
root.resizable(FALSE, FALSE)
frames_buttons = Frame(root)
frames_buttons.place(x=0, y=300, width=500, height=200)
def opens():
    subprocess.Popen(["python", "apps.py"])
    time.sleep(7)
    root.destroy()
entryframes = Frame(root,background="whitesmoke")
entryframes.place(x=0,y=300,width=500,height=300)
entry1 = Entry(entryframes)
entry1.place(x=40,y=30,height=30,width=400)
entry2 = Entry(entryframes)
entry2.place(x=40,y=70,width=400,height=30)

buttons1 = Button(root,text="open systems",fg="white",bg="green",command=opens,cursor='hand2')
buttons1.place(x=150,y=440,width=200,height=40)
root.mainloop()
