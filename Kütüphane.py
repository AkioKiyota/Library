from tkinter import *
from tkinter import ttk
import os



def getbook():
    takeBook.state(["disabled"])
    with open("names", "r") as db:
        names = db.read().split("\n")
        ttk.Label(tk, text= "\n".join(names)).pack()
        global inp
        inp = ttk.Entry(tk)
        enterButton = ttk.Button(tk,text="Enter",command=enter)
        inp.pack()
        enterButton.pack()

def enter():
    with open("names", "r") as db:
        names = db.read().split("\n")
    

    with open("states", "r") as db:
        global states
        states = db.read().split("\n")
        book = inp.get()
        debug = ""
        if book in names:
            global ind
            ind = names.index(book)
            state = states[ind]
            if state == "true":
                states[ind] = "false"
                debug = "You got the book!"
                db.close()
                changeDB()
                
            elif state == "false":
                debug = "We do not have that book right now."
            else:
                debug = "ERROR-01" ## ERROR-01: error causes by names file ##
        else:
            debug = "There is no such a book."
        ttk.Label(tk, text=debug).pack()
        
def changeDB():
    os.remove("states")
    with open("states","w") as db:
        db.write("\n".join(states))
    

def giveBook():
    giveeBook.state(["disabled"])
    with open("names", "r") as db:
        global inp
        inp = ttk.Entry(tk)
        enterButton = ttk.Button(tk,text="Enter",command=enter1)
        inp.pack()
        enterButton.pack()

def enter1():
    with open("names", "r") as db:
        names = db.read().split("\n")
    

    with open("states", "r") as db:
        global states
        states = db.read().split("\n")
        book = inp.get()
        debug = ""
        if book in names:
            global ind
            ind = names.index(book)
            state = states[ind]
            if state == "false":
                states[ind] = "true"
                debug = "Thank You!"
                db.close()
                changeDB()
                
            elif state == "true":
                debug = "We Already Have That Book"
            else:
                debug = "ERROR-01" ## ERROR-01: error causes by names file ##
        else:
            debug = "You cant register that a book."
        ttk.Label(tk, text=debug).pack()






tk = Tk()

tk.title("Example")
tk.geometry("700x600+30+30")

mainLabel = ttk.Label(tk, text="What to do?").pack()
takeBook = ttk.Button(tk, text="Take Book", command= getbook)
giveeBook = ttk.Button(tk, text="Give Book", command= giveBook)

takeBook.pack()
giveeBook.pack()

tk.mainloop()