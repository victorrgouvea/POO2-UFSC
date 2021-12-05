# Warm up lista 1 POO II

# item 3:
class Televisao:
    def __init__(self, tamanho: int, marca: str, canal: int):
        self.__ligada = False
        self.__canal = canal
        self.__tamanho = tamanho
        self.__marca = marca
        
        # item 4:
        self.__canal_minimo = 1
        self.__canal_maximo = 99     

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
    
    # item 3 e 4:
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

tv1 = Televisao(32, "LG", 98)

tv1.muda_canal_para_cima()
print("O canal é", tv1.canal)

tv1.muda_canal_para_cima()
print("O canal é", tv1.canal)