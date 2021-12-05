# Warm up lista 1 POO II

# item 1:
class Televisao:
    def __init__(self, tamanho: int, marca: str):
        self.__ligada = False
        self.__canal = 2
        
        #item 2:
        self.__tamanho = tamanho
        self.__marca = marca

    @property
    def ligada(self):
        return self.__ligada

    @property
    def canal(self):
        return self.__canal

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def marca(self):
        return self.__marca

    @canal.setter
    def canal(self, novo_canal: int):
        self.__canal = novo_canal


# item 2:
tv1 = Televisao(32, "LG")
tv2 = Televisao(46, "Samsung")

print("A primeira televisão tem", tv1.tamanho, "polegadas e é da marca", tv1.marca)
print("A segunda televisão tem", tv2.tamanho, "polegadas e é da marca", tv2.marca)