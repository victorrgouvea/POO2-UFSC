'''Nessa aplicação, utilizo 3 classes: Turma, Aluno e Professor. 
   Nas classes Aluno e Professor, seus atributos indicam os dados cadastrais do aluno/professor.
   Já a classe Turma tem apenas o código da turma como atributo, e possui métodos para cadastrar um aluno
   ou professor na turma e exibir os dados dos alunos ou professores'''

class Turma:
    def __init__(self, codigo: str):
        self.__codigo = codigo
        self.__alunos = []
        self.__professores = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, new: str):
        self.__codigo = new

    def __str__(self):
        return f"Turma {self.__codigo}"

    def cadastrar_aluno(self, aluno):
        self.__alunos.append(aluno)
        print(f"Aluno {aluno.nome} cadastrado na turma {self.__codigo}.")

    def cadastrar_prof(self, prof):
        self.__professores.append(prof)
        print(f"Professor {prof.nome} cadastrado na turma {self.__codigo}.")

    def dados_alunos(self):
        print(f"Dados dos alunos da turma {self.__codigo}:")
        for aluno in self.__alunos:
            print()
            print(f"Nome: {aluno.nome}")
            print(f"Idade: {aluno.idade}")
            print(f"Curso: {aluno.curso}")
            print(f"Notas: {aluno.notas}")
            print(f"Presença: {aluno.presenca}%")

    def dados_profs(self):
        print(f"Dados dos professores da turma {self.__codigo}:")
        for prof in self.__professores:
            print()
            print(f"Nome: {prof.nome}")
            print(f"Idade: {prof.idade}")
            print(f"E-mail: {prof.email}")


class Aluno:
    def __init__(self, nome: str, idade: int, curso: str, notas: list, presenca: float):
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso
        self.__notas = notas
        self.__presenca = presenca

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
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, new: str):
        self.__curso = new

    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, new: list):
        self.__notas = new

    @property
    def presenca(self):
        return self.__presenca

    @presenca.setter
    def presenca(self, new: float):
        self.__presenca = new

class Professor:
    def __init__(self, nome: str, idade: int, email: str):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, new: str):
        self.__email = new

# Demonstração:
turma_calculo = Turma("1A")

joao = Aluno("João Souza", 20, "Engenharia Civil", [6.5, 7], 80)
gabriel = Aluno("Gabriel Antunes", 23, "Ciência da Computação", [8, 5.5], 75)
alberto = Professor("Alberto Nunes", 46, "alberto.nunes@gmail.com")

turma_calculo.cadastrar_aluno(joao)
turma_calculo.cadastrar_aluno(gabriel)
turma_calculo.cadastrar_prof(alberto)

turma_calculo.dados_alunos()
turma_calculo.dados_profs()