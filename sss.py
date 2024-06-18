from tkinter import *



class Prueba:
    __ventana: object
    __boton_verde: object
    __boton_rojo: object
    __boton_amarillo: object
    __boton_azul: object
    __lista_colores_maquina: list
    __lista_colores_usuario: list
    __tiempo: float

def __init__(self, gestor_jugadores):
        self.__ventana = Tk()
        self.__ventana.iconbitmap("icono_juego_simon.ico")
        self.__ventana.title("SIMON Virtual 3D")
        self.__ventana.geometry("510x750")
        self.__ventana.resizable(0, 0)
        self.__ventana.config(background = "#000000")
        self.gestor_jugadores = gestor_jugadores
        barra_menu = Menu(self.__ventana)
        menu_opciones = Menu(barra_menu, tearoff = 0)
        menu_opciones.add_command(label = "Puntaje", command = self.mostrarPuntaje)
        menu_opciones.add_command(label = "Salir", command = self.salirPrograma)
        barra_menu.add_cascade(label = "Opciones", menu = menu_opciones)
        self.__ventana.config(menu = barra_menu)
        self.colores_iluminados = {0: "#87FB81", 1: "#F47878", 2: "#F2F587", 3: "#99B7F9"}
        self.colores_originales = {0: "#35C812", 1: "#ED1313", 2: "#D8EC1C", 3: "#2F6AED"}
        self.__lista_colores_usuario = []
        self.__lista_colores_maquina = []
        self.__lista_colores = ["green", "red", "yellow", "blue"]
        self.__tiempo = 0.85
        self.puntuacion = 0
        self.jugador = self.gestor_jugadores.getJugadorActual()
        self.nombre_jugador = self.jugador.getNombreJugador()
        self.diccionario_partidas = self.gestor_jugadores.toJSON()
        if len(self.nombre_jugador) == 0:
            self.jugador.setNombreJugador("Sin_Nombre")
            self.nombre_jugador = self.jugador.getNombreJugador()
        self.puntuacion = self.jugador.getPuntajeJugador()
        self.posicion_color_comparador = 0
        Label(self.__ventana, text = "SIN NOMBRE", bg = "#000000", fg = "#F2F2F2").grid(column = 0, row = 0, padx = 30, sticky = "w")
        self.marcador_puntos = Label(self.__ventana, text = "0", bg = "#000000", fg = "#F2F2F2")
        self.marcador_puntos.grid(column = 1, row = 0, sticky = "n")
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
        self.comenzarSecuencia()
        self.boton = None
        self.__boton_verde.bind('<ButtonPress-1>', lambda event: self.seleccionarColor(self.__boton_verde))
        self.__boton_rojo.bind('<ButtonPress-1>', lambda event: self.seleccionarColor(self.__boton_rojo))
        self.__boton_amarillo.bind('<ButtonPress-1>', lambda event: self.seleccionarColor(self.__boton_amarillo))
        self.__boton_azul.bind('<ButtonPress-1>', lambda event: self.seleccionarColor(self.__boton_azul))
        self.__ventana.mainloop()
    
if __name__ == '__main__':
    Prueba()