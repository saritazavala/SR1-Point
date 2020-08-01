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

def color(r, g, b):
    return bytes([round(b * 255), round(g * 255), round(r * 255)])


class Render(object):

    def __init__(self, width, height):
 
        self.width = width
        self.height = height
        self.framebuffer = []
        self.clear_color = color(0.5,1,0.7)
        self.glClear()

    def glClear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def glClearColor(self, r,g,b):
        self.current_color = color(r, g, b)


    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

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
        self.point(round(x_point),round(y_point)) 


    def write(self, filename):
        f = open(filename, 'bw')

        #File header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14+40+self.width+self.height*3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        #info header
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

        #Pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()


render = Render(100,100)
render.glCreateWindow = (100,100)
render.glColor(1,0.1,0.1)
render.glViewPort(25, 25, 50 ,50)
render.glClearColor(1,0,1)
render.glVertex(0, 0) 

render.write("AhoraSi.bmp")













        





