from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade, totalPessoas, totalAndaresPredio, andarAtual):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        self.__totalAndaresPredio = totalAndaresPredio
        self.__andarAtual = andarAtual


    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
            return "O elevador desceu um andar"
        else:
            raise ElevadorJahNoTerreoException
    
    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self.__totalPessoas < self.__capacidade:
            self.__totalPessoas += 1
            return "Uma pessoa entrou no elevador"
        else:
            raise ElevadorCheioException
    
    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self.__totalPessoas > 0:
            self.__totalPessoas -= 1
            return "Uma pessoa saiu do elevador"
        else:
            raise ElevadorJahVazioException
    
    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self.__andarAtual == self.__totalAndaresPredio-1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
            return "O elevador subiu um andar"
    
    @property
    def capacidade(self) -> int:
        return self.__capacidade
    
    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas
    
    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio
    
    @property
    def andarAtual(self) -> int:
        return self.__andarAtual
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @totalPessoas.setter
    def totalPessoas(self, totalPessoas: int):
        self.__totalPessoas = totalPessoas

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio

    @andarAtual.setter
    def andarAtual(self, andarAtual: int):
        self.__andarAtual = andarAtual