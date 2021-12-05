from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartas_jogador = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        carta = self.__cartas_jogador.pop(random.randrange(0, len(self.__cartas_jogador)))
        return carta

    @property
    def mao(self) -> list:
        return self.__cartas_jogador

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.__cartas_jogador.append(carta)