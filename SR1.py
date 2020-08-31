#Laboratorio 1
#Graficas 
#Sara Zavala 18893
#Universidad del Valle

import struct 

def char(c):
    return struct.pack('=c', c.encode('ascii'))

# 2 bytes
def word(c):
    return struct.pack('=h', c)

# 4 bytes
def dword(c):
    return struct.pack('=l', c)

def color(red, green, blue):
    return bytes( [blue, green,red ])


class Render(object):

    #Initial values -------------------------------

    def __init__(self, width, height, filename):
        self.width = 0
        self.height = 0
        self.framebuffer = []
        self.change_color = color(0,0,255)
        self.filename = filename
        self.x_position = 0
        self.y_position = 0
        self.ViewPort_height = 0
        self.ViewPort_width = 0
        self.glClear()

    
    #File Header ----------------------------------

    def header(self):
        doc = open(self.filename,'bw')
        doc.write(char('B'))
        doc.write(char('M'))
        doc.write(dword(54 + self.width * self.height * 3))
        doc.write(dword(0))
        doc.write(dword(54))
        self.info(doc)
        
        
    #Info header ---------------------------------------

    def info(self, doc):
        doc.write(dword(40))
        doc.write(dword(self.width))
        doc.write(dword(self.height))
        doc.write(word(1))
        doc.write(word(24))
        doc.write(dword(0))
        doc.write(dword(self.width * self.height * 3))
        doc.write(dword(0))
        doc.write(dword(0))
        doc.write(dword(0))
        doc.write(dword(0))
        
        #Image ----------------------------------
        for x in range(self.width):
            for y in range(self.height):
                doc.write(self.framebuffer[y][x])
        doc.close()

    #Cleans a full image with the color defined in "change_color"
    def glClear(self):
        
        self.framebuffer = [
            [self.change_color for x in range(self.width)]
            for y in range(self.height)
        ]

    #Takes a new color  
    def glClearColor(self, red,blue,green):
        self.change_color = color(red, blue, green)

    #Writes all the doc
    def glFinish(self):
        self.header()
    
    def glColor(self, r, g, b):
        self.change_color = color(r, g, b)

    #Draws a point according ot frameBuffer
    def glpoint(self, x, y):
        self.framebuffer[y][x] = self.change_color

    #Creates a window 
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    #Defines the area where will be able to draw
    def glViewPort(self, x_position, y_position, ViewPort_height, ViewPort_width):
        self.x_position = x_position
        self.y_position = y_position
        self.ViewPort_height = ViewPort_height
        self.ViewPort_width = ViewPort_width

    def glVertex(self, x, y):
        x_Vertex = self.x_position + int(round( self.ViewPort_width/2 + x * self.ViewPort_width/2 ))
        y_Vertex = self.y_position + int(round(self.ViewPort_height/2 + y * self.ViewPort_height/2 ))
        self.glpoint(round(x_Vertex), round(y_Vertex))


#Crear Render
r = Render(100,100, 'FINAL.bmp')
#Crear pantalla
r.glCreateWindow(100,100)
#Se delimita el arrea donde si se va a poder dibujar
r.glViewPort(25, 25, 50 ,50)
#Tomo el bote de pintura de este color
r.glClearColor(255,0,0)
#Echo el bote de pintura y pinto todo
r.glClear()
#Dibujo mi punto en el centrp
r.glColor(0,0,0)
r.glVertex(0,0) 
#Termino y escribo todo
r.glFinish()


        
        
        

