from abc import ABC

class Transporte(ABC):
    def __init__(self, nome: str, altura: float, comprimento: float,
                    carga: float, velocidade: float):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def carga(self):
        return self.__carga

    @property
    def velocidade(self):
        return self.__velocidade
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, 
                    velocidade: float, autonomia: float, envergadura: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    def __str__(self):
        return "Transporte Aéreo"

    @property
    def autonomia(self):
        return self.__autonomia
    
    @autonomia.setter
    def autonomia(self, autonomia):
        self.__autonomia = autonomia

    @property
    def envergadura(self):
        return self.__envergadura
    
    @envergadura.setter
    def envergadura(self, envergadura):
        self.__envergadura = envergadura

class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, 
                    velocidade: float, motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    def __str__(self):
        return "Transporte Terrestre"

    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    @property
    def rodas(self):
        return self.__rodas
    
    @rodas.setter
    def rodas(self, rodas):
        self.__rodas = rodas

class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, 
                    velocidade: float, boca: float, calado: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    def __str__(self):
        return "Transporte Aquático"

    @property
    def boca(self):
        return self.__boca
    
    @boca.setter
    def boca(self, boca):
        self.__boca = boca

    @property
    def calado(self):
        return self.__calado
    
    @calado.setter
    def calado(self, calado):
        self.__calado = calado

class Catalogo:

    def __init__(self, data):
        self.__data = data
        self.__veiculos = []

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    def insercao(self, veiculo):
        if isinstance(veiculo, Transporte):
            self.__veiculos.append(veiculo)

    def apresentacao(self):
        count = 1
        print(f"Veículos cadastrados no catálogo do dia {self.__data}:")
        for veiculo in self.__veiculos:
            print("-Veículo", count)
            print(f"Nome: {veiculo.nome}")
            print("Tipo:", veiculo)
            print(f"Altura: {veiculo.altura}m")
            print(f"Comprimento: {veiculo.comprimento}m")
            print(f"Carga: {veiculo.carga} toneladas")
            print(f"Velocidade: {veiculo.velocidade}km/h")

            if isinstance(veiculo, TransporteAereo):
                print(f"Autonomia: {veiculo.autonomia}km")
                print(f"Envergadura: {veiculo.envergadura}m")
            
            elif isinstance(veiculo, TransporteTerrestre):
                print(f"Motor: {veiculo.motor}")
                print(f"Rodas: {veiculo.rodas}")

            elif isinstance(veiculo, TransporteAquatico):
                print(f"Boca: {veiculo.boca}m")
                print(f"Calado: {veiculo.calado}m")

            print()
            count += 1

catalogo1 = Catalogo("26/11")

veiculo1 = TransporteAereo("Boeing 787", 17, 62.8, 253, 958, 11500, 60.1)
veiculo2 = TransporteTerrestre("Koenigsegg One:1", 1.2, 4.5, 0.2, 440, "5.0L V8", "Michelin")
veiculo3 = TransporteAquatico("Symphony of the Seas", 72.5, 362, 228000, 41, 47, 9.32)

catalogo1.insercao(veiculo1)
catalogo1.insercao(veiculo2)
catalogo1.insercao(veiculo3)

catalogo1.apresentacao()