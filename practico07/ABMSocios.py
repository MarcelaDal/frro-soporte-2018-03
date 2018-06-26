from tkinter import *
from tkinter import ttk
from practico06.capa_negocio import NegocioSocio
from practico07.TlSocio import TlSocio

class ABMSocios(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.grid(row=0, column=0, ipady=5, ipadx=5)
        self.create_components()
        self.create_businesslayer()
        self.cargar_socios()

    def create_components(self):
        self.twSocios = ttk.Treeview(self, columns=("nombre", "apellido", "dni"))
        self.twSocios.grid(column=0, row=0)
        self.twSocios.heading("#0", text="Id")
        self.twSocios.heading("nombre", text="Nombre")
        self.twSocios.heading("apellido", text="Apellido")
        self.twSocios.heading("dni", text="DNI")
        frameControls = Frame(self)
        frameControls.grid(column=0,row=1, sticky='w')
        Button(frameControls,text='Alta',command=self.handleAlta).grid(column=0)
        Button(frameControls, text='Baja',command=self.handleBaja).grid(column=1, row=0)
        Button(frameControls, text='Modificar',command=self.handleModificacion).grid(column=2, row=0)

    def create_businesslayer(self):
        self.capa_negocio = NegocioSocio()

    def cargar_socios(self):
        socios = self.capa_negocio.todos()
        for socio in socios:
            self.twSocios.insert("", END, text=socio.id, values=(socio.nombre, socio.apellido, socio.dni))

    def vaciar_treeview(self):
        self.twSocios.delete(*self.twSocios.get_children())

    def handleAlta(self):
        alta = Toplevel()
        TlSocio(root=alta, master=self, tipo="alta")

    def handleBaja(self):
        for socio in self.twSocios.selection():
            self.capa_negocio.baja(self.twSocios.item(socio)['text'])
        self.vaciar_treeview()
        self.cargar_socios()


    def handleModificacion(self):
        modificacion = Toplevel()
        TlSocio(root=modificacion, master=self, tipo="modificacion")


if __name__ == "__main__":
    father = Tk()
    app = ABMSocios(root=father)
    father.mainloop()
    exit()