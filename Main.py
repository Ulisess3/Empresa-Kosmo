from tkinter import *
from tkinter.font import Font

root = Tk()

root.title("Empresa Kosmos")
root.geometry("600x400")
root.config(bg="lightgray")
root.resizable(0,0)
letra = Font(family="Bold", size=25)

top = Frame(root, bg="gray", width=600, height=60).place(x=0, y=0)

Button(top, text="Iniciar Sesión").place(x=500, y=18)
Button(top, text="Registrarse").place(x=420, y=18)

Label(top, text="KOSMOS", bg="gray", font=letra).place(x=30, y=10)
Label(root, text="*aquí estarán los productos*").place(x=250, y=200)

root.mainloop()