from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
import subprocess
from tkinter import scrolledtext
root=Tk()
root.geometry("1200x600+80+40")
root.title("pharmacy")
root.resizable(FALSE,FALSE)
billframe = Frame(root,background="white")
root.iconbitmap("taha.ico")
billframe.place(x=900,y=0,height=600,width=400)
framebutton = Frame(billframe,background="#fff")
framebutton.place(x=0,y=500,width=400,height=150)
# function
def message_users():
     messagebox.showinfo("Message", "welcome in the pharmacy stores")
message_users()
def exit_program():
    root.destroy()
    print("the program destroyed right now")
def delete():
    if spins == "" and spins2 == "" and spins3 == "" and spins4 == "" and spins5 == "" and spins6 == "" and spins7 == "" and spins8 == "" and spins9 == "" and spins10 == "" and spins11=="" and spins12 == "":
        messagebox.showinfo("Message", "no data to deleted ")
        button1.config(state=DISABLED)
    else:
        spins.delete(0,tk.END)
        spins2.delete(0,tk.END)
        spins3.delete(0,tk.END)
        spins4.delete(0,tk.END)
        spins5.delete(0,tk.END)
        spins6.delete(0,tk.END)
        spins7.delete(0,tk.END)
        spins8.delete(0,tk.END)
        spins9.delete(0,tk.END)
        spins10.delete(0,tk.END)
        spins11.delete(0,tk.END)
        spins12.delete(0,tk.END)
        print("the data has been deleted")
def insertdata():
    framesinsert=Frame(billframe,background="#222")
    framesinsert.place(x=0,y=0,width=400,height=500)
    value = int(spins.get())
    if value == "":
       messagebox.showerror("error","no content ordered right now")
    elif spins.get()!=0:
        labels1 = Label(framesinsert,text="you ordered  histamed\n",fg="white",bg="#222",font=("verdana",13))
        labels1.place(x=20,y=20)
        messagebox.showinfo("Success", "the order has added to the cart try other order")
    value2 = int(spins2.get())
    if  value2!="":
        labels2 = Label(framesinsert,text="you ordered  motilium\n",fg="white",bg="#222",font=("verdana",13))
        labels2.place(x=20,y=40)
    elif value2=="":
        messagebox.showwarning("Warning","order the order to added to cart")
    value3=int(spins3.get())
    if value3 == "":
        messagebox.showerror("Error","no order ordered")
    elif value3 != "":
        labels3 = Label(framesinsert,text="you ordered  panadol\n",fg="white",bg="#222",font=("verdana",13))
        labels3.place(x=20,y=60)
    value4 = int(spins4.get())
    if value4 != "" and value == "" and value2 == "" and value3 == "":
        messagebox.showinfo("Error","no order ordered")
    elif value4 != "":
        labels4 = Label(framesinsert,text="you ordered  profinal\n",fg="white",bg="#222",font=("verdana",13))
        labels4.place(x=20,y=80)
    value5 = int(spins5.get())
    if value5 != "":
        labels5 = Label(framesinsert,text="you ordered  vitamin a\n",fg="white",bg="#222",font=("verdana",13))
        labels5.place(x=20,y=100)
    elif value5 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    value6 = int(spins6.get())
    if value6 == "":
         messagebox.showerror("Error","the entry is empty order an order")
    elif value6 != "":
        labels6 = Label(framesinsert,text="you ordered  vitamin c\n",fg="white",bg="#222",font=("verdana",13))
        labels6.place(x=20,y=120)
    value7 = int(spins7.get())
    if value7 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    elif value7 != "":
        labels7 = Label(framesinsert,text="you ordered  vitamin d\n",fg="white",bg="#222",font=("verdana",13))
        labels7.place(x=20,y=140)
    value8 = int(spins8.get())
    if value8 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    elif value8!="":
        labels8 = Label(framesinsert,text="you ordered  ABC\n",fg="white",bg="#222",font=("verdana",13))
        labels8.place(x=20,y=140)
    value9 = int(spins9.get())
    if value9 == "":
         messagebox.showerror("Error","the entry is empty order an order")
    elif value9 != "":
        labels9 = Label(framesinsert,text="you ordered  ABC\n",fg="white",bg="#222",font=("verdana",13))
        labels9.place(x=20,y=160)
    value10 = int(spins10.get())
    if value10 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    elif value10!=0:
        labels10 = Label(framesinsert,text="you ordered  omni c\n",fg="white",bg="#222",font=("verdana",13))
        labels10.place(x=20,y=180)
    value11 = int(spins11.get())
    if value11 == "":
         messagebox.showerror("Error","the entry is empty order an order")
    elif value11 != "":
        labels11 = Label(framesinsert,text="you ordered  advil\n",fg="white",bg="#222",font=("verdana",13))
        labels11.place(x=20,y=180)
    value12 = int(spins12.get())
    if value12 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    elif value12!="":
        labels12 = Label(framesinsert,text="you ordered  lipitor\n",fg="white",bg="#222",font=("verdana",13))
        labels12.place(x=20,y=200)
    value13 = int(spins12.get())
    if value12 == "":
        messagebox.showerror("Error","the entry is empty order an order")
    elif value12!="":
        labels12 = Label(framesinsert,text="you ordered  panadol syrup\n",fg="white",bg="#222",font=("verdana",13))
        labels12.place(x=20,y=200)
    label14 = Label(framesinsert,text="--------------------------------------------------------",fg="white",bg="#222")
    label14.place(x=0,y=220)
    label15=Label(framesinsert,text="Total:",fg="white",bg="#222",font=("verdana",11))
    label15.place(x=20,y=250)
    
    def calctotal():
        total = (value+value2+value3+value4+value5+value8+value6+value7+value9+value10+value11+value12)*10
        label1message=Label(framesinsert,text=total,fg="white",bg="#222",font=("verdana",11))
        label1message.place(x=76,y=250)
    calctotal()
    def qr_code_maker():
            import qrcode
            from PIL import ImageTk, Image
            datavalue = spins.get()
            datavalue2 = spins2.get()
            datavalue3 = spins3.get()
            datavalue4 = spins4.get()
            datavalue5 = spins5.get()
            datavalue6 = spins6.get()
            datavalue7 = spins7.get()
            datavalue8 = spins8.get()
            datavalue9 = spins9.get()
            datavalue10 = spins10.get()
            datavalue11 = spins11.get()
            datavalue12 = spins12.get()
            combineddata = f"{datavalue,datavalue2,datavalue3,datavalue4,datavalue5,datavalue6,datavalue7,datavalue8,datavalue9,datavalue10,datavalue11,datavalue12}"
            qr_image = qrcode.make(combineddata)
            tk_image = ImageTk.PhotoImage(qr_image)
            labshow = Label(framesinsert, image=tk_image)
            labshow.configure(image=tk_image,background="#222")
            labshow.place(x=0, y=0,width=400,height=500)
    
    threads=threading.Thread(target=qr_code_maker)
    threads.start()
