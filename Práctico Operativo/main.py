from tkinter import *
import time
from random import *

class Juego:
    __ventana: object
    __boton_verde: object
    __boton_rojo: object
    __boton_amarillo: object
    __boton_azul: object
    __lista_colores_maquina: list
    __lista_colores_usuario: list
    __boton: object

    def iluminarColor(self, posicion_color):
        if self.__lista_colores_maquina[posicion_color] == "green":
            self.clickearColorVerde(evento=None)
            time.sleep(self.tiempo)
            self.__ventana.update()
            self.soltarColorVerde(evento=None)
        elif self.__lista_colores_maquina[posicion_color] == "red":
            self.clickearColorRojo(evento=None)
            time.sleep(self.tiempo)
            self.__ventana.update()
            self.soltarColorRojo(evento=None)
        elif self.__lista_colores_maquina[posicion_color] == "yellow":
            self.clickearColorAmarillo(evento=None)
            time.sleep(self.tiempo)
            self.__ventana.update()
            self.soltarColorAmarillo(evento=None)
        elif self.__lista_colores_maquina[posicion_color] == "blue":
            self.clickearColorAzul(evento=None)
            time.sleep(self.tiempo)
            self.__ventana.update()
            self.soltarColorAzul(evento=None)
        time.sleep(self.tiempo)
        self.__ventana.update()

    def generarColorAleatorio(self):
        self.color_generado = choice(["green", "red", "yellow", "blue"])
        self.__lista_colores_maquina.append(self.color_generado)
        print(self.tiempo)
        for posicion_color in range(len(self.__lista_colores_maquina)):
            print(f"Color nro: {posicion_color + 1}: {self.__lista_colores_maquina[posicion_color]}")
            self.iluminarColor(posicion_color)

    def compararColores(self):
        seguir_jugando:bool = True
        posicion_color = 0
        print(self.__lista_colores_maquina)
        print(self.__lista_colores_usuario)
        if len(self.__lista_colores_maquina) != len(self.__lista_colores_usuario):
            seguir_jugando = False
        while seguir_jugando != False and posicion_color < len(self.__lista_colores_maquina):
            if self.__lista_colores_maquina[posicion_color] != self.__lista_colores_usuario[posicion_color]:
                seguir_jugando = False
            posicion_color += 1
        if seguir_jugando != False:
            if self.tiempo >= 0.1:
                self.tiempo -= 0.15
            else:
                self.tiempo = 0.08
            self.__lista_colores_usuario.clear()
            print(f"PASAS DE RONDA\n Nivel: {self.dificultad.get()}\n")
            self.dificultad.set(int(self.dificultad.get()) + 1)
            self.generarColorAleatorio()
        else:
            print("\n\tPERDISTE")
            boton2 = Button(self.__ventana, text = "Comenzar de nuevo", command = self.LimpiarListaColores).grid(column = 1, row = 3)

    def LimpiarListaColores(self):
        self.__lista_colores_maquina.clear()
        self.__lista_colores_usuario.clear()
        self.dificultad.set(1)
        self.generarColorAleatorio()

    def clickearColorVerde(self, evento):
        self.__boton_verde.config(bg = "#87FB81", relief = "sunken")
        self.__boton_verde.bind('<ButtonRelease-1>', self.soltarColorVerde)
    
    def clickearColorRojo(self, evento):
        self.__boton_rojo.config(bg = "#F47878", relief = "sunken")
        self.__boton_rojo.bind('<ButtonRelease-1>', self.soltarColorRojo)

    def clickearColorAmarillo(self, evento):
        self.__boton_amarillo.config(bg = "#F2F587", relief = "sunken")
        self.__boton_amarillo.bind('<ButtonRelease-1>', self.soltarColorAmarillo)

    def clickearColorAzul(self, evento):
        self.__boton_azul.config(bg = "#99B7F9", relief = "sunken")
        self.__boton_azul.bind('<ButtonRelease-1>', self.soltarColorAzul)

    def añadirColorVerde(self, evento):
        color = "green"
        self.__lista_colores_usuario.append(color)

    def añadirColorRojo(self, evento):
        color = "red"
        self.__lista_colores_usuario.append(color)

    def añadirColorAmarillo(self, evento):
        color = "yellow"
        self.__lista_colores_usuario.append(color)

    def añadirColorAzul(self, evento):
        color = "blue"
        self.__lista_colores_usuario.append(color)

    def soltarColorVerde(self, evento):
        time.sleep(0.1)
        self.__boton_verde.config(bg = "#35C812", relief = "raised")

    def soltarColorRojo(self, evento):
        time.sleep(0.1)
        self.__boton_rojo.config(bg = "#ED1313", relief = "raised")

    def soltarColorAmarillo(self, evento):
        time.sleep(0.1)
        self.__boton_amarillo.config(bg = "#D8EC1C", relief = "raised")

    def soltarColorAzul(self, evento):
        time.sleep(0.1)
        self.__boton_azul.config(bg = "#2F6AED", relief = "raised")

    def __init__(self):
        self.__lista_colores_usuario = []
        self.__lista_colores_maquina = []
        self.tiempo = 0.85
        self.__ventana = Tk()
        self.__ventana.iconbitmap("icono_juego_simon.ico")
        self.__ventana.title("SIMON Virtual 3D")
        self.__ventana.geometry("540x800")
        self.__ventana.resizable(0, 0)
        self.__ventana.config(background = "#000000")
        self.dificultad = IntVar()
        self.dificultad.set(0)
        Label(self.__ventana, text = "Puntaje", bg = "#000000", fg = "#F2F2F2").grid(column = 0, row = 0, ipadx = 115)
        self.puntaje = Label(self.__ventana, textvariable = self.dificultad, bg = "#000000", fg = "#F2F2F2").grid(column = 1, row = 0, ipadx = 115)
        boton = Button(self.__ventana, text = "Confirmar", command = self.compararColores).grid(column = 0, row = 3, pady = 40)
        boton = Button(self.__ventana, text = "Empezar", command = self.generarColorAleatorio).grid(column = 1, row = 3, pady = 40)
        '''
        cantidad_colores = 0
        posicion_columna = 0
        posicion_fila = 1
        for color in self.__puntaje:
            cantidad_colores += 1
            if posicion_columna == 2:
                posicion_fila += 1
                posicion_columna = 0
            self.__boton = Canvas(self.__ventana, background = color, relief = "raised", borderwidth = 10, cursor = "hand2")
            self.__boton.config(width = 240, height = 325)
            self.__boton.grid(column = posicion_columna, row = posicion_fila)
            posicion_columna += 1
        '''
        self.__boton_verde = Canvas(self.__ventana, background = "#35C812", highlightbackground = "#262626", relief = "raised", borderwidth = 5, cursor = "hand2")
        self.__boton_verde.config(width = 240, height = 325)
        self.__boton_verde.grid(column = 0, row = 1)
        self.__boton_rojo = Canvas(self.__ventana, background = "#ED1313", highlightbackground = "#262626", relief = "raised", borderwidth = 5, cursor = "hand2")
        self.__boton_rojo.config(width = 240, height = 325)
        self.__boton_rojo.grid(column = 1, row = 1)
        self.__boton_amarillo = Canvas(self.__ventana, background = "#D8EC1C", highlightbackground = "#262626", relief = "raised", borderwidth = 5, cursor = "hand2")
        self.__boton_amarillo.config(width = 240, height = 325)
        self.__boton_amarillo.grid(column = 0, row = 2)
        self.__boton_azul = Canvas(self.__ventana, background = "#2F6AED", highlightbackground = "#262626", relief = "raised", borderwidth = 5, cursor = "hand2")
        self.__boton_azul.config(width = 240, height = 325)
        self.__boton_azul.grid(column = 1, row = 2)
        self.__boton_verde.bind('<ButtonPress-1>', self.clickearColorVerde)
        self.__boton_verde.bind('<ButtonPress-1>', self.añadirColorVerde, add = "+")
        self.__boton_rojo.bind('<ButtonPress-1>', self.clickearColorRojo)
        self.__boton_rojo.bind('<ButtonPress-1>', self.añadirColorRojo, add = "+")
        self.__boton_amarillo.bind('<ButtonPress-1>', self.clickearColorAmarillo)
        self.__boton_amarillo.bind('<ButtonPress-1>', self.añadirColorAmarillo, add = "+")
        self.__boton_azul.bind('<ButtonPress-1>', self.clickearColorAzul)
        self.__boton_azul.bind('<ButtonPress-1>', self.añadirColorAzul, add = "+")
        self.__ventana.mainloop()

if __name__ == '__main__':
    app = Juego()