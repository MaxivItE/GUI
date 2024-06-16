import tkinter as tk

class SumaPosicionAbsoluta(tk.Frame):
    __ventana: None
    __primer_numero: None
    __segundo_numero: None
    __resultado: None

    def realizarSuma(self) -> None:
        self.__resultado.delete(0, "end")
        self.__resultado.insert(0, float(self.__primer_numero.get()) + float(self.__segundo_numero.get()))

    def __init__(self, master = None) -> None:
        super().__init__(master, width = 450, height = 200)
        self.__ventana = master
        self.__ventana.resizable(width = 0, height = 0)
        self.pack()
        self.agregarWidgets()

    def agregarWidgets(self) -> None:
        mostrar_texto_numero1 = tk.Label(self.__ventana, text = "Primer Número")
        self.__primer_numero = tk.Entry(self.__ventana, width = 10)
        mostrar_texto_numero2 = tk.Label(self.__ventana, text = "Segundo Número")
        self.__segundo_numero = tk.Entry(self.__ventana, width = 10)
        mostrar_texto_resultado = tk.Label(self.__ventana, text = "Resultado")
        self.__resultado = tk.Entry(self.__ventana, background = "green", cursor = "watch", width = 10)
        boton_sumar = tk.Button(self.__ventana, text = "Sumar", cursor = "plus", command = self.realizarSuma)
        boton_salir = tk.Button(self.__ventana, text = "SALIR", bg = "red", command = self.__ventana.destroy)
        mostrar_texto_numero1.place(x = 10, y = 10, width = 100, height = 30)
        self.__primer_numero.place(x = 120, y = 10, height = 25)
        mostrar_texto_numero2.place(x = 10, y = 50, width = 100, height = 30)
        self.__segundo_numero.place(x = 120, y = 50, height = 25)
        mostrar_texto_resultado.place(x = 10, y = 120, width = 100, height = 30)
        self.__resultado.place(x = 120, y = 120, height = 25)
        boton_sumar.place(x = 230, y = 60, width = 150, height = 60)
        boton_salir.place(x = 180, y = 160, width = 100, height = 30)

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    ventana_principal.wm_title("Suma de Números")
    aplicacion_sumar = SumaPosicionAbsoluta(master = ventana_principal)
    aplicacion_sumar.mainloop()