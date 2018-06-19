from tkinter import *


class App:
    def __init__(self, master):

        frameA = Frame(master)
        frameA.grid(padx=2, pady=2)
        self.entryText = StringVar()
        self.error = StringVar(value='')
        self.entryA = Entry(frameA, textvariable=self.entryText)
        self.entryA.grid(row=1, pady=2, padx=2, columnspan=4)

        frameB = Frame(master)
        Label(frameB, textvariable=self.error).grid(row=4, column=0, padx=8, pady=8)
        frameB.grid(padx=2, pady=2)
        Button(frameB, text="7", command=lambda: self.agregarNro('7')).grid(row=0, column=0, padx=8, pady=8)
        Button(frameB, text="8", command=lambda: self.agregarNro('8')).grid(row=0, column=1, padx=8, pady=8)
        Button(frameB, text="9", command=lambda: self.agregarNro('9')).grid(row=0, column=2, padx=8, pady=8)
        Button(frameB, text="+", command=lambda: self.agregarNro('+')).grid(row=0, column=3, padx=8, pady=8)
        Button(frameB, text="4", command=lambda: self.agregarNro('4')).grid(row=1, column=0, padx=8, pady=8)
        Button(frameB, text="5", command=lambda: self.agregarNro('5')).grid(row=1, column=1, padx=8, pady=8)
        Button(frameB, text="6", command=lambda: self.agregarNro('6')).grid(row=1, column=2, padx=8, pady=8)
        Button(frameB, text="-", command=lambda: self.agregarNro('-')).grid(row=1, column=3, padx=8, pady=8)
        Button(frameB, text="1", command=lambda: self.agregarNro('1')).grid(row=2, column=0, padx=8, pady=8)
        Button(frameB, text="2", command=lambda: self.agregarNro('2')).grid(row=2, column=1, padx=8, pady=8)
        Button(frameB, text="3", command=lambda: self.agregarNro('3')).grid(row=2, column=2, padx=8, pady=8)
        Button(frameB, text="/", command=lambda: self.agregarNro('/')).grid(row=2, column=3, padx=8, pady=8)
        Button(frameB, text="0", command=lambda: self.agregarNro('0')).grid(row=3, column=0, padx=8, pady=8)
        Button(frameB, text="=", command=self.solve).grid(row=3, column=1, padx=8, pady=8, columnspan= 2)
        Button(frameB, text="*", command=lambda: self.agregarNro('*')).grid(row=3, column=3, padx=8, pady=8)

    def agregarNro(self, nro):
        self.error.set('')
        self.entryText.set(self.entryText.get()+nro)

    def solve(self):
        try:
            self.entryText.set(eval(self.entryText.get()))

        except ZeroDivisionError:
            self.entryText.set('')
            self.error.set('Zero division')

        except SyntaxError:
            self.entryText.set('')
            self.error.set('Syntax error')
        except Exception:
            self.entryText.set('')
            self.error.set('Error')




root = Tk()
app = App(root)
root.mainloop()
exit()
