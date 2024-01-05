from tkinter import *

raiz = Tk()

raiz.title("ventana de pruebas Bernal")
raiz.config(bg="blue")

# Configura el color de fondo directamente al crear el Frame
miFrame = Frame(raiz, bg="blue", width=500, height=500) 

miFrame.pack(side="right")

raiz.mainloop()
