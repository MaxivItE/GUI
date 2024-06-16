from tkinter import *  #Tkinter es un "puente" entre Python y la librería TCL/TK  
#Con el import * se importará todas las clases o paquetes de la librería Tkinter
#Frame es el organizador o el aglutinador de elementos que tendrá dentro la ventana 
# #Widgets son los elementos que tendrá nuestra ventana, pueden ser desde botones y cuadros de textos hasta el mismo Frame

def mensaje():
    print("Mensaje del botón")


if __name__ == '__main__':
    ventana = None  #Es la raiz donde se escrtucturará cómo se verá la ventana de inicio graficamente
    ventana = Tk()  #Es la clase de la raiz, se crea el inicio o la base de la ventana
    ventana.geometry("650x350")  #Le dará un tamaño especificado a la ventana creada
    ventana.iconbitmap("icono_boca_juniors.ico")  #Mostrará una imagen en formato .ico a la ventana
    ventana.title("Ventana de Pruebas")  #Mostrará el nombre del título de la ventana
    ventana.config(background = "blue")  #Le dará un color especificado en ingles a la ventana creada
    ventana.resizable(width = 1, height = 1)  #Limita las delimitaciones que pueda desplegar la ventana, resizable(Ancho = True/False, Largo = True/False)
    label = Label(ventana, text = "Este es un [Label] tkinter")  #Crea un widget donde mostrará un texto en la ventana
    label.pack()
    boton = Button(ventana, text = "Preciona este [Button] para mensaje", command = mensaje)  #Crea un widget donde mostrará un botón presionable en la ventana
    boton.pack()  #Posiciona los widgets creados dentro de la ventana
    ventana.mainloop()  #Mantiene la ventana abierta en un bucle infinito, tambíen debé atender todo el tiempo a los eventos de los widgets configurados(Siempre debe ir al final)