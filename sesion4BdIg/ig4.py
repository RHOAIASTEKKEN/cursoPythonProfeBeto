from tkinter import *

def addnumber():
    res1 = int(entry1.get()) + int(entry2.get())
    mytext.set(res1)

ws = Tk()
ws.title("Suma python Tovar")
ws.geometry("500x500")

mytext = StringVar()

Label(ws, text="Numero 1").grid(row=0, sticky=W)
Label(ws, text="Numero 2").grid(row=1, sticky=W)
Label(ws, text="Resultado").grid(row=3, sticky=W)

result = Label(ws, text="", textvariable=mytext)
result.grid(row=3, column=1, sticky=W)

entry1 = Entry(ws)
entry2 = Entry(ws)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button = Button(ws, text="Calcular", command=addnumber)
button.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

ws.mainloop()
