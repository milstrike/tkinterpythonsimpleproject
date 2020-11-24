import tkinter as tk

#list for name and telephone number
nameContact = []
telContact = []
index = 0

def listingContacts():
    contactLists.delete(0, 'end')
    a = 1
    for idx, val in enumerate(nameContact):
        values = val + ", " + telContact[idx]
        contactLists.insert(a, values)
        a += 1

def contactSelector(mw):
    global index
    rts = mw.widget
    index = int(rts.curselection()[0])
    nameInput.delete(0, 'end')
    nameInput.insert(0, nameContact[index])
    telInput.delete(0, 'end')
    telInput.insert(0, telContact[index])

def createKontak():
    nama = nameInput.get()
    telepon = telInput.get()
    nameContact.append(nama)
    telContact.append(telepon)
    listingContacts()
    nameInput.delete(0, 'end')
    telInput.delete(0, 'end')

def removeKontak():
    del nameContact[index]
    del telContact[index]
    listingContacts()
    nameInput.delete(0, 'end')
    telInput.delete(0, 'end')

def updateKontak():
    nama = nameInput.get()
    telepon = telInput.get()
    nameContact[index] = nama
    telContact[index] = telepon
    listingContacts()
    nameInput.delete(0, 'end')
    telInput.delete(0, 'end')

master = tk.Tk()
#app window title
master.title("Simple Contact App")
#change the size of the geometry if the widget is not visible
master.geometry("193x330")

#create input for name input
nameInput = tk.Entry(master)
#create input for telephone number input
telInput = tk.Entry(master)
#create listbox for display the contact list
contactLists = tk.Listbox(master)
#bind the contactlist to the contactSelector function
contactLists.bind('<<ListboxSelect>>', contactSelector)

#put name label
tk.Label(master, text="Name: ").grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.N, ipadx=0, ipady=0)
#put name input entry
nameInput.grid(row=1, column=0, sticky=tk.N, ipadx=0, columnspan=3, ipady=0)
#put telephone label
tk.Label(master, text="Telephone: ").grid(row=2, column=0, columnspan=3, sticky=tk.W)
#put telephone input entry
telInput.grid(row=3, column=0, sticky=tk.N, columnspan=3, ipadx=0, ipady=0)

#put label contact list
tk.Label(master, text="Contact List: ").grid(row=4, column=0, columnspan=3, sticky=tk.W)
#put contact list listbox
contactLists.grid(row=5, column=0, sticky=tk.W+tk.E, padx=2, columnspan=3, pady=0)

#put three button for Create, Update, and Delete
tk.Button(master, text="CREATE", command=createKontak).grid(row=6, column=0, sticky=tk.W+tk.E)
tk.Button(master, text="UPDATE", command=updateKontak).grid(row=6, column=1, sticky=tk.W+tk.E)
tk.Button(master, text="DELETE", command=removeKontak).grid(row=6, column=2, sticky=tk.W+tk.E)


listingContacts()

tk.mainloop()