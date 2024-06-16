import tkinter as tk

class SumaPorDefecto(tk.Frame):
    __ventana: None
    __primer_numero: None
    __segundo_numero: None
    __resultado: None

    def realizarSuma(self) -> None:
        self.__resultado.delete(0, "end")
        self.__resultado.insert(0, float(self.__primer_numero.get()) + float(self.__segundo_numero.get()))

    def __init__(self, master = None) -> None:
        super().__init__(master, width = 270, height = 10)
        self.__ventana = master
        self.pack()
        self.crearWidgets()
    
    def crearWidgets(self) -> None:
        mostrar_texto_numero1 = tk.Label(self.__ventana, text = "Primer Número")
        mostrar_texto_numero1.pack()
        self.__primer_numero = tk.Entry(self.__ventana)
        self.__primer_numero.pack()
        mostrar_texto_numero2 = tk.Label(self.__ventana, text = "Segundo Número")
        mostrar_texto_numero2.pack()
        self.__segundo_numero = tk.Entry(self.__ventana)
        self.__segundo_numero.pack()
        mostrar_texto_resultado = tk.Label(self.__ventana, text = "Resultado")
        mostrar_texto_resultado.pack()
        self.__resultado = tk.Entry(self.__ventana, background = "green")
        self.__resultado.pack()
        sumar_numeros = tk.Button(self.__ventana, text = "Sumar", command = self.realizarSuma)
        sumar_numeros.pack()

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    ventana_principal.wm_title("Suma de Números")
    aplicacion_sumar = SumaPorDefecto(master = ventana_principal)
    aplicacion_sumar.mainloop()