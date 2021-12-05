# Warm up lista 1 POO II

# item 5:
class Televisao:
    def __init__(self, tamanho: int, marca: str, canal: int, canal_minimo=2, canal_maximo=14):
        self.__ligada = False
        self.__canal = canal
        self.__tamanho = tamanho
        self.__marca = marca
        self.__canal_minimo = canal_minimo
        self.__canal_maximo = canal_maximo

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

    @property
    def canal_minimo(self):
        return self.__canal_minimo

    @property
    def canal_maximo(self):
        return self.__canal_maximo

    @canal.setter
    def canal(self, novo_canal: int):
        self.__canal = novo_canal

    @canal_minimo.setter
    def canal_minimo(self, novo_min: int):
        self.__canal_minimo = novo_min

    @canal_maximo.setter
    def canal_maximo(self, novo_max: int):
        self.__canal_maximo = novo_max     


    def muda_canal_para_cima(self):
        if self.__canal == self.__canal_maximo:
            self.__canal = self.__canal_minimo
        else:
            self.__canal += 1

    def muda_canal_para_baixo(self):
        if self.__canal == self.__canal_minimo:
            self.__canal = self.__canal_maximo
        else:
            self.__canal -= 1

# item 6:
tv1 = Televisao(32, "LG", 98, canal_minimo=5, canal_maximo=45)
tv2 = Televisao(46, "Samsung", 2, canal_minimo=7, canal_maximo=34)

print("O canal mínimo da primeira televisão é", tv1.canal_minimo, "e o máximo é", tv1.canal_maximo)
print("O canal mínimo da segunda televisão é", tv2.canal_minimo, "e o máximo é", tv2.canal_maximo)