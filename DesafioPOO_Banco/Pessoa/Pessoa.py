from abc import ABC, abstractmethod
from modulo_data import *


class Pessoa:
	def __init__(self, nome, data_nasc):
		self.__nome = nome
		self.__datanasc = data_nasc
		self.idade = calcular_idade(self.datanasc)

	@property
	def nome(self):
		return self.__nome

	@property
	def datanasc(self):
		return self.__datanasc


	
class Cliente(Pessoa):
	def __init__(self, nome, data_nasc, renda_mensal, tipo_conta):
		"""
		: tipo_conta -> 1 = Conta Corrente, 2 = Conta Poupança, 3 = Ambas
		"""
		super().__init__(nome, data_nasc)
		self.renda_mensal = renda_mensal
		self.tipo_conta = tipo_conta
		self.processamento_tipo_conta()


	def processamento_tipo_conta(self):
		if self.tipo_conta == 1:
			self.conta_corrente = True
			self.conta_poupanca = False

		elif self.tipo_conta == 2:
			self.conta_corrente = False
			self.conta_poupanca = True

		elif self.tipo_conta == 3:
			self.conta_corrente = True
			self.conta_poupanca = True





