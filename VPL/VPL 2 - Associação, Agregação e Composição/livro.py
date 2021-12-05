from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora):
        self.__editora = editora


    def incluirAutor(self, autor: Autor):
        if autor not in self.__autores and isinstance(autor, Autor):
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if autor in self.__autores and isinstance(autor, Autor):
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        incluir = True
        for cap in self.__capitulos:
            if cap.titulo == tituloCapitulo:
                incluir = False
                break
        if incluir:
            self.__capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))

    def excluirCapitulo(self, tituloCapitulo: str):
        excluir = False
        capitulo = None
        for cap in self.__capitulos:
            if cap.titulo == tituloCapitulo:
                excluir = True
                capitulo = cap
                break
        if excluir:
            self.__capitulos.remove(capitulo)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        capitulo = None
        for cap in self.__capitulos:
            if cap.titulo == tituloCapitulo:
                capitulo = cap
                break
        if capitulo != None:
            return capitulo