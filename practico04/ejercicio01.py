from tkinter import *


class App:
    def __init__(self, master):

        frameA = Frame(master)
        frameA.grid(row=0, column=0, padx=2, pady=2)

        Label(frameA, text="Primer operando").grid(row=0, column=0, sticky=W, pady=2, padx=2)
        Label(frameA, text="Segundo operando").grid(row=0, column=1, sticky=W, pady=2, padx=2)
        self.entryA = Entry(frameA)
        self.entryA.grid(row=1, column=0, pady=2, padx=2)
        self.entryB = Entry(frameA)
        self.entryB.grid(row=1, column=1, pady=2, padx=2)

        frameB = Frame(master)
        frameB.grid(row=0, column=1, padx=2, pady=2)
        Button(frameB, text="+", command=self.handleMas).grid(row=0, column=0)
        Button(frameB, text="-", command=self.handleMenos).grid(row=0, column=1)
        Button(frameB, text="/", command=self.handleDiv).grid(row=0, column=2)
        Button(frameB, text="*", command=self.handlePor).grid(row=0, column=3)
        self.resultado = StringVar(value="Resultado: ")
        Label(master, textvariable=self.resultado).grid(row=3, sticky=W)

    def handleMas(self):
        entrys=self.getEntrys()
        if entrys is not None:
            resultado=str(entrys[0]+entrys[1])
            self.mostrarResultado(resultado)


    def handleMenos(self):
        entrys = self.getEntrys()
        if entrys is not None:
            resultado = str(entrys[0] - entrys[1])
            self.mostrarResultado(resultado)

    def handleDiv(self):
        entrys = self.getEntrys()
        if entrys is not None:
            try:
                resultado = str(entrys[0] / entrys[1])
            except ZeroDivisionError:
                resultado = "Error, divisor es zero"
            self.mostrarResultado(str(resultado))

    def handlePor(self):
        entrys = self.getEntrys()
        if entrys is not None:
            resultado = str(entrys[0] * entrys[1])
            self.mostrarResultado(resultado)

    def mostrarResultado(self, resultado):
        self.resultado.set("Resultado: "+str(resultado))

    def getEntrys(self):
        entryA=self.getEntryAsFloat(self.entryA)
        entryB=self.getEntryAsFloat(self.entryB)
        if entryA is not None and entryB is not None:
            return [entryA, entryB]
        else:
            self.mostrarResultado("Error, no es un valor aduecuado")
            return None

    def getEntryAsFloat(self, entry):
        try:
            return float(entry.get())
        except ValueError:
            return None


root = Tk()
app = App(root)
root.mainloop()
exit()
