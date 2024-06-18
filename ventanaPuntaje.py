from tkinter import *
from tkinter import ttk
import tkinter as tk
class VentanaPuntajes:
    __ventana_puntajes: object

    def __init__(self):
        self.__ventana_puntajes = Tk()
        self.__ventana_puntajes.geometry("600x255")
        self.__panel_puntajes = ttk.Labelframe(self.__ventana_puntajes, text = "Galeria de Puntajes")
        self.__panel_puntajes.pack(fill = "both", expand = True)
        ttk.Label(self.__panel_puntajes, text = "Jugador").grid(row = 0, column = 0,padx=55)
        ttk.Label(self.__panel_puntajes, text = "Fecha").grid(row = 0, column = 1, padx=55)
        ttk.Label(self.__panel_puntajes, text = "Hora").grid(row = 0, column = 2, padx=55)
        ttk.Label(self.__panel_puntajes, text = "Puntaje").grid(row = 0, column = 3, padx=55)
        self.__panel_lista_puntajes = Frame(self.__panel_puntajes)
        self.__panel_lista_puntajes.grid(row = 1, column = 0)
        self.__panel_lista_puntajes.grid(sticky = "nswe", columnspan=4, rowspan = 4)
        self.lista_puntajes = Listbox(self.__panel_lista_puntajes)
        barra_desplazamiento = tk.Scrollbar(self.__panel_lista_puntajes, command = self.lista_puntajes.yview)
        self.lista_puntajes.config(yscrollcommand = barra_desplazamiento.set)
        barra_desplazamiento.pack(side = RIGHT, fill = Y)
        self.lista_puntajes.pack(side = LEFT, fill = BOTH, expand = 1)
        ttk.Button(self.__ventana_puntajes, text = "cerrar").pack()
        self.__ventana_puntajes.mainloop()

if __name__ == '__main__':
    VentanaPuntajes()