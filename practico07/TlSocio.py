from tkinter import *
from practico05.ejercicio_01 import Socio

class TlSocio:
    def __init__(self, root, master, tipo, socio=None):
        self.root = root
        self.master = master
        self.tipo = tipo
        self.frameData = Frame(root)
        self.frameData.grid(column=0, row=0)

        self.entryTextId = StringVar()
        self.entryTextDni = StringVar()
        self.entryTextApellido = StringVar()
        self.entryTextNombre = StringVar()
        self.error = StringVar(value='')

        Label(self.frameData, text="ID").grid(row=0, column=0)
        Label(self.frameData, text="DNI").grid(row=1, column=0)
        Label(self.frameData, text="Apellido").grid(row=2, column=0)
        Label(self.frameData, text="Nombre").grid(row=3, column=0)
        Label(self.frameData, textvariable=self.error).grid(row=4, column=0, padx=8, pady=8, columnspan=2)

        self.entryID = Entry(self.frameData, textvariable=self.entryTextId, state="disabled")
        self.entryID.grid(column=1, row=0)
        self.entryDNI = Entry(self.frameData, textvariable=self.entryTextDni)
        self.entryDNI.grid(column=1, row=1)
        self.entryApellido = Entry(self.frameData, textvariable=self.entryTextApellido)
        self.entryApellido.grid(column=1, row=2)
        self.entryNombre = Entry(self.frameData, textvariable=self.entryTextNombre)
        self.entryNombre.grid(column=1, row=3)

        if self.tipo == 'modificacion':
            self.socio = socio
            self.entryTextId.set(self.socio.id)
            self.entryTextDni.set(self.socio.dni)
            self.entryTextNombre.set(self.socio.nombre)
            self.entryTextApellido.set(self.socio.apellido)

        if self.tipo == 'alta':
            self.entryTextId.set('0')

        self.frameButtons = Frame(root)
        self.frameButtons.grid(column=0, row=1)
        Button(self.frameButtons, text="Guardar", command=self.guardarDatos).grid(row=0, column=0)
        Button(self.frameButtons, text="Cancelar", command=root.destroy).grid(row=0, column=1)

    def guardarDatos(self):
        socio = Socio()
        socio.id = self.entryID.get()
        socio.dni = self.entryDNI.get()
        socio.apellido = self.entryApellido.get()
        socio.nombre = self.entryNombre.get()
        if self.tipo == 'alta':
            resp = self.master.agregar(socio)
            if type(resp) != Socio:
                self.error.set(resp)
            else:
                self.root.destroy()
                self.master.refresh_treeview()

        elif self.tipo == 'modificacion':
            resp = self.master.modificar(socio)
            if type(resp) != Socio:
                self.error.set(resp)
            else:
                self.root.destroy()
                self.master.refresh_treeview()
