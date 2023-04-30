from tkinter import *
import tkinter as tk
root = Tk()
root.geometry("1000x600+200+50")
root.title("supermaket application")
root.resizable(FALSE, FALSE)
root.configure(background="#333")
frame2 = Frame(root, background="#333", padx=10, pady=10)
frame2.place(x=0, y=0, width=300, height=500)
frameentry = Frame(root, background="#333")
frameentry.place(x=10, y=40, width=200, height=500)
# --------------------------function-----------------------------
# frame to add the bill
frame10 = Frame(root, background="#333")
frame10.place(x=570, y=15, height=390, width=400)
# add entry
sn = Entry(frame10, background="#333", fg="white", font=("verdana", 13))
sn.place(x=90, y=110, width=220, height=30)
sn.insert(0, "you ordered ")

# some information


def say():
    import pyttsx3
    say = pyttsx3.init()
    say.say("welcome in my supermarket ")
    say.runAndWait()


labeinfo = Label(frame10, text="Bill list", fg="white",
                 bg="#222", font=("verdana", 13), padx=100, pady=6)
labeinfo.pack()
labeldescripton = Label(frame10, text="welcome in red store \nsupermarket",
                        fg="white", bg="#333", font=("verdana", 13))
labeldescripton.place(x=110, y=50)
# function to define
titlename = Label(frame2, text="Food", font=(
    "verdana", 13), fg="white", bg="#333")
titlename.place(x=10, y=10)
# start making the order"
labs1 = Label(frameentry, text="Bread", fg="white",
              bg="#333", font=("verdana", 13))
labs1.place(x=12, y=40)
# entry to set the quantity of the number
sg1 = Entry(frameentry)
sg1.place(x=15, y=70, width=120, height=20)
labs2 = Label(frameentry, text="candy", fg="white",
              bg="#333", font=("verdana", 13))
labs2.place(x=12, y=90)
sg2 = Entry(frameentry)
sg2.place(x=16, y=120, width=120, height=20)
lasb3 = Label(frameentry, text="hamburger", fg="white",
              bg="#333", font=("verdana", 13))
lasb3.place(x=12, y=150)
eng3 = Entry(frameentry)
eng3.place(x=14, y=180, width=120, height=20)
lasgb4 = Label(frameentry, text="hotdog", fg="white",
               bg="#333", font=("verdana", 13))
lasgb4.place(x=12, y=200)
en5d = Entry(frameentry)
en5d.place(x=14, y=230, width=120, height=20)
lasb5g = Label(frameentry, text="sandwich", fg="white",
               bg="#333", font=("verdana", 13))
lasb5g.place(x=12, y=250)
en5s = Entry(frameentry)
en5s.place(x=14, y=280, width=120, height=20)
calctotalbtn = Button(frameentry, text="Total", fg="white", bg="red", font=(
    "verdana", 13), cursor="hand2", command=say)
calctotalbtn.place(x=14, y=330, width=120, height=30)
# frame5
framentry6 = Frame(root, background="#333")
framentry6.place(x=200, y=22, width=200, height=360)
# fram for entry to display it in the same size
frameentru7 = Frame(root, background="#333")
frameentru7.place(x=200, y=43, width=200, height=360)
label6 = Label(framentry6, text="Grocery", fg="white",
               bg="#333", font=("verdana", 13))
label6.place(x=12, y=0)
labs1 = Label(frameentru7, text="Rice", fg="white",
              bg="#333", font=("verdana", 13))
labs1.place(x=12, y=40)
# entry to set the quantity of the number
s1 = Entry(frameentru7)
s1.place(x=15, y=70, width=120, height=20)
labs2 = Label(frameentru7, text="food oil", fg="white",
              bg="#333", font=("verdana", 13))
labs2.place(x=12, y=90)
s2 = Entry(frameentru7)
s2.place(x=16, y=120, width=120, height=20)
lasb3 = Label(frameentru7, text="salt", fg="white",
              bg="#333", font=("verdana", 13))
lasb3.place(x=12, y=150)
en3 = Entry(frameentru7)
en3.place(x=14, y=180, width=120, height=20)
lasb4 = Label(frameentru7, text="wheat", fg="white",
              bg="#333", font=("verdana", 13))
lasb4.place(x=12, y=200)
en4 = Entry(frameentru7)
en4.place(x=14, y=230, width=120, height=20)
lasb5 = Label(frameentru7, text="sugar", fg="white",
              bg="#333", font=("verdana", 13))
