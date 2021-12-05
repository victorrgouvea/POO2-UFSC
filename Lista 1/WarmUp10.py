# Warm up lista 1 POO II

# item 10:
from fractions import Fraction

class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.__numerador = numerador
        self.__denominador = denominador

    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, new: int):
        self.__numerador = new

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, new: int):
        self.__denominador = new

    
    # item A:
    def soma(self, outra):
        soman, somad = (self.__numerador   * outra.denominador +
                        self.__denominador * outra.numerador,
                        self.__denominador * outra.denominador)
        return "%d/%d" %(soman, somad)

    def subtracao(self, outra):
        subn, subd =  (self.__numerador   * outra.denominador -
                       self.__denominador * outra.numerador,
                       self.__denominador * outra.denominador)
        return "%d/%d" %(subn, subd)

    def multiplicacao(self, outra):
        multn, multd =  (self.__numerador * outra.numerador, 
                        self.__denominador * outra.denominador)
        return "%d/%d" %(multn, multd)

    def divisao(self, outra):
        divn, divd =  (self.__numerador * outra.denominador, 
                        self.__denominador * outra.numerador)
        return "%d/%d" %(divn, divd)
    
    # item B:
    def __str__(self):
        return "%d/%d" %(self.__numerador, self.__denominador)

    # item C:
    def inverte(self):
        self.__numerador, self.__denominador = self.__denominador, self.__numerador

    # item D:
    def valor_real(self):
        return self.__numerador / self.__denominador

    # item E:
    @staticmethod
    def criar_fracao(valor):
        valor = str(valor)
        return Fraction(valor)


f1 = Fracao(1, 2)
f2 = Fracao(3, 2)

# item A
print(f"Soma: {f1} + {f2} = {f1.soma(f2)}")
print(f"Substração: {f1} - {f2} = {f1.subtracao(f2)}")
print(f"Multiplicação: {f1} * {f2} = {f1.multiplicacao(f2)}")
print(f"Divisão: {f1} / {f2} = {f1.divisao(f2)}")
print()

# item B
print(f"A fração é {f1}")
print(f"A fração é {f2}")
print()

# item C:
f2.inverte()
print(f"A fração é {f2}")
f2.inverte()
print(f"A fração é {f2}")
print()

# item D:
print(f"O valor real de {f1} é {f1.valor_real()}")
print()

# item E:
n = 1.13
print(f"O valor {n} como fração é {Fracao.criar_fracao(n)}")