from abc import ABC, abstractmethod
from Pessoa.Pessoa import *

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
		pass

	def depositar(self, valor):
		pass

	def ver_saldo(self):
		pass


class ContaCorrente(Conta):
	def __init__(self, nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito, limite):
		super().__init__(nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito)
		self.limite = limite

	def sacar(self):
		pass

class ContaPoupanca(Conta):
	def __init__(self, nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito):
		super().__init__(nome, data_nasc, renda_mensal, tipo_conta, conta, agencia, saldo, credito)

	def sacar(self):
		pass