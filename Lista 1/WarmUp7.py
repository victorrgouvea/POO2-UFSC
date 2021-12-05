# Warm up lista 1 POO II

# item 7:
class Cidade:
    def __init__(self, nome: str, populacao: int):
        self.__nome = nome
        self.__populacao = populacao

    @property
    def nome(self):
        return self.__nome

    @property
    def populacao(self):
        return self.__populacao

    @populacao.setter
    def populacao(self, novo_pop: int):
        self.__populacao = novo_pop

class Estado:
    def __init__(self, nome: str, sigla: str, cidades: list):
        self.__nome = nome
        self.__sigla = sigla
        self.__cidades = cidades

    @property
    def nome(self):
        return self.__nome

    @property
    def sigla(self):
        return self.__sigla

    @property
    def cidades(self):
        return self.__cidades

    @cidades.setter
    def cidades(self, novo_cid: list):
        self.__cidades = novo_cid

    def populacao_total(self):
        total = 0
        for cidade in self.cidades:
            total += cidade.populacao
        return total

c1 = Cidade("São Paulo", 1000000)
c2 = Cidade("Campinas", 800000)
c3 = Cidade("Florianópolis", 500000)
c4 = Cidade("Joinvile", 450000)
c5 = Cidade("Curitiba", 650000)
c6 = Cidade("Maringá", 550000)

e1 = Estado("São Paulo", "SP", [c1, c2])
e2 = Estado("Santa Catarina", "SC", [c3, c4])
e3 = Estado("Paraná", "PR", [c5, c6])

print("A população total do estado de", e1.nome, "é", e1.populacao_total())
print("A população total do estado de", e2.nome, "é", e2.populacao_total())
print("A população total do estado de", e3.nome, "é", e3.populacao_total())