from tkinter import *
from tkinter import ttk, font
class Aplicacion():
    __ventana: object
    __clave: object
    __usuario: object
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("430x200")
        self.__ventana.resizable(0,0) # la ventana no se puede redimensionar
        self.__ventana.title("Acceso")
        self.fuente = font.Font(weight='bold')
        self.etiq1 = ttk.Label(self.__ventana, text="Usuario:",
        font=self.fuente)
        self.etiq2 = ttk.Label(self.__ventana, text="Contraseña:",
        font=self.fuente)
        self.__mensaje = StringVar()
        self.etiq3 = ttk.Label(self.__ventana, textvariable=self.__mensaje,
        font=self.fuente, foreground='blue')
        self.__usuario = StringVar()
        self.__clave = StringVar()
        self.__usuario.set('')
        self.ctext1 = ttk.Entry(self.__ventana,
        textvariable=self.__usuario, width=30)
        self.ctext2 = ttk.Entry(self.__ventana,
        textvariable=self.__clave, width=30,
        show="*")
        self.separ1 = ttk.Separator(self.__ventana, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.__ventana, text="Aceptar",
        padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.__ventana, text="Cancelar",
        padding=(5,5), command=quit)
        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.separ1.place(x=5, y=145, bordermode=OUTSIDE,
        height=10, width=420)
        self.boton1.place(x=170, y=160)
        self.boton2.place(x=290, y=160)
        self.ctext2.bind('<Button-1>', self.borrar_mensaje)
        self.ctext1.focus_set()
        self.ctext2.bind('<Button-1>', self.borrar_mensaje)
        print("Sali")
        self.__ventana.mainloop()
    def aceptar(self):
        if self.__clave.get() == 'tkinter':
            self.etiq3.configure(foreground='blue')
            self.__mensaje.set("Acceso permitido")
        else:
            self.etiq3.configure(foreground='red')
            self.__mensaje.set("Acceso denegado")
    def borrar_mensaje(self, evento):
        self.__clave.set("")
        self.__mensaje.set("")
        print("Entre")
def testAPP():
    mi_app = Aplicacion()
    return 0
if __name__ == '__main__':
    testAPP()

