from tkinter import *
broj = 0 
#cuva vrijednost nakon sto se pozove operacija
e = 0 
#unos
operacija = 0 

def da_li_je_prazno():
    return entry.get() == ""
def obrisi(string):
    """ odgovara dugmetu Obrisi -> brise sve sa ulaza"""
    entry.configure(state = "normal")
    entry.delete(0, END)
    entry.insert(0, string)
    entry.configure(state = "readonly")

def submit(vrijednost):
    """ odgovara svakom dugmetu sa brojevima -> ucitava vrijednosti sa ulaza"""
    global e
    entry.configure(state = "normal")
    e = str(entry.get()) + str(vrijednost)
    obrisi(e)

def racunaj(operator):
    entry.configure(state = "normal")
    global operacija 
    operacija = operator
    if da_li_je_prazno():
        obrisi("")
    else:
        global broj
        broj = float(entry.get()) 
        obrisi("")
       
def procenat():
    entry.configure(state = "normal")
    global broj
    if da_li_je_prazno():
        obrisi("")
    else:
        broj = float(entry.get()) / 100
        obrisi(str(broj))

def rezultat():
    """ odgovara dugmetu jednako -> postavlja rezultat operacije"""
    global broj
    global e
    entry.configure(state = "normal")
    e = entry.get()
    if da_li_je_prazno():
        obrisi("")
    else:
        entry.delete(0, END)
        if operacija == "sabiranje":
            _rezultat = broj + float(e)
        elif operacija == "oduzimanje":
            _rezultat = broj - float(e)
        elif operacija == "mnozenje":
            _rezultat = broj * float(e)
        elif operacija == "dijeljenje":
            try:
                _rezultat = broj / float(e)
            except:
                entry.insert(0, "Napravili ste gresku, pokusajte ponovo")
        else:
            _rezultat = broj ** float(e)
        obrisi(_rezultat)
        broj = 0

root = Tk()
root.title("Calculator")
root.geometry("240x375")
root.configure(bg = "white")
root.resizable(False, False)

entry = Entry(root, width = 35, borderwidth = 5, state = "readonly")
entry.grid(row = 0, column = 0, padx = 5, pady = 4, ipady = 3, columnspan = 3)

button1 = Button(root, text = "1", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(1))
button1.grid(row = 1, column = 0)

button2 = Button(root, text = "2", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(2))
button2.grid(row = 1, column = 1)

button3 = Button(root, text = "3", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(3))
button3.grid(row = 1, column = 2)

button4 = Button(root, text = "4", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(4))
button4.grid(row = 2, column = 0)

button5 = Button(root, text = "5", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(5))
button5.grid(row = 2, column = 1)

button6 = Button(root, text = "6", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(6))
button6.grid(row = 2, column = 2)

button7 = Button(root, text = "7", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(7))
button7.grid(row = 3, column = 0)

button8 = Button(root, text = "8", width = 10, height = 3, bg = "#f3c4fb", command = lambda: submit(8))
button8.grid(row = 3, column = 1)

button9 = Button(root, text = "9", width = 10, height = 3,  bg = "#f3c4fb", command = lambda: submit(9))
button9.grid(row = 3, column = 2)

button0 = Button(root, text = "0", width = 10, height = 3, bg = "#e5b3fe", command = lambda: submit(0))
button0.grid(row = 4, column = 0)

button_plus = Button(root, text = "+", width = 10, height = 3, bg = "#e5b3fe", command = lambda: racunaj("sabiranje"))
button_plus.grid(row = 4, column = 1)

button_minus = Button(root, text = "-", width = 10, height = 3, bg = "#e5b3fe", command = lambda: racunaj("oduzimanje") )
button_minus.grid(row = 4, column = 2)

button_puta = Button(root, text = "*", width = 10, height = 3, bg = "#e5b3fe", command = lambda: racunaj("mnozenje"))
button_puta.grid(row = 5, column = 0)

button_podijeljeno = Button(root, text = "/", width = 10, height = 3, bg = "#e5b3fe", command = lambda: racunaj("dijeljenje"))
button_podijeljeno.grid(row = 5, column = 1)

button_modulo = Button(root, text = "%", width = 10, height = 3, bg = "#e5b3fe", command = procenat )
button_modulo.grid(row = 5, column = 2)

button_stepen = Button(root, text = "^", width = 10, height = 3, bg = "#e5b3fe", command = lambda: racunaj("stepen")) 
button_stepen.grid(row = 6, column = 0)

button_jednako = Button(root, text = "=", width = 10, height = 3, bg = "#e5b3fe", command = rezultat)
button_jednako.grid(row = 6, column = 1)

button_obrisi = Button(root, text = "C", width = 10, height = 3, bg = "#e5b3fe", command = lambda : obrisi(""))
button_obrisi.grid(row = 6, column = 2)

root.mainloop()