lasb5.place(x=12, y=250)
en5 = Entry(frameentru7)
en5.place(x=14, y=280, width=120, height=20)
calctotalbtn = Button(frameentru7, text="Total", fg="white",
                      bg="red", font=("verdana", 13), cursor="hand2")
calctotalbtn.place(x=14, y=330, width=120, height=30)
# others frame

framentry7 = Frame(root, background="#333")
framentry7.place(x=400, y=22, width=200, height=360)
titlename = Label(framentry7, text="others", font=(
    "verdana", 13), fg="white", bg="#333")
titlename.place(x=10, y=-3)
# fram for entry to display it in the same size
frameentru7 = Frame(root, background="#333")
frameentru7.place(x=400, y=43, width=200, height=360)
label6 = Label(framentry6, text="Grocery", fg="white",
               bg="#333", font=("verdana", 13))
label6.place(x=12, y=0)
labs1 = Label(frameentru7, text="Gatorade", fg="white",
              bg="#333", font=("verdana", 13))
labs1.place(x=12, y=40)
# entry to set the quantity of the number
s12 = Entry(frameentru7)
s12.place(x=15, y=70, width=120, height=20)
labs2 = Label(frameentru7, text="coke", fg="white",
              bg="#333", font=("verdana", 13))
labs2.place(x=12, y=90)
s22 = Entry(frameentru7)
s22.place(x=16, y=120, width=120, height=20)
lasb3 = Label(frameentru7, text="jiuce", fg="white",
              bg="#333", font=("verdana", 13))
lasb3.place(x=12, y=150)
en33 = Entry(frameentru7)
en33.place(x=14, y=180, width=120, height=20)
lasb4 = Label(frameentru7, text="waffer", fg="white",
              bg="#333", font=("verdana", 13))
lasb4.place(x=12, y=200)
en44 = Entry(frameentru7)
en44.place(x=14, y=230, width=120, height=20)
lasb5 = Label(frameentru7, text="bisciut", fg="white",
              bg="#333", font=("verdana", 13))
lasb5.place(x=12, y=250)
en55 = Entry(frameentru7)
en55.place(x=14, y=280, width=120, height=20)
calctotalbtn = Button(frameentru7, text="Total", fg="white",
                      bg="red", font=("verdana", 13), cursor="hand2")
calctotalbtn.place(x=14, y=330, width=120, height=30)
# other frame


def insetsdata():
    s1.insert(0, 0)
    s2.insert(0, 0)
    en3.insert(0, 0)
    en4.insert(0, 0)
    en5.insert(0, 0)
    sg1.insert(0, 0)
    sg2.insert(0, 0)
    eng3.insert(0, 0)
    en5d.insert(0, 0)
    en5s.insert(0, 0)
    s12.insert(0, 0)
    s22.insert(0, 0)
    en33.insert(0, 0)
    en44.insert(0, 0)
    en55.insert(0, 0)


insetsdata()


