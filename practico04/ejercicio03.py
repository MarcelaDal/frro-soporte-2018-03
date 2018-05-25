from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, root):
        self.frame = Frame(root)
        self.treeview = ttk.Treeview(self.frame, columns="cp")
        self.agregar_item("Rosario", 2000)
        self.agregar_item("Cordoba", 5000)
        self.agregar_item("San Miguel de Tucuman", 4000)
        self.agregar_item("Chajari", 3228)
        self.agregar_item("Reconquista", 3560)
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("cp", text="Codigo Postal")
        self.treeview.pack()
        self.frame.grid(row=0, column=0)


    def agregar_item(self, nombre, cp):
        self.treeview.insert("", END, text=nombre, values=cp)


root = Tk()
app = App(root)
root.mainloop()
exit()
