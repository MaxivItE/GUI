from ClaseJugador import Jugador
from datetime import datetime
import csv

class GestorJugadores:
    __lista_jugadores: list
    __jugador_actual: object
    __fecha: str
    __hora: str

    def __init__(self):
        self.__lista_jugadores = []
    
    def addJugador(self, nombre_jugador, tiempo_jugador):
        self.getFechaActual()
        unJugador = Jugador(nombre_jugador, tiempo_jugador, self.__fecha, self.__hora)
        self.__jugador_actual = unJugador

    def getJugadorActual(self):
        return self.__jugador_actual
    
    def getFechaActual(self):
        fecha_actual = datetime.now()
        self.__fecha = fecha_actual.strftime('%d/%m/%Y')
        self.__hora = fecha_actual.strftime("%H:%M")

    def guardarPartida(self, unJugador):
        self.getFechaActual()
        self.__lista_jugadores.append(unJugador)
    
    def getListaJugadores(self):
        return self.__lista_jugadores
    
    def toJSON(self):  #Despues de almacenar las partidas en el diccioanrio, se va a la función guardarJSONArhcivo para guardar las partidas en el archivo
        diccionario_partidas = dict(
            __class__ = self.__class__.__name__,
            partidas = [partida.toJSON() for partida in self.__lista_jugadores]
        )
        return diccionario_partidas

    def mostrarDatos(self):
        for i in range(len(self.__lista_jugadores)):
            print(self.__lista_jugadores[i])

    '''def guardarPartidaArchivo(self):
        archivo_puntajes = open("pysimonpuntajes.csv", "w", newline = '')
        posicion_partida = csv.writer(archivo_puntajes)
        for partida in range(len(self.__lista_jugadores)):
            posicion_partida.writerow([self.__lista_jugadores[partida].getNombreJugador(), self.__lista_jugadores[partida].getFechaPartida(), self.__lista_jugadores[partida].getHoraPartida(), self.__lista_jugadores[partida].getPuntajeJugador()])'''