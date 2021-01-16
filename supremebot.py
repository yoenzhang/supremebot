import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
from tkinter import *
from tkinter import ttk
import inventory

items =[]

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def addItem():
    item1 = itemName1.get()
    item2 = colorName1.get()
    tempName = item1 + ' ' + item2

    if (tempName in items):
        nItems.set('That item is already in your cart!' + '\n'
                   'Add a different item or submit your cart!' + '\n'
                   'Number of Items in Cart: ' + str(len(items)))
    else:
        items.append(tempName)
        nItems.set('Number of Items in Cart: ' + str(len(items)))
        itemList = ''
        for item in items:
            itemList = itemList + item + '\n'
        cItems.set('Items in Cart: ' + '\n' + itemList)

def remItem():
    if len(items) == 0:
        cItems.set('There are no items in your cart currently!')
    elif len(items) == 1:
        cItems.set('Items in Cart: Nothing')
        del items[-1]
    else:
        del items[-1]
        nItems.set('Number of Items in Cart: ' + str(len(items)))
        itemList = ''
        for item in items:
            itemList = itemList + item + '\n'
        cItems.set('Items in Cart: ' + '\n' + itemList)

def subCart():
    cart = open("cart.txt", 'w+')
    for item in items:
        print(items)
        file = open('supremeproducts.txt', 'r')
        for line in file:
            if item in line:
                link = line.split(' ')
                link = link[-1][:-1]
                cart.write(link + '\n')
                break
    nItems.set('Your cart was submitted!')
    tItems.set('Resubmit Cart')

def clearCart():
    cart = open("cart.txt", 'w+')
    items=[]
    nItems.set('Number of Items In Cart: 0')
    cItems.set('Items in Cart: Nothing')

def subForm():
    form1 = a1.get()
    form2 = b1.get()
    form3 = c1.get()
    form4 = d1.get()
    form5 = e1.get()
    form6 = f1.get()
    form7 = g1.get()
    form8 = h1.get()
    form9 = i1.get()
    form10 = j1.get()
    form11 = k1.get()
    settings = open('setting.txt', 'w+')
    settings.write(form1 + '\n')
    settings.write(form2 + '\n')
    settings.write(form3 + '\n')
    settings.write(form4 + '\n')
    settings.write(form5 + '\n')
    settings.write(form6 + '\n')
    settings.write(form7 + '\n')
    settings.write(form8 + '\n')
    settings.write(form9 + '\n')
    settings.write(form10 + '\n')
    settings.write(form11 + '\n')
    sItems.set('Resubmit Settings')

    popup = tk.Tk()
    popup.minsize(300,75)
    popup.wm_title("!")
    label = ttk.Label(popup, text='Your Settings Were Succesfully Submitted!')
    label.pack()
    label.place(relx=.5, rely=.15, anchor="center")
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    B1.place(relx=.5, rely=.55, anchor="center")

    popup.mainloop()


def runBot():
    exec(open('surpemescript.py').read())

root = tk.Tk()
nItems = tk.StringVar()
cItems = tk.StringVar()
tItems = tk.StringVar()
sItems = tk.StringVar()

root.minsize(1000, 800)
root.title("SUPREME BOT")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Home')
tabControl.add(tab2, text='Cart')
tabControl.add(tab3, text='Settings')
tabControl.add(tab4, text='Run Bot')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1,
          text="Welcome! Before you run this bot you should know about a couple of things!" + '\n'
               "1) Make sure you have completed both the cart and the settings tab!" + '\n'
               "2) Makes sure you have installed all the required files" + '\n'
               "3) This bot is not professionally made, use at your own risk," + '\n'
               "     all infomation is locally stored on your computer so I cannot see it!" + '\n'
               "4) Good Luck and Have Fun Shopping!").place(relx=.5, rely=.2, anchor="center")



ttk.Label(tab2,
          text="Please fill out the form below to add items to your cart" + '\n'
               "Make sure you spell your items EXACTLY as they appear on the website" + '\n'
               "Including the color!" + '\n'
               "SUBMIT your cart after you add all items, you can modify your cart after you submit as well!!" + '\n'
               "Lastly, as Supreme does not allow for duplicate items to be purchased," + '\n'
               "make sure there are no duplicates in your cart! ").place(relx=.5, rely=.15, anchor="center")

itemName = ttk.Label(tab2, text="Item Name?: ").place(relx=.3, rely=.35, anchor="center")
color = ttk.Label(tab2, text="Color?: ").place(relx=.3, rely=.425, anchor="center")

