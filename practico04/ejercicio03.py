from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, root):
        self.FrameM = Frame(root)
        self.FrameM.grid(row=0, column=0, ipady=5, ipadx=5)
        self.framT = Frame(self.FrameM)
        self.framT.grid(column=0, row=0,padx=5,pady=5)
        self.treeview = ttk.Treeview(self.framT, columns="cp")
        self.treeview.grid(column=0, row=0)
        self.agregar_item("Rosario", 2000)
        self.agregar_item("Cordoba", 5000)
        self.agregar_item("San Miguel de Tucuman", 4000)
        self.agregar_item("Chajari", 3228)
        self.agregar_item("Reconquista", 3560)
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("cp", text="Codigo Postal")


    def agregar_item(self, nombre, cp):
        self.treeview.insert("", END, text=nombre, values=cp)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
    exit()
