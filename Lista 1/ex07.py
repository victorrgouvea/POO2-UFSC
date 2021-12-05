'''Nesse sistema, o usuário tem que informar alguns dados para fazer o seu cadastro e conseguir acessar os livros.
   Quando o usuário abre um livro, ele é retirado da biblioteca, e não pode ser usado por nenhum outro usuário.
   Esse livro só ficará disponível quando esse usuário fecha-lo
   O sistema tambem consegue retornar todos os livros disponíveis na biblioteca, além das funções de
   passar as páginas na leitura'''

# Classe do exercício 2(biblioteca):
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

class Usuario:
    usuarios = []
    
    def __init__(self, nome: str, idade: int, celular: str, livro=""):
        self.__nome = nome
        self.__idade = idade
        self.__celular = celular
        self.__livro = livro
        Usuario.usuarios.append(self)

    def __str__(self):
        return self.__nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new: str):
        self.__nome = new

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, new: int):
        self.__idade = new

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, new: str):
        self.__celular = new

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, new: str):
        self.__livro = new

    def remover_usuario(self):
        Usuario.usuarios.remove(self)

    def add_usuario(self):
        Usuario.usuarios.append(self)

class SistemaLeitura:

    def livros_disponiveis():
        Livro.mostrar_biblioteca()
    
    def abrir_livro(usuario, livro):
        '''Abre o livro na tela'''
        if livro not in Livro.biblioteca:
            print("Esse livro não está disponível na biblioteca")
        if usuario not in Usuario.usuarios:
            print("Esse usuário não está cadastrado corretamente ou já está com um livro aberto")
        else:
            usuario.livro = livro
            usuario.remover_usuario()
            livro.remover_da_biblioteca()
            print(f'O usuário {usuario} abriu o livro "{livro}"')

    def fechar_livro(usuario, livro):
        '''Fecha o livro na tela'''
        if usuario.livro == "":
            print("Esse usuário não possue nenhum livro aberto")
        else:
            usuario.livro = ""
            usuario.add_usuario()
            livro.add_biblioteca()
            print(f'O usuário {usuario} fechou o livro "{livro}"')

    def proxima_pagina():
        '''Avança para a próxima página do livro'''
        print("Página virada")

    def voltar_pagina():
        '''Volta para a página anterior'''
        print("Página recuada")

    def avancar_pagina(pagina: int):
        '''Avança para a página informada'''
        print(f"Página {pagina} aberta")


livro1 = Livro("Cemitério dos Vivos", "Lima Barreto", 1920, "Companhia das Letras", 2, 1)
livro2 = Livro("A Revolução dos Bichos", "George Orwell", 1945, "Companhia das Letras", 1, 1)

# Criação de usuários:
usuario1 = Usuario("André Teixeira", 19, "991874653")
usuario2 = Usuario("Felipe Almeida", 34, "999807324")

# Busca pelos livros disponíveis:
SistemaLeitura.livros_disponiveis()

# Leitura do livro:
SistemaLeitura.abrir_livro(usuario1, livro2)
SistemaLeitura.proxima_pagina()
SistemaLeitura.voltar_pagina()
SistemaLeitura.avancar_pagina(14)
SistemaLeitura.fechar_livro(usuario1, livro2)