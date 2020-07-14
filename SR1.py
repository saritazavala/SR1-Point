#Laboratorio 1
#Graficas 
#Sara Zavala 18893
#Universidad del Valle

import struct 

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(c):
    return struct.pack('=h', c)

def dword(c):
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])


BLACK = color(0, 0, 0)


class Render(object):
    def glInit(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.glclear()
        #inicialice cualquier objeto interno que requiera su software renderer

    def glclear(self):
        self.pixels = [
        [BLACK for x in range(self.width)] 
        for y in range(self.height)
        ]
        #llene el mapa de bits con un solo color

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        # inicialice su framebuffer con un tamaño 

    def glViewPort(self, x, y, width, height):
        pass
        #defina el área de la imagen sobre la que se va a poder dibujar (hint)



    def glClearColor(self, r, g, b):
        self.clear_color = color( round(r*255) ,round(g*255), round(b*255))
        # con la que se pueda cambiar el color con el que funciona glClear(). 


    def  glVertex(self, x, y) :
        #que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron 
        # con glViewPort glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina 
        # superior derecha. glVertex(-1, -1) la esquina inferior izquierda. 
        pass

    def glColor(self, r, g, b):
        #con la que se pueda cambiar el color con el que funciona glVertex()
        pass

    def glFinish(self, filename):

        f = open(filename, 'bw')
        # file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.width):
            for y in range(self.height):
                f.write(self.framebuffer[y][x])

        f.close()
        #que escriba el archivo de imagen
    def point(self, x, y):
        self.framebuffer[y][x] = color(255, 0, 0)


