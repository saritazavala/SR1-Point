#Laboratorio 1
#Graficas 
#Sara Zavala 18893
#Universidad del Valle

import struct 

def glInit():
    pass
    #inicialice cualquier objeto interno que requiera su software renderer

def glCreateWindow(width, height):
    pass
    # inicialice su framebuffer con un tamaño 

def glViewPort(x, y, width, height):
    pass
    #defina el área de la imagen sobre la que se va a poder dibujar (hint)

def glClear():
    pass
    #llene el mapa de bits con un solo color

def glClearColor(r, g, b):
    #que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
    pass

def  glVertex(x, y) :
    #que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron 
    # con glViewPort glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina 
    # superior derecha. glVertex(-1, -1) la esquina inferior izquierda. 
    pass

def glColor(r, g, b):
    #con la que se pueda cambiar el color con el que funciona glVertex()
    pass

def glFinish():
    #que escriba el archivo de imagen
    pass


