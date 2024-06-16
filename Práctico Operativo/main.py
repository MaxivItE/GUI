from tkinter import *
import time
from random import *

class Juego:
    __ventana: object
    __boton_verde: object
    __boton_rojo: object
    __boton_amarillo: object
    __boton_azul: object
    __puntaje: dict


    def generarColorAleatorio(self):
        for color in range(self.dificultad):
            color_generado = choice(["green", "red", "yellow", "blue"])
            self.__puntaje[color_generado] += 1
            print(f"Color nro: {color + 1}: {color_generado}")
    
    def compararColores(self):
        seguir_jugando:bool = True
        color_diccionario = 0
        while seguir_jugando != False and color_diccionario < 3:
            if self.__puntaje != self.puntaje_usuario:
                seguir_jugando = False
            color_diccionario += 1
        if seguir_jugando != False:
            print(f"PASAS DE RONDA\n Nivel: {self.dificultad}\n")
            self.dificultad += 1
            self.generarColorAleatorio()
        else:
            print("\n\tPERDISTE")
            boton2 = Button(self.__ventana, text = "Comenzar de nuevo", command = self.volverEmpezar).grid(column = 1, row = 3)
    
    def volverEmpezar(self):
        for color in self.puntaje_usuario:
            self.puntaje_usuario[color] = 0
        for color in self.__puntaje:
            self.__puntaje[color] = 0
        self.dificultad = 1
        self.generarColorAleatorio()

    def ingresarColorVerde(self, evento):
        color = "green"
        self.puntaje_usuario[color] += 1
        self.contador_clicks += 1
        print(color)
        
    def ingresarColorRojo(self, evento):
        color = "red"
        self.puntaje_usuario[color] += 1
        self.contador_clicks += 1
        print(color)

    def ingresarColorAmarillo(self, evento):
        color = "yellow"
        self.puntaje_usuario[color] += 1
        self.contador_clicks += 1
        print(color)

    def ingresarColorAzul(self, evento):
        color = "blue"
        self.puntaje_usuario[color] += 1
        self.contador_clicks += 1
        print(color)

    def __init__(self):
        self.contador_clicks = 0
        self.dificultad = 1
        self.__ventana = Tk()
        self.__ventana.title("Juego")
        self.__ventana.geometry("550x800")
        self.__ventana.resizable(0, 0)
        self.__puntaje = {"green": 0, "red": 0, "yellow": 0, "blue": 0}
        self.puntaje_usuario = {"green": 0, "red": 0, "yellow": 0, "blue": 0}
        Label(self.__ventana, text = "Puntaje", bg = "blue").grid(column = 0, row = 0, ipadx = 115)
        Label(self.__ventana, text = "Puntaje", bg = "green").grid(column = 1, row = 0, ipadx = 115)
        boton = Button(self.__ventana, text = "Confirmar", command = self.compararColores).grid(column = 0, row = 3)
        self.__boton_verde = Canvas(self.__ventana, background = "green", relief = "raised", borderwidth = 10, cursor = "hand2")
        self.__boton_verde.config(width = 240, height = 325)
        self.__boton_verde.grid(column = 0, row = 1)
        self.__boton_rojo = Canvas(self.__ventana, background = "red", relief = "raised", borderwidth = 10, cursor = "hand2")
        self.__boton_rojo.config(width = 240, height = 325)
        self.__boton_rojo.grid(column = 1, row = 1)
        self.__boton_amarillo = Canvas(self.__ventana, background = "yellow", relief = "raised", borderwidth = 10, cursor = "hand2")
        self.__boton_amarillo.config(width = 240, height = 325)
        self.__boton_amarillo.grid(column = 0, row = 2)
        self.__boton_azul = Canvas(self.__ventana, background = "blue", relief = "raised", borderwidth = 10, cursor = "hand2")
        self.__boton_azul.config(width = 240, height = 325)
        self.__boton_azul.grid(column = 1, row = 2)
        self.__boton_verde.bind('<ButtonPress-1>', self.ingresarColorVerde)
        self.__boton_rojo.bind('<ButtonPress-1>', self.ingresarColorRojo)
        self.__boton_amarillo.bind('<ButtonPress-1>', self.ingresarColorAmarillo)
        self.__boton_azul.bind('<ButtonPress-1>', self.ingresarColorAzul)
        self.generarColorAleatorio()
        self.__ventana.mainloop()







if __name__ == '__main__':
    app = Juego()