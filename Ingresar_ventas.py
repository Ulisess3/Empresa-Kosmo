from tkinter import *
from tkinter.font import Font

def poleron():
    vtn = Toplevel()
    vtn.title("Comprar producto")
    vtn.geometry("400x200")
    vtn.config(bg="lightgray")

    fuente = Font(family ="Bold", size=10)
    titulo = Font(family ="Bold", size=15)

    poleron = PhotoImage(file="imagenes/poleron.png").subsample(6)

    def cancelar():
        vtn.destroy()

    Label(vtn, text="¿Desea comprar este producto?", font=fuente, bg="lightgray").place(x=20, y=10)
    Label(vtn, image=poleron).place(x=20, y=40)
    Label(vtn, text="Polerón Negro", font=titulo).place(x=140, y=40)
    Label(vtn, text="Precio: $15.000", font=fuente, bg="lightgray").place(x=140, y=80)
    Label(vtn, text="Disponibles: 0", font=fuente, bg="lightgray").place(x=140, y=100)
    
    Button(vtn, text="COMPRAR").place(x=200, y=160)
    Button(vtn, text="CANCELAR", command=cancelar).place(x=300, y=160)

    vtn.mainloop()

def pantalon():
    vtn = Toplevel()
    vtn.title("Comprar producto")
    vtn.geometry("400x200")
    vtn.config(bg="lightgray")

    fuente = Font(family ="Bold", size=10)
    titulo = Font(family ="Bold", size=15)

    pantalon = PhotoImage(file="imagenes/pantalon.png").subsample(6)

    def cancelar():
        vtn.destroy()

    Label(vtn, text="¿Desea comprar este producto?", font=fuente, bg="lightgray").place(x=20, y=10)
    Label(vtn, image=pantalon).place(x=20, y=40)
    Label(vtn, text="Pantalón Jeans", font=titulo).place(x=140, y=40)
    Label(vtn, text="Precio: $12.000", font=fuente, bg="lightgray").place(x=140, y=80)
    Label(vtn, text="Disponibles: 0", font=fuente, bg="lightgray").place(x=140, y=100)
    
    Button(vtn, text="COMPRAR").place(x=200, y=160)
    Button(vtn, text="CANCELAR", command=cancelar).place(x=300, y=160)

    vtn.mainloop()