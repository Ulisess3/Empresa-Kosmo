from tkinter import *
from tkinter.font import Font

import Ventas

root = Tk()

root.title("Empresa Kosmos")
root.geometry("600x400")
root.config(bg="lightgray")
root.resizable(0,0)

titulo = Font(family="Bold", size=25)
fuente = Font(family ="Bold", size=15)

poleron = PhotoImage(file="imagenes/poleron.png").subsample(4)
pantalon = PhotoImage(file="imagenes/pantalon.png").subsample(4)

top = Frame(root, bg="gray", width=600, height=60).place(x=0, y=0)

Button(top, text="Iniciar Sesión").place(x=500, y=18)
Button(top, text="Registrarse").place(x=420, y=18)

Label(top, text="KOSMOS", bg="gray", font=titulo).place(x=30, y=10)

#Polerón Negro
Imagen1 = Label(root, image=poleron).place(x=20, y=80)

Label(root, text="Polerón Negro", bg="lightgray", font=fuente).place(x=40, y=248)
Label(root, text="$", bg="lightgray").place(x=80, y=275)
Label(root, text=Ventas.precio_poleron, bg="lightgray").place(x=90, y=275)

vender_poleron = Ventas.poleron

Button(root, command=vender_poleron, text="COMPRAR").place(x=70, y=300)

#Pantalón Jeans
Imagen2 = Label(root, image=pantalon).place(x=220, y=80)

Label(root, text="Pantalón Jeans", bg="lightgray", font=fuente).place(x=240, y=248)
Label(root, text="$", bg="lightgray").place(x=280, y=275)
Label(root, text=Ventas.precio_pantalon, bg="lightgray").place(x=290, y=275)

vender_pantalon = Ventas.pantalon

Button(root, text="COMPRAR", command=vender_pantalon).place(x=270, y=300)

#Boton que usare mas tarde :)
#Button(root, text="ver", command=Ventas.ver).place(x=300, y=340)

root.mainloop()