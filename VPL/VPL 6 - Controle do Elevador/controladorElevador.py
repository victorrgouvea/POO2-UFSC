from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None
    
    def subir(self) -> str:
        self.__elevador.subir()
    
    def descer(self) -> str:
        self.__elevador.descer()

    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()
	
    def saiPessoa(self) -> str:
        self.__elevador.saiPessoa()
	
    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        if not (isinstance(andarAtual, int) and isinstance(totalAndaresPredio, int) 
            and isinstance(capacidade, int) and isinstance(totalPessoas, int)):
            raise ComandoInvalidoException
        elif (andarAtual < 0 or totalAndaresPredio < 0 or capacidade < 0 or totalPessoas < 0):
            raise ComandoInvalidoException
        elif andarAtual >= totalAndaresPredio:
            raise ComandoInvalidoException
        elif totalPessoas > capacidade:
            raise ComandoInvalidoException
        else:
            self.__elevador = Elevador(capacidade, totalPessoas, totalAndaresPredio, andarAtual)

controle = ControladorElevador()
controle.inicializarElevador(1, 4, 6, 2)