def calculatevalues():
    calc1 = s1.get()
    calc2 = s2.get()
    calc3 = en3.get()
    calc4 = en4.get()
    calc5 = en5.get()
    # gro content
    calc6 = sg1.get()
    calc7 = sg2.get()
    calc8 = eng3.get()
    calc9 = en5d.get()
    calc10 = en5s.get()
    calc11 = s12.get()
    calc12 = s22.get()
    calc13 = en33.get()
    calc14 = en44.get()
    calc15 = en55.get()

    if calc1 == 0 and calc2 == 0 and calc3 == 0 and calc4 == 0 and calc5 == 0:
        print("the value is  equals to"+0)
    elif calc1 != 0 or calc2 != 0 or calc3 != 0 or calc4 != 0 or calc5 != 0:
        labeltotal = Label(
            frame10, text="the total value of this product \n ordered is:", fg="white", bg="#333")
        labeltotal.place(x=100, y=150)
        x = calc1*5 and calc2*5 and calc3*5 and calc4*5 and calc5*5
        valueentry = Entry(frame10, background="#333", fg="white")
        valueentry.place(x=120, y=190, width=120, height=30)
        valueentry.insert(0, x)

        def qr_code_maker():
            import qrcode
            from PIL import ImageTk, Image
            datavalue = valueentry.get()
            combineddata = f"{datavalue}"
            qr_image = qrcode.make(combineddata)
            tk_image = ImageTk.PhotoImage(qr_image)
            labshow = Label(frame10, image=tk_image)
            labshow.configure(image=tk_image)
            labshow.place(x=60, y=40)
        buttonadd = Button(frame10, text="Add to cart", fg="white",
                           bg="red", cursor="hand2", command=qr_code_maker)
        buttonadd.place(x=120, y=240, width=120, height=30)

    elif calc6 == 0 and calc7 == 0 and calc8 == 0 and calc9 == 0 and calc10 == 0:
        print("the value is equal to"+0)
    elif calc6 != 0 or calc7 != 0 or calc8 != 0 or calc9 == 0 or calc10 != 0:
        labeltotal = Label(
            frame10, text="the total value of this product \n ordered is:", fg="white", bg="#333")
        labeltotal.place(x=120, y=150)
        x = calc6*3 and calc7*3 and calc8*3 and calc9*3 and calc10*3
        valueentry = Entry(frame10, background="#333", fg="white")
        valueentry.place(x=120, y=190, width=120, height=30)
        valueentry.insert(0, x)

        def qr_code_maker():
            import qrcode
            from PIL import ImageTk, Image
            datavalue = valueentry.get()
            combineddata = f"{datavalue}"
            qr_image = qrcode.make(combineddata)
            tk_image = ImageTk.PhotoImage(qr_image)
            labshow = Label(frame10, image=tk_image, bg="#333", fg="white")
            labshow.configure(image=tk_image)
            labshow.place(x=26, y=40)
        buttonadd = Button(frame10, text="Add to cart", fg="white",
                           bg="red", cursor="hand2", command=qr_code_maker)
        buttonadd.place(x=120, y=240, width=120, height=30)
    elif calc11 == 0 and calc12 == 0 and calc13 == 0 and calc14 == 0 and calc15 == 0:
        print("the value is equal to"+0)
    elif calc11 != 0 or calc12 != 0 or calc13 != 0 or calc14 == 0 or calc15 != 0:
        labeltotal = Label(
            frame10, text="the total value of this product \n ordered is:", fg="white", bg="#333")
        labeltotal.place(x=120, y=150)
        x = calc11*10 and calc12*10 and calc13*10 and calc14*10 and calc15*10
        valueentry = Entry(frame10, background="#333", fg="white")
        valueentry.place(x=120, y=190, width=120, height=30)
        valueentry.insert(0, x)

        def qr_code_maker():
            import qrcode
            from PIL import ImageTk, Image
            datavalue = valueentry.get()
            combineddata = f"{datavalue}"
            qr_image = qrcode.make(combineddata)
            tk_image = ImageTk.PhotoImage(qr_image)
            labshow = Label(frame10, image=tk_image)
            labshow.configure(image=tk_image)
            labshow.image_names = tk_image
            labshow.place(x=26, y=40)
        buttonadd = Button(frame10, text="Add to cart", fg="white",
                           bg="red", cursor="hand2", command=qr_code_maker)
        buttonadd.place(x=120, y=240, width=120, height=30)
# ==========================this is the price of the product======================
# food content:bread 3$ candy 4$ hamburger 5$ hotdog 6$ sandwich 7$ for 1piece
# grocery content:rice 10$ food oil :10$ salt:10$ wheat :10$ sugar 10$
# others content gatorade 20$ coke 20$ jiuce 20$ waffer 10$ bisciut 10$
# def clear text inside the entry


def openprogram():
    import tkinter
    import qrcode
    from PIL import ImageTk, Image
    root = Tk()
    root.geometry("190x400")
    root.title("login")
    root.resizable(FALSE, FALSE)
# divide the program into 3
    frame1 = Frame(root, background="#333")
    frame1.place(x=0, y=0, width=250, height=500)
# label definition
    # labe1 = Label(text="supermarket grocery system",
    #           fg="white", bg="#333", font=("Courier", 13))
    # labe1.place(x=360, y=5)
# user details
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
        wb.save("data.xlsx")

    orderbtn = Button(frame1, bg="royalblue", fg="white",
                      text="order now", cursor="hand2", command=save_to_excel)

    orderbtn.place(x=12, y=270, width=140, height=30)
    
# delete data inside the input
    deletebutton = Button(frame1, text="delete",
                          fg="white", bg="red", cursor="hand2", command=deletedata)
    deletebutton.place(x=12, y=320, width=140, height=30)
    root.mainloop()


