from tkinter import Tk, Label, Entry, Button, Widget

class SumaPosicionRelativa:
    __ventana: Widget
    __primer_numero: Widget
    __segundo_numero: Widget
    __resultado: Widget

    def realizarSuma(self) -> None:
        self.__resultado.delete(0, "end")
        self.__resultado.insert(0, float(self.__primer_numero.get()) + float(self.__segundo_numero.get()))

    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.title("Suma de Números")
        self.__ventana.geometry("450x200")
        mostrar_texto_numero1 = Label(self.__ventana, text = "Primer Número")
        mostrar_texto_numero1.place(relx = 0.03, rely = 0.03, relwidth = 0.25, relheight = 0.13)
        self.__primer_numero = Entry(self.__ventana)
        self.__primer_numero.place(relx = 0.3, rely = 0.03, relwidth = 0.2, relheight = 0.13)
        mostrar_texto_numero2 = Label(self.__ventana, text = "Segundo Número")
        mostrar_texto_numero2.place(relx = 0.03, rely = 0.25, relwidth = 0.25, relheight = 0.15)
        self.__segundo_numero = Entry(self.__ventana)
        self.__segundo_numero.place(relx = 0.3, rely = 0.25, relwidth = 0.2, relheight = 0.13)
        mostrar_texto_resultado = Label(self.__ventana, text = "Resultado")
        mostrar_texto_resultado.place(relx = 0.03, rely = 0.70, relwidth = 0.2, relheight = 0.13)
        self.__resultado = Entry(self.__ventana, background = "grey")
        self.__resultado.place(relx = 0.3, rely = 0.70, relwidth = 0.2, relheight = 0.13)
        sumar_numeros = Button(self.__ventana, text = "Sumar", background = "green",command = self.realizarSuma)
        sumar_numeros.place(relx = 0.6, rely = 0.2, relwidth = 0.35, relheight = 0.50)
        self.__ventana.mainloop()