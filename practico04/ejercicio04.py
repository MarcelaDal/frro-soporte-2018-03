from tkinter import *
from tkinter import ttk
from practico04.ejercicio03 import App


class VentanaAceptar:
    def __init__(self, root, master):
        self.root = root
        self.master = master
        self.frameM = Frame(root)
        self.frameM.grid(column=0, row=0)
        Label(self.frameM, text="Ciudad").grid(row=0, column=0)
        Label(self.frameM, text="Codigo Postal").grid(row=1, column=0)
        self.entryA = Entry(self.frameM)
        self.entryA.grid(column=1, row=0)
        self.entryB = Entry(self.frameM)
        self.entryB.grid(column=1, row=1)
        self.frameA= Frame(root)
        self.frameA.grid(column=0, row=1)
        Button(self.frameA, text="Aceptar",command=self.manejarAdd).grid(row=0, column=0)
        Button(self.frameA, text="Cancelar",command=root.destroy).grid(row=0, column=1)

    def manejarAdd(self):
        self.master.agregar_item(self.entryA.get(), self.entryB.get())
        self.root.destroy()

class App2(App):
    def __init__(self, root):
        super().__init__(root)
        frameB=Frame(self.FrameM)
        frameB.grid(column=1, row=0, pady=5, padx=0, sticky=N)
        Button(frameB, text="Alta", command=self.handleAlta).grid(row=0, column=0)
        Button(frameB, text="Baja", command=self.handleBaja).grid(row=1, column=0)

    def handleAlta(self):
        accept = Toplevel()
        accept.geometry("+400+400")
        VentanaAceptar(accept, self)

    def handleBaja(self):
        if self.treeview.selection() is not "":
            for e in self.treeview.selection():
                self.treeview.delete(e)



if __name__ == "__main__":
    root = Tk()
    root.geometry("+300+300")
    app = App2(root)
    root.mainloop()
    exit()