def gettotal():
    if spins ==0 or spins2 == 0 or spins3==0 or spins4 == 0 or spins5==0 or spins6==0 or spins7 ==0 or spins8==0 or spins9==0 or spins10==0 or spins11==0 or spins12==0:
        def disable_button():
            button3.config(state=DISABLED)
        disable_button()

        openprogram()
    
def openprogram():
    import tkinter
    import qrcode
    from PIL import ImageTk, Image
    root = Tk()
    root.geometry("180x370")
    root.title("ordered product")
    root.configure(background="green")
    root.iconbitmap("taha.ico")
    root.resizable(FALSE, FALSE)
# divide the program into 3
    frame1 = Frame(root, background="#333")
    frame1.place(x=0, y=0, width=250, height=500)
    username = Label(frame1, text="Customer Name:", font=(
        "Courier", 13), fg="white", bg="#333")
    username.place(x=10, y=20)
    useren1 = Entry(frame1)
    useren1.place(x=12, y=50, width=140, height=20)
# user address
    address = Label(frame1, text="address:", fg="white",
                    bg="#333", font=("Courier", 13))
    address.place(x=12, y=80)
    address1 = Entry(frame1)
    address1.place(x=12, y=110, width=140, height=20)
# user phone number
    phonenumber = Label(frame1, text="phone number:", font=(
        "Courier", 13), fg="white", bg="#333")
    phonenumber.place(x=12, y=140)
    phonenumberentry = Entry(frame1)
    phonenumberentry.place(x=12, y=170, width=140, height=20)
# bill code
    billcode = Label(frame1, text="bill code:", fg="white",
                     bg="#333", font=("Courier", 13))
    billcode.place(x=12, y=200)
    bllentry = Entry(frame1)
    bllentry.place(x=12, y=230, height=20, width=140)
# order now button

    

    def generaterandomnumber():
        import random
        promo_code = str(random.randint(1, 100)).zfill(
            2) + str(random.randint(0, 99999999)).zfill(8)
        bllentry.delete(0, tk.END)
        bllentry.insert(0, promo_code)
    generaterandomnumber()

    def deletedata():
        useren1.delete(0, tk.END)
        address1.delete(0, tk.END)
        phonenumberentry.delete(0, tk.END)
        bllentry.delete(0, tk.END)

    def save_to_excel():
        from openpyxl import Workbook
        usernames = useren1.get()
        addresses = address1.get()
        phones = phonenumberentry.get()
        billcode = bllentry.get()

        data = [usernames, addresses, phones, billcode]
        wb = Workbook()
        sheet = wb.active
        sheet.append(data)
        wb.save("order.xlsx")

    orderbtn = Button(frame1, bg="royalblue", fg="white",
                      text="order now", cursor="hand2", command=save_to_excel)

    orderbtn.place(x=12, y=270, width=140, height=30)
    
