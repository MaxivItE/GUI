import tkinter as tk
from tkinter.ttk import Combobox
from libFracMix import FracMix
from tkinter import messagebox

class InferazFracciones(tk.Frame):
    __ventana_princial: None
    __primer_entero: None
    __primer_numerador: None
    __primer_denominador: None
    __segundo_entero: None
    __sengundo_numerador: None
    __segundo_denominador: None
    __resultado: None
    __calcular: None

    def __init__(self, master = None) -> None:
        super().__init__(master, width = 320, height = 170, bg = "#9EDA9E")
        self.__ventana_princial = master
        self.__ventana_princial.resizable(width = 0, height = 0)
        self.__ventana_princial.iconbitmap("icono_fracciones_mixtas.ico") 
        self.pack()
        self.crearWidgets()

    def calcularFraccion(self):
        primer_fraccion = FracMix(int(self.__primer_entero.get()), int(self.__primer_numerador.get()), int(self.__primer_denominador.get()))
        segunda_fraccion = FracMix(int(self.__segundo_entero.get()), int(self.__sengundo_numerador.get()), int(self.__segundo_denominador.get()))
        match self.opcion.current():
            case 0: resultado_fraccion = primer_fraccion + segunda_fraccion
            case 1: resultado_fraccion = primer_fraccion - segunda_fraccion
            case 2: resultado_fraccion = primer_fraccion * segunda_fraccion
            case 3: resultado_fraccion = primer_fraccion / segunda_fraccion
        self.__resultado.delete(0, "end")
        self.__resultado.insert(0, resultado_fraccion)

    def ingresarOpcionSalida(self):
        if messagebox.askokcancel(message = "¿Desea Salir del programa?", title = "Saliendo") == True:
            self.__ventana_princial.destroy()

    def definirLabelWidgets(self):
        tk.Label(self, text = "Fracción 1", bg = "#9EDA9E").place(x = 50, y = 0)
        tk.Label(self.ventana_primer_entero, text = "En", bg = "#8FD0F1").pack(side = "left")
        tk.Label(self.ventana_primera_fraccion, text = "Num", bg = "#F1FE4C").grid(row = 0, column = 2)
        tk.Label(self.ventana_primera_fraccion, text = "Den", bg = "#F1FE4C").grid(row = 1, column = 2)

        tk.Label(self, text = "Fracción 2", bg = "#9EDA9E").place(x = 210, y = 0)
        tk.Label(self.ventana_segundo_entero, text = "En", bg = "#8FD0F1").pack(side = "left")
        tk.Label(self.ventana_segunda_fraccion, text = "Num", bg = "#F1FE4C").grid(row = 0, column = 2)
        tk.Label(self.ventana_segunda_fraccion, text = "Den", bg = "#F1FE4C").grid(row = 1, column = 2)
        tk.Label(self, text = "Operación:", bg = "#9EDA9E").place(x = 20, y = 80)
        tk.Label(self, text = "Resultado:", bg = "#9EDA9E").place(x = 20, y = 115)

    def definirFrameWidgets(self):
        self.ventana_primera_fraccion = tk.Frame(self.__ventana_princial, text = "Algo",bg = "#F1FE4C")
        self.ventana_primer_entero = tk.Frame(self.ventana_primera_fraccion, background = "#8FD0F1")
        self.ventana_segunda_fraccion = tk.Frame(self.__ventana_princial, bg = "#F1FE4C")
        self.ventana_segundo_entero = tk.Frame(self.ventana_segunda_fraccion, background = "#8FD0F1")

        self.ventana_primera_fraccion.place(x = 20, y = 20, width = 120, height = 50)
        self.ventana_primer_entero.grid(row = 0, column = 0, rowspan = 2)
        self.ventana_segunda_fraccion.place(x = 180, y = 20, width = 120, height = 50)
        self.ventana_segundo_entero.grid(row = 0, column = 0, rowspan = 2)

    def definirEntyWidgets(self):
        self.__primer_entero = tk.Entry(self.ventana_primer_entero, width = 4)
        self.__primer_numerador = tk.Entry(self.ventana_primera_fraccion, width = 4)
        self.__primer_denominador = tk.Entry(self.ventana_primera_fraccion, width = 4)
        self.__segundo_entero = tk.Entry(self.ventana_segundo_entero, width = 4)
        self.__sengundo_numerador = tk.Entry(self.ventana_segunda_fraccion, width = 4)
        self.__segundo_denominador = tk.Entry(self.ventana_segunda_fraccion, width = 4)
        self.__resultado = tk.Entry(self.__ventana_princial, width = 15)

        self.__primer_entero.pack(side = "right", pady = 10, padx = 5)
        self.__primer_numerador.grid(row = 0, column = 1)
        self.__primer_denominador.grid(row = 1, column = 1)
        self.__segundo_entero.pack(side = "right", pady = 10, padx = 5)
        self.__sengundo_numerador.grid(row = 0, column = 1)
        self.__segundo_denominador.grid(row = 1, column = 1)
        self.__resultado.place(x = 90, y = 115)
    
    def definirButtonWidgets(self):
        self.__calcular = tk.Button(self.__ventana_princial, text = "Calcular", command = self.calcularFraccion)
        self.salir = tk.Button(self.__ventana_princial, text = "SALIR", bg = "#DA2020", command = self.ingresarOpcionSalida)

        self.__calcular.place(x = 200, y = 80, width = 80, height = 25)
        self.salir.place(x = 200, y = 110, width = 80, height = 35)

    def crearWidgets(self) -> None:
        self.definirFrameWidgets()
        self.definirLabelWidgets()
        self.definirEntyWidgets()
        self.definirButtonWidgets()
        self.lista_opciones = ["Suma", "Resta", "Multiplicación", "División"]
        self.opcion = Combobox(self.__ventana_princial, width = 13, values = self.lista_opciones, state = "readonly")
        self.opcion.place(x = 90, y = 80)
        self.opcion.current(0)

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    ventana_principal.wm_title("Fracciones Mixtas")
    app_fracciones = InferazFracciones(master = ventana_principal)
    app_fracciones.mainloop()