from tkinter import *
from tkinter.font import Font
import sqlite3
import tkinter.messagebox as messagebox
from tkinter.simpledialog import askinteger
from tkinter import ttk

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
            vtn.destroy()

    Button(vtn, text="COMPRAR", command=comprar).place(x=200, y=160)
    Button(vtn, text="CANCELAR", command=cancelar).place(x=300, y=160)

    vtn.mainloop()

cursor.execute('select * from productos')
datos = cursor.fetchall()

def ver():    
    tabla = ttk.Treeview(columns=("#1","#2","#3","#4"))
    tabla.grid(row=0, column=0)
    tabla.heading("#0", text="", anchor=CENTER)
    tabla.heading("#1", text="ID", anchor=CENTER)
    tabla.heading("#2", text="Nombre", anchor=CENTER)
    tabla.heading("#3", text="Precio", anchor=CENTER)
    tabla.heading("#4", text="Cantidad", anchor=CENTER)

    def borrar_fila():
        seleccion = tabla.selection()
    
        if len(seleccion) != 0:
            fila_id = tabla.item(seleccion)['values'][0]
        
            cursor.execute("DELETE FROM productos WHERE ID=?", (fila_id,))
            con.commit()
        
            tabla.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una fila para borrar.")

    for col in tabla["columns"]:
        tabla.column(col, anchor=CENTER)

    tabla.column("#0", width=0)
    tabla.column("#1", width=100)
    tabla.column("#2", width=200)
    tabla.column("#3", width=150)
    tabla.column("#4", width=150)

    for x in datos:
        tabla.insert("", END, values=x[0:])
    
    f = Frame(bg="white", width=600, height=50, borderwidth=1, relief="sunken").grid(row=1, column=0)

    boton_borrar = Button(f,text="Borrar fila", command=borrar_fila)
    boton_borrar.grid(row=1, column=0)