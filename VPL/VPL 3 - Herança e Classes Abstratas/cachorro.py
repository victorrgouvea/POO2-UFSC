from mamifero import Mamifero

class Cachorro(Mamifero):

    def __init__(self, tamanho_passo: int = 3, volume_som: int = 3):
        super().__init__(tamanho_passo, volume_som)

    def latir(self):
        return f"MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU"

    def produzirSom(self):
        pass