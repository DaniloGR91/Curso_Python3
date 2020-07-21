from abc import ABC, abstractmethod
from Pessoa.Pessoa import Cliente


class Conta(ABC, Cliente):
    def __init__(self, nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito):
        super().__init__(nome, data_nasc, renda_mensal, tipo_conta)
        self.conta = conta
        self.agencia = agencia
        self.__saldo = saldo
        self.credito = credito

    @property
    def saldo(self):
        return self.__saldo

    @abstractmethod
    def sacar(self):
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

    def depositar(self, valor):
        pass

    def ver_saldo(self):
        print(f'O seu saldo é {self.saldo}')


class ContaCorrente(Conta):
    def __init__(self, nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito, limite):
        super().__init__(nome, data_nasc, renda_mensal,
                         tipo_conta, conta, agencia, saldo, credito)
        self.limite = limite

    def sacar(self):
        pass


class ContaPoupanca(Conta):
    def __init__(self, nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito):
        super().__init__(nome, data_nasc, renda_mensal,
                         tipo_conta, conta, agencia, saldo, credito)

    def sacar(self):
        pass
