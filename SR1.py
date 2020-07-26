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
    return bytes([b, g, r])


class Render(object):

    def __init__(self, width, height):
        self.viewport_x = 0
        self.viewport_y = 0
        self.width = width
        self.height = height
        self.Vheight = 100
        self.Vwidth = 100
        self.framebuffer = []
        self.clear_color = color(255,204,243)
        self.col = color(0,0,0)
        self.glClear()

    def glClear(self):
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def glClearColor(self, r, g, b):
        self.clear_color = color(
            int(round(r*255)),
            int(round(g*255)),
            int(round(b*255)))


    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

    def glColor(self, r,g,b):
        self.col = color(
            int(round(r*255)),
            int(round(g*255)),
            int(round(b*255)))

    def glViewPort(self, height,width,x,y):
        self.Vheight = height
        self.Vwidth = width
        self.viewport_x = x
        self.viewport_y = y



    def point(self,x,y):
        self.framebuffer[x][y] = color(0,0,0)

    
    def glVertex(self, x, y):
        vertex_x = round((x+1) * (self.Vwidth/2) + self.viewport_x)
        vertex_y= round((y+1) * (self.Vheight/2) + self.viewport_y)
        self.point(vertex_x, vertex_y)     


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


render = Render(800,600)
render.glCreateWindow = (300,300)
render.glColor(1,1,0)
render.glViewPort(100, 100, 100 ,100)
render.glClearColor(1,0,1)
render.glVertex(0, 0) 
render.glVertex(1, 0) 

render.write("final.bmp")










        





