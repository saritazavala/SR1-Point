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
    return bytes(
        [round(blue * 255), 
        round(green * 255), 
        round(red * 255)]
    )


class Render(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []
        self.actual_color = color(0.5,1,0.7)
        self.glClear()


    def glClear(self):
        self.framebuffer = [
            [self.actual_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def glClearColor(self, red, green, blue ):
        self.actual_color = color(red, green, blue)


    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

    def glColor(self, red, green, blue):
        self.actual_color = color(red, green, blue)

    def glViewPort(self, x, y, width, height):
        self.xViewPort = x
        self.yViewPort = y
        self.widthViewPort = width
        self.heightViewPort = height


    def point(self,x,y):
        self.framebuffer[x][y] = color(0,0,0)

    
    def glVertex(self, x, y):
        x_temp = int(round(self.widthViewPort/2 + x * self.widthViewPort/2))
        y_temp =  int(round(self.heightViewPort/2 + y * self.heightViewPort/2))
        x_point = self.xViewPort + x_temp
        y_point = self.yViewPort + y_temp
        self.point( round(x_point), round(y_point)) 


    def write(self, filename):
        doc = open(filename, 'bw')
        total_size = 14 + 40

        #File header
        doc.write(char('B'))
        doc.write(char('M'))
        doc.write(dword( total_size + self.width + self.height * 3 ))
        doc.write(dword(0))
        doc.write(dword(total_size))

        #info header
        doc.write(dword(40))
        doc.write(dword(self.width))
        doc.write(dword(self.height))
        doc.write(word(1))
        doc.write(word(24))
        doc.write(dword(0))
        doc.write(dword( self.width * self.height * 3 ))
        doc.write(dword(0))
        doc.write(dword(0))
        doc.write(dword(0))
        doc.write(dword(0))

        #Pixel data
        for x in range(self.height):
            for y in range(self.width):
                doc.write(self.framebuffer[x][y])
        doc.close()

#Prueba con un punto en medio
render = Render(100,100)
render.glCreateWindow(100,100)
render.glViewPort(25, 25, 50 ,50)
render.glClearColor(1,0.1,1)
render.glClear()
render.glColor(1,0.1,0.1)
render.glVertex(0, 0) 
render.write("Final.bmp")

