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
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        self.pixels = [
            [color(0, 0, 255) for x in range(self.width)] 
            for y in range(self.height)
    ]


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
                f.write(self.pixels[x][y])
        f.close()

    def point(self,x,y):
        self.pixels[x][y] = color(0,0,0)

        
    



render = Render(800,600)
render.point(0,0)
render.write("prueba.bmp")










        