useren1 = 0
address1 = 0
phonenumberentry = 0
bllentry = 0


def taha():
    pass


# menu frames
menuframe = Frame(root, background="#333")
menuframe.place(x=0, y=430, width=1000, height=140)
# =============================buttons=======================
menulabel = Label(menuframe, text="Total", fg="white",
                  bg="#333", font=("verdana", 13), cursor="hand2")
menulabel.place(x=20, y=0)
# ============lets add label and some entry============
labels = Label(menuframe, text="food:", fg="white",
               bg="#333", font=("verdana", 14))
labels.place(x=20, y=30)
labeen1 = Entry(menuframe,state=DISABLED)
labeen1.place(x=130, y=30, width=120, height=25)
labels2 = Label(menuframe, text="Grocery:", fg="white",
                bg="#333", font=("verdana", 14))
labels2.place(x=20, y=60)
labeen2 = Entry(menuframe,state=DISABLED)
labeen2.place(x=130, y=60, width=120, height=25)
labels2 = Label(menuframe, text="others:", fg="white",
                bg="#333", font=("verdana", 14))
labels2.place(x=20, y=90)
labeen3 = Entry(menuframe,state=DISABLED)
labeen3.place(x=130, y=90, width=120, height=25)
# ==================taxesfor the product=========================
labe1tax = Label(menuframe, text="Food tax:", fg="white",
                 bg="#333", font=("verdana", 14))
labe1tax.place(x=300, y=30)
labeen1tax = Entry(menuframe,state=DISABLED)
labeen1tax.place(x=400, y=33, width=120, height=25)
labe2tax = Label(menuframe, text="gro tax:", fg="white",
                 bg="#333", font=("verdana", 14))
labe2tax.place(x=300, y=60)
labeen2tax = Entry(menuframe,state=DISABLED)
labeen2tax.place(x=400, y=66, width=120, height=25)
labe3tax = Label(menuframe, text="other tax:", fg="white",
                 bg="#333", font=("verdana", 14))
labe3tax.place(x=300, y=94)


labeen3tax = Entry(menuframe,state=DISABLED)
labeen3tax.place(x=400, y=99, width=120, height=25)


def insertingdata():
    labeen1.insert(0, 4)
    labeen2.insert(0, 4)
    labeen3.insert(0, 4)
    labeen1tax.insert(0, 2)
    labeen2tax.insert(0, 2)
    labeen3tax.insert(0, 2)


def cleardata():
    labeen1.delete(0, tk.END)
    labeen2.delete(0, tk.END)
    labeen3.delete(0, tk.END)
    labeen1tax.delete(0, tk.END)
    labeen2tax.delete(0, tk.END)
    labeen3tax.delete(0, tk.END)
    s1.delete(0, tk.END)
    s2.delete(0, tk.END)
    en3.delete(0, tk.END)
    en4.delete(0, tk.END)
    en5.delete(0, tk.END)
    sg1.delete(0, tk.END)
    sg2.delete(0, tk.END)
    eng3.delete(0, tk.END)
    en5d.delete(0, tk.END)
    en5s.delete(0, tk.END)
    s12.delete(0, tk.END)
    s22.delete(0, tk.END)
    en33.delete(0, tk.END)
    en44.delete(0, tk.END)
    en55.delete(0, tk.END)


insertingdata()

# ============buttonns frame to editing the data======
# ==============
btnframes = Frame(root, background="#333")
btnframes.place(x=550, y=470, width=400, height=80)
# function button frame==========


def qiut():
    print("you qiut the program ...")
    root.destroy()


# ========buttons ==========
btn1 = Button(btnframes, text="Total", fg="white", bg="red",
              cursor="hand2", font=("verdana", 13), command=calculatevalues)
btn1.place(x=0, y=0, width=200, height=40)
btn2 = Button(btnframes, text="Generate bill", fg="white", bg="#76EE00",
              cursor="hand2", font=("verdana", 13), command=openprogram)
btn2.place(x=200, y=0, width=200, height=40)
btn3 = Button(btnframes, text="clear", fg="white", bg="#222",
              cursor="hand2", font=("verdana", 13), command=cleardata)
btn3.place(x=0, y=40, width=200, height=40)
btn4 = Button(btnframes, text="exit", fg="white", bg="red",
              cursor="hand2", font=("verdana", 13), command=qiut)
btn4.place(x=200, y=40, width=200, height=40)

root.mainloop()
