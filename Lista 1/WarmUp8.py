# Warm up lista 1 POO II

# item 8:
import math

class Coordenada:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, novo_x: int):
        self.__x = novo_x

    @y.setter
    def y(self, novo_y: int):
        self.__y = novo_y

    
    def mostrar_coordendas(self):
        print("As coordenadas desse ponto são ({},{})".format(self.__x, self.__y))

    def distancia_para(self, coord):
        dist = math.sqrt(((coord.x - self.__x)**2) + ((coord.y - self.__y)**2))
        return dist

    def comparar_coordenadas(self, coord):
        dist01 = math.sqrt(((self.__x)**2) + ((self.__y)**2))
        dist02 = math.sqrt(((coord.x)**2) + ((coord.y)**2))

        if dist01 < dist02:
            print(f"A coordenada ({self.__x},{self.__y}) está mais perto centro")
        else:
            print(f"A coordenada ({coord.x},{coord.y}) está mais perto centro")

    def para_polar(self):
        radius = math.sqrt(self.__x**2 + self.__y**2 )
        theta = math.atan(self.__y/self.__x)
        theta = 180 * theta/math.pi
        
        print(f"A coordenada polar de ({self.__x},{self.__y}) é (%0.2f,%0.2f)" % (radius, theta))
        

c1 = Coordenada(-3, -11)
c2 = Coordenada(2, 1)

c1.mostrar_coordendas()
print(f"A distância de ({c1.x},{c1.y}) para ({c2.x},{c2.y}) é {c1.distancia_para(c2)}")
c1.comparar_coordenadas(c2)

c1.para_polar()
c2.para_polar()