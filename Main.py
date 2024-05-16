from tkinter import *

root = Tk()

root.title("Empresa Kosmos")
root.geometry("600x400")
root.config(bg="lightgray")
root.resizable(0,0)

top = Frame(root, bg="gray", width=600, height=60).place(x=0, y=0)
Button(top, text="Iniciar Sesión").place(x=500, y=18)

root.mainloop()