from tkinter import *
from tkinter.font import Font
import sqlite3
import tkinter.messagebox as messagebox
from tkinter.simpledialog import askinteger

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute('select precio from productos where id = 1')
precio_poleron = cursor.fetchone()

cursor.execute('select cantidad from productos where id = 1')
cantidad_poleron = cursor.fetchone()

def poleron():
    vtn = Toplevel()
    vtn.title("Comprar producto")
    vtn.geometry("400x200")
    vtn.config(bg="lightgray")

    fuente = Font(family ="Bold", size=10)
    titulo = Font(family ="Bold", size=15)

    poleron = PhotoImage(file="imagenes/poleron.png").subsample(6)

    Label(vtn, text="¿Desea comprar este producto?", font=fuente, bg="lightgray").place(x=20, y=10)
    Label(vtn, image=poleron).place(x=20, y=40)
    Label(vtn, text="Polerón Negro", font=titulo).place(x=140, y=40)
    Label(vtn, text="Precio: $", font=fuente, bg="lightgray").place(x=140, y=80)
    Label(vtn, text=precio_poleron, font=fuente, bg="lightgray").place(x=195, y=80)
    Label(vtn, text="Disponibles: ", font=fuente, bg="lightgray").place(x=140, y=100)
    Label(vtn, text=cantidad_poleron, font=fuente, bg="lightgray").place(x=220, y=100)

    def cancelar():
        vtn.destroy()

    def comprar():
        respuesta = askinteger("Cantidad", "¿Cuantos quiere comprar?")
        if respuesta:
            resultado = cantidad_poleron[0]    
            if respuesta > resultado:
                messagebox.showinfo("Info", "No se pudo comprar el producto debido a falta de stock")
                vtn.destroy()
            else:
                messagebox.showinfo("Info", "El producto fue comprado correctamente")
        else:
            messagebox.showinfo("Info", "Compra cancelada")
            vtn.destroy()

    Button(vtn, text="COMPRAR", command=comprar).place(x=200, y=160)
    Button(vtn, text="CANCELAR", command=cancelar).place(x=300, y=160)

    vtn.mainloop()

cursor.execute('select precio from productos where id = 2')
precio_pantalon = cursor.fetchone()

cursor.execute('select cantidad from productos where id = 2')
cantidad_pantalon = cursor.fetchone()

def pantalon():
    vtn = Toplevel()
    vtn.title("Comprar producto")
    vtn.geometry("400x200")
    vtn.config(bg="lightgray")

    fuente = Font(family ="Bold", size=10)
    titulo = Font(family ="Bold", size=15)

    pantalon = PhotoImage(file="imagenes/pantalon.png").subsample(6)

    Label(vtn, text="¿Desea comprar este producto?", font=fuente, bg="lightgray").place(x=20, y=10)
    Label(vtn, image=pantalon).place(x=20, y=40)
    Label(vtn, text="Pantalón Jeans", font=titulo).place(x=140, y=40)
    Label(vtn, text="Precio: $", font=fuente, bg="lightgray").place(x=140, y=80)
    Label(vtn, text=precio_pantalon, font=fuente, bg="lightgray").place(x=195, y=80)
    Label(vtn, text="Disponibles: 0", font=fuente, bg="lightgray").place(x=140, y=100)

    def cancelar():
        vtn.destroy()

    def comprar():
        respuesta = askinteger("Cantidad", "¿Cuantos quiere comprar?")
        if respuesta:
            resultado = cantidad_pantalon[0]    
            if respuesta > resultado:
                messagebox.showinfo("Info", "No se pudo comprar el producto debido a falta de stock")
                vtn.destroy()
            else:
                messagebox.showinfo("Info", "El producto fue comprado correctamente")
        else:
            messagebox.showinfo("Info", "Compra cancelada")
            vtn.destroy()

    Button(vtn, text="COMPRAR", command=comprar).place(x=200, y=160)
    Button(vtn, text="CANCELAR", command=cancelar).place(x=300, y=160)

    vtn.mainloop()