itemName1 = ttk.Entry(tab2)
itemName1.place(relx=.55, rely=.35, anchor="center")
colorName1 = ttk.Entry(tab2)
colorName1.place(relx=.55, rely=.425, anchor="center")

clearItem = ttk.Button(tab2, text='Clear Cart', command=clearCart).place(relx=.3, rely=.5, anchor="center")
submitCart = ttk.Button(tab2, textvariable=tItems, command=subCart).place(relx=.3, rely=.575, anchor="center")
tItems.set('Submit Cart')
addItem = ttk.Button(tab2, text='Add Item', command=addItem).place(relx=.55, rely=.5, anchor="center")
removeItem = ttk.Button(tab2, text='Remove Last Item', command=remItem).place(relx=.55, rely=.575, anchor="center")
numItems = ttk.Label(tab2,textvariable=str(nItems)).place(relx=.3, rely=.65, anchor="center")
nItems.set('Number of Items In Cart: ' + str(len(items)))
countItems = ttk.Label(tab2,textvariable=str(cItems)).place(relx=.55, rely=.65, anchor="center")
cItems.set('Items in Cart: Nothing')



ttk.Label(tab3,
          text="Please fill out the form below to ensure your information is filled correctly" + '\n'
               "Make sure you enter your information as suggested!").place(relx=.5, rely=.15, anchor="center")

name = ttk.Label(tab3, text="Full Name?: ").place(relx=.35, rely=.25, anchor="center")
email = ttk.Label(tab3, text="Email Address?: ").place(relx=.35, rely=.3, anchor="center")
tel = ttk.Label(tab3, text="Telephone Number?: ").place(relx=.35, rely=.35, anchor="center")
street = ttk.Label(tab3, text="Street Name?: ").place(relx=.35, rely=.4, anchor="center")
apt = ttk.Label(tab3, text="Apt/Unit/Suite? (Optional): ").place(relx=.35, rely=.45, anchor="center")
zip = ttk.Label(tab3, text="Zip?: ").place(relx=.35, rely=.5, anchor="center")
city = ttk.Label(tab3, text="City?: ").place(relx=.35, rely=.55, anchor="center")
state = ttk.Label(tab3, text="State/Province? (eg. Florida = FL): ").place(relx=.35, rely=.6, anchor="center")
country = ttk.Label(tab3, text="Country? (USA, CANADA, or MEXICO): ").place(relx=.35, rely=.65, anchor="center")
credit = ttk.Label(tab3, text="Credit Card Number?: ").place(relx=.35, rely=.7, anchor="center")
exp = ttk.Label(tab3, text="Expirary Date? (eg. MM/YYYY): ").place(relx=.35, rely=.75, anchor="center")
cvv = ttk.Label(tab3, text="CVV?: ").place(relx=.35, rely=.8, anchor="center")

a1 = ttk.Entry(tab3)
a1.place(relx=.65, rely=.25, anchor="center")
b1 = ttk.Entry(tab3)
b1.place(relx=.65, rely=.3, anchor="center")
c1 = ttk.Entry(tab3)
c1.place(relx=.65, rely=.35, anchor="center")
d1 = ttk.Entry(tab3)
d1.place(relx=.65, rely=.4, anchor="center")
e1 = ttk.Entry(tab3)
e1.place(relx=.65, rely=.45, anchor="center")
f1 = ttk.Entry(tab3)
f1.place(relx=.65, rely=.5, anchor="center")
g1 = ttk.Entry(tab3)
g1.place(relx=.65, rely=.55, anchor="center")
h1 = ttk.Entry(tab3)
h1.place(relx=.65, rely=.6, anchor="center")
i1 = ttk.Entry(tab3)
i1.place(relx=.65, rely=.65, anchor="center")
j1 = ttk.Entry(tab3)
j1.place(relx=.65, rely=.7, anchor="center")
k1 = ttk.Entry(tab3)
k1.place(relx=.65, rely=.75, anchor="center")
l1 = ttk.Entry(tab3)
l1.place(relx=.65, rely=.8, anchor="center")

submitForm = ttk.Button(tab3, textvariable=sItems, command=subForm).place(relx=.65, rely=.85, anchor="center")
sItems.set('Submit Settings')

ttk.Label(tab4,
          text="Before hitting run make sure:" + '\n'
               "1) Your cart has every item that you want!" + '\n'
               "2) Your settings has been filled out correctly!" + '\n'
               "3) You have enough money on your card for all the items!").grid(column=0,
                          row=0,
                          padx=30,
                          pady=30)

runBot = tk.Button(tab4, text='Run Bot', padx=10, pady=5, fg='black', bg='#FF0100', command=runBot).grid(row=1, column=0)


root.mainloop()