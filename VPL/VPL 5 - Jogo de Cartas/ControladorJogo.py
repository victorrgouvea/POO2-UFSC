from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia, habilidade, velocidade, resistencia, tipo)
        self.__personagems.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        for _ in range(5):
            c1 = self.__baralho.pop(0)
            c2 = self.__baralho.pop(0)
            jogador1.inclui_carta_na_mao(c1)
            jogador2.inclui_carta_na_mao(c2)

    def jogada(self, mesa: Mesa) -> Jogador:
        if mesa.carta_jogador1.valor_total_carta() > mesa.carta_jogador2.valor_total_carta():
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador1
        elif mesa.carta_jogador1.valor_total_carta() < mesa.carta_jogador2.valor_total_carta():
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador2
        else:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return None
            