# delete data inside the input
    deletebutton = Button(frame1, text="delete",
                          fg="white", bg="red", cursor="hand2", command=deletedata)
    deletebutton.place(x=12, y=320, width=140, height=30)
    root.mainloop()
button1=Button(framebutton,text="clear",fg="white",bg="#111",font=("verdana",11),cursor="hand2",command=delete)
button1.place(x=0,y=0,width=150,height=50)
button2=Button(framebutton,text="Total",fg="white",bg="green",font=("verdana",11),cursor="hand2",command=insertdata)
button2.place(x=150,y=0,height=50,width=150)
button3=Button(framebutton,text="generate bill",fg="white",bg="#444",font=("verdana",11),cursor="hand2",command=openprogram)
button3.place(x=0,y=50,width=150,height=50)

button4 = Button(framebutton,text="Exit",cursor="hand2",font=("verdana",11),fg="white",bg="red",command=exit_program)
button4.place(x=150,y=50,width=150,height=50) 

product_frame = Frame(root,background="whitesmoke")
scrollbar = tk.Scrollbar(product_frame)
scrollbar.pack(side="right", fill="y")

product_frame.place(x=0,y=0,width=900,height=600)
# =========add product=======================
histamedimage=PhotoImage(file="histameds.png")
motiliumimages=PhotoImage(file="motilium.png")
panadolimages=PhotoImage(file="panadol.png")
profinalsimages=PhotoImage(file="profinals.png")
vitamin_c = PhotoImage(file="vitamin_c.png")
vitamin_a = PhotoImage(file="vitamin_a.png")
vitamin_d = PhotoImage(file="vitamin_d.png")
abc=PhotoImage(file="vitamin_d.png")
advil=PhotoImage(file="abc.png")
omni=PhotoImage(file="omni.png")
panadolsey=PhotoImage(file="panadolse.png")
antibiotics = PhotoImage(file="antibiotics.png")

statin=PhotoImage(file="statin.png")
label1=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=histamedimage)
label1.place(x=20,y=20,width=200,height=100)
spins =Entry(product_frame)
spins.place(x=20,y=140,width=200,height=30)
label2=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=motiliumimages)
label2.place(x=230,y=20,width=170,height=100)
global spins2
spins2=Entry(product_frame)
spins2.place(x=230,y=140,width=170,height=30)
label3=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=panadolimages)
label3.place(x=430,y=20,width=170,height=100)
spins3=Entry(product_frame)
spins3.place(x=430,y=140,width=170,height=30)
label4=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=profinalsimages)
label4.place(x=630,y=20,width=170,height=100)
spins4=Entry(product_frame)
spins4.place(x=630,y=140,width=170,height=30)
# new category
label5=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=vitamin_a)
label5.place(x=20,y=200,width=170,height=100)
spins5=Entry(product_frame)
spins5.place(x=20,y=310,width=170,height=30)
# ======
label6=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=vitamin_c)
label6.place(x=230,y=200,width=170,height=100)
spins6=Entry(product_frame)
spins6.place(x=230,y=310,width=170,height=30)
# ==========================
label7=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=vitamin_d)
label7.place(x=430,y=200,width=170,height=100)
spins7=Entry(product_frame)
spins7.place(x=430,y=310,width=170,height=30)
# ============
label8=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=advil)
label8.place(x=630,y=200,width=170,height=100)
spins8=Entry(product_frame)
spins8.place(x=630,y=310,width=170,height=30)
# ================
label9=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=omni)
label9.place(x=20,y=400,width=170,height=100)
spins9=Entry(product_frame)
spins9.place(x=20,y=510,width=170,height=30)
# ===========
label10=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=antibiotics)
label10.place(x=200,y=400,width=170,height=100)
spins10=Entry(product_frame)
spins10.place(x=200,y=510,width=170,height=30)
label11=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=statin)
label11.place(x=400,y=400,width=170,height=100)
spins11=Entry(product_frame)
spins11.place(x=400,y=510,width=170,height=30)
label12=Label(product_frame,fg="#222",bg="whitesmoke",font=("verdana",12),image=panadolsey)
label12.place(x=630,y=400,width=170,height=100)
spins12=Entry(product_frame)
spins12.place(x=630,y=510,width=170,height=30)
# buttons frame
def sendtoprinter():
    time.sleep(2)
    subprocess.Popen(["python","tests.py"])
    root.destroy()
framesbtn = Frame(root,background="whitesmoke")
framesbtn.place(x=0,y=560,width=900,height=40)
buttonse = Button(framesbtn,text="add sheet to printer",fg="white",bg="royalblue",cursor="hand2",command=sendtoprinter)
buttonse.place(x=300,y=0,width=300,height=30)

# INSERT DATA INSIDE THE ENTRY

root.mainloop()