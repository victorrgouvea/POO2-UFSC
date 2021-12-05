# Warm up lista 1 POO II

# item 9:
import math

class Quadrado:
    def __init__(self, lado: float):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    def area(self):
        return self.__lado * self.__lado


class Retangulo:
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    def area(self):
        return self.__base * self.__altura


class Circulo:
    def __init__(self, raio: float):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
 
    def area(self):
        return math.pi * self.__raio**2

f1 = Quadrado(5)
f2 = Retangulo(6, 4)
f3 = Circulo(3)

print(f"A área é {f1.area()}")
print(f"A área é {f2.area()}")
print(f"A área é {f3.area()}")