'''A classe "Livro" tem como atributos as informações do livro e possue uma lista que armazena 
   os livros que estão na biblioteca, sendo que quando um objeto livro é criado ele já é adicionado
   automaticamente na biblioteca.
   Os métodos dessa classe tem as funções de exibir uma lista com os livros da biblioteca e adicionar 
   e remover livros dessa mesma biblioteca.'''

class Livro:
    biblioteca = []
    
    def __init__(self, titulo: str, autores: str, ano: int, editora: str, edicao: int, volume: int):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume
        Livro.biblioteca.append(self)

    def __str__(self):
        return self.__titulo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autores(self):
        return self.__autores

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def edicao(self):
        return self.__edicao

    @property
    def volume(self):
        return self.__volume

    @classmethod
    def mostrar_biblioteca(cls):
        livros = cls.biblioteca
        print("Livros da biblioteca:")
        for livro in livros:
            print(f"-{livro.titulo}, {livro.autores}/{livro.ano}")

    def remover_da_biblioteca(self):
        Livro.biblioteca.remove(self)
        print(f"{self.__titulo} removido da biblioteca")

    def add_biblioteca(self):
        Livro.biblioteca.append(self)
        print(f"{self.__titulo} adicionado a biblioteca")


livro1 = Livro("Cemitério dos Vivos", "Lima Barreto", 1920, "Companhia das Letras", 2, 1)
livro2 = Livro("A Revolução dos bichos", "George Orwell", 1945, "Companhia das Letras", 1, 1)

Livro.mostrar_biblioteca()
print()
livro1.remover_da_biblioteca()
Livro.mostrar_biblioteca()
print()
livro1.add_biblioteca()
Livro.mostrar_biblioteca()