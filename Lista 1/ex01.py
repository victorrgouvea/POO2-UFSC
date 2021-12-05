'''Nesse sistema, são criadas contas de banco, as quais são associadas titulares(lista de clientes)
   Temos 3 tipos de conta: a conta corrente normal, a especial e a poupança. Nos 3 tipos de conta temos
   as mesmas funções, como saque, depósito, mostrar o extrato, adicionar e remover titulares e mostrar
   a lista de titulares.
   O diferencial da conta especial é que ela tem um limite de saldo acima do normal, o qual o cliente
   pode usar para sacar uma quantia mesmo sem ter dinheiro suficiente no saldo naquele momento.
   Já a conta poupança tem um rendimento mensal, que é aplicado no total disponível no saldo.'''

import datetime

class Cliente:
    def __init__(self, nome: str, fone: str):
        self.__nome = nome
        self.__fone = fone

    def __str__(self):
        return self.__nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new: str):
        self.__nome = new

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, new: int):
        self.__fone = new

class ContaCorrente:
    def __init__(self, saldo: float, titulares=[]):
        self.__saldo = saldo
        self.__titulares = titulares
        self.__operacoes = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, new: str):
        self.__saldo = new

    @property
    def titulares(self):
        return self.__titulares

    @titulares.setter
    def titulares(self, new: int):
        self.__titulares = new

    @property
    def operacoes(self):
        return self.__operacoes

    @operacoes.setter
    def operacoes(self, new: str):
        self.__operacoes = new

    def saque(self, quantia: float):
        if quantia < 0:
            print("Valor em formato errado")
        elif quantia <= self.__saldo:
            self.__saldo -= quantia
            self.__operacoes.append(f"-Saque de R${quantia} - {datetime.datetime.today().strftime('%d/%m/%Y %H:%M')}")
            print(f"Saque de R${quantia} realizado")
        else:
            print("Você não tem dinheiro suficiente para realizar essa saque")

    def deposito(self, quantia: float):
        if quantia < 0:
            print("Valor em formato errado")
        else:
            self.__saldo += quantia
            self.__operacoes.append(f"-Depósito de R${quantia} - {datetime.datetime.today().strftime('%d/%m/%Y %H:%M')}")
            print(f"Depósito de R${quantia} realizado")

    def extrato(self):
        print("Extrato da conta:")
        for op in self.__operacoes:
            print(op)
        print()
        print(f"Saldo atual: {self.__saldo}")

    def add_titular(self, titular: Cliente):
        if titular not in self.__titulares:
            self.__titulares.append(titular)
            print(f"O Cliente {titular} agora é titular dessa conta")
        else:
            print("Esse cliente já é titular dessa conta")

    def remover_titular(self, titular: Cliente):
        if titular in self.__titulares:
            self.__titulares.remove(titular)
            print(f"O Cliente {titular} não é mais titular dessa conta")
        else:
            print("Esse cliente não é titular dessa conta")

    def mostrar_titulares(self):
        print("Titulares da conta:")
        for titular in self.__titulares:
            print("-", titular)

class ContaEspecial(ContaCorrente):
    def __init__(self, saldo: float, titulares=[], limite=300):
        super().__init__(saldo, titulares=titulares)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, new: str):
        self.__limite = new

    def saque(self, quantia):
        if quantia < 0:
            print("Valor em formato errado")
        elif quantia <= self.saldo + self.__limite:
            self.saldo -= quantia
            self.operacoes.append(f"-Saque de R${quantia} - {datetime.datetime.today().strftime('%d/%m/%Y %H:%M')}")
            print(f"Saque de R${quantia} realizado")
        else:
            print("Você não tem dinheiro suficiente para realizar essa saque")

class ContaPoupanca(ContaCorrente):
    def __init__(self, saldo: float, titulares=[], rendimento=1.02):
        super().__init__(saldo, titulares=titulares)
        self.__rendimento = rendimento

    @property
    def rendimento(self):
        return self.__rendimento

    @rendimento.setter
    def rendimento(self, new: str):
        self.__rendimento = new

    def aplicar_rendimento(self):
        '''Aplica o rendimento no final de cada mês'''
        self.saldo = self.saldo * self.__rendimento
        print("Rendimento mensal aplicado")


# Exemplos:
cliente1 = Cliente("Amanda Ferreira", "991212343")
cliente2 = Cliente("Alberto Nunes", "999928712")

conta1 = ContaCorrente(1000, [cliente1])
conta1.saque(300)
print(conta1.saldo)
conta1.deposito(500)
conta1.extrato()
conta1.add_titular(cliente2)
conta1.mostrar_titulares()
conta1.add_titular(cliente2)
print()

conta2 = ContaEspecial(500, [cliente2])
conta2.saque(800)
print(conta2.saldo)
conta2.deposito(1000)
conta2.extrato()
conta2.mostrar_titulares()
print()

conta3 = ContaPoupanca(1000, [cliente1])
conta3.aplicar_rendimento()
print(conta3.saldo)
conta3.deposito(500)
conta3.extrato()