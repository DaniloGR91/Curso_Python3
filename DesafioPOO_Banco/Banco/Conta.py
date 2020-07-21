from abc import ABC, abstractmethod
from Pessoa.Pessoa import Cliente


class Conta(ABC, Cliente):
    def __init__(self,
                 nome,
                 data_nasc,
                 renda_mensal,
                 tipo_conta,
                 conta,
                 agencia,
                 saldo,
                 credito):

        super().__init__(nome, data_nasc, renda_mensal, tipo_conta)
        self.conta = conta
        self.agencia = agencia
        self.__saldo = saldo
        self.credito = credito

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @abstractmethod
    def sacar(self):
        pass

    def depositar(self, valor):
        pass

    def ver_saldo(self):
        print(f'O seu saldo é {self.saldo}')


class ContaCorrente(Conta):
    def __init__(self,
                 nome,
                 data_nasc,
                 renda_mensal,
                 tipo_conta,
                 conta,
                 agencia,
                 saldo,
                 credito,
                 limite):

        super().__init__(nome, data_nasc, renda_mensal,
                         tipo_conta, conta, agencia, saldo, credito)
        self.limite = limite

    def sacar(self):
        print('método sacar conta corrente')
        while True:
            valor = input('Quanto você deseja sacar? ').strip()
            valor = valor.replace('R$', '')
            valor = valor.replace(',', '.')
            try:
                valor = int(valor)
                break
            except ValueError:
                print('Digite um valor válido.')
                continue

        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            print(f'Seu novo saldo é de {self.saldo}')

    def retorna_cliente_dados(self):
        cliente_dados = {self.conta: {
            'nome': self.nome,
            'datanasc': self.datanasc,
            'renda_mensal': self.renda_mensal,
            'saldo': self.saldo,
            'credito': self.credito,
            'limite': self.limite,
            'agencia': self.agencia
        }}

        return cliente_dados


class ContaPoupanca(Conta):
    def __init__(self,
                 nome,
                 data_nasc,
                 renda_mensal,
                 tipo_conta,
                 conta,
                 agencia,
                 saldo,
                 credito):

        super().__init__(nome, data_nasc, renda_mensal,
                         tipo_conta, conta, agencia, saldo, credito)

    def sacar(self):
        print('método sacar poupanca')
        while True:
            valor = input('Quanto você deseja sacar? ').strip()
            valor = valor.replace('R$', '')
            valor = valor.replace(',', '.')
            try:
                valor = int(valor)
                break
            except ValueError:
                print('Digite um valor válido.')
                continue

        # Ajeitr self.saldo pra ficar inteiro
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Seu novo saldo é de {self.saldo}')

    def retorna_cliente_dados(self):
        cliente_dados = {self.conta: {
            'nome': self.nome,
            'datanasc': self.datanasc,
            'renda_mensal': self.renda_mensal,
            'saldo': self.saldo,
            'credito': self.credito,
            'agencia': self.agencia
        }}

        return cliente_dados
