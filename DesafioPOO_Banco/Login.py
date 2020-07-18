import json

class SistemaLogin:
	def __init__(self):
		self.agencias = {}
		self.carregar_agencias()


	def carregar_agencias(self):
		try:
			with open('agencias.json', mode='r') as arq:
				arquivo = arq.read()
				database = json.loads(arquivo)
				self.agencias = database
		except FileNotFoundError:
			raise FileNotFoundError('Banco de dados de agências não encontrado.')


	def validar_agencia(self):
		try:
			self.agencia_atual = int(self.agencia_atual)
		except ValueError:
			print('Digite uma agência válida')
			return False
		
		if self.agencia_atual in self.agencias.values():
			return True
		else:
			print('Agência não cadastrada')
			return False