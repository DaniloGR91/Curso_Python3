from Banco.Banco import Banco
import sys


class Menu(Banco):
    def __init__(self, agencias, agencia_atual):
        self.agencias = agencias
        self.__agencia_atual = agencia_atual

        while True:
            self.menu_principal()
            if self.validar_opcao():
                self.escolher_opcao()

                if self.opcao == 1 or self.opcao == 3:
                    break

    @property
    def agencia_atual(self):
        return self.__agencia_atual

    def menu_principal(self):
        print('-'*50)
        print('1 - Abrir Conta')
        print('2 - Cadastrar Agência')
        print('3 - Abrir menu do cliente')
        print('4 - Trocar agência')
        print('5 - Sair do sistema')
        print('-'*50)
        self.opcao = input('Digite a opção desejada: ')

    def validar_opcao(self, max=5):
        try:
            self.opcao = int(self.opcao)
        except ValueError:
            print('Digite uma opção válida')
            return False

        if self.opcao in range(1, max+1):
            return True
        else:
            print('Digite uma opção válida')
            return False

    def escolher_opcao(self):
        if self.opcao == 1:
            return self.opcao

        if self.opcao == 2:
            if self.agencia_atual == 1111:

                while True:
                    agencia_nome = input('Digite o nome da agência: ').strip()
                    agencia_numero = input('Digite a agência: ').strip()
                    if self.validar_nova_agencia(agencia_nome, agencia_numero):
                        super().cadastrar_agencia(agencia_nome=agencia_nome,
                                                  agencia_numero=int(agencia_numero))
                        break
            else:
                print(
                    'Apenas a agência 1111 tem autorização para cadastrar uma nova agência')

        if self.opcao == 3:
            return self.opcao

        if self.opcao == 4:
            from main import init
            init()

        if self.opcao == 5:
            print('Obrigado por usar o nosso sistema')
            sys.exit()
            return

    def validar_nova_agencia(self, agencia_nome, agencia_numero):
        try:
            int(agencia_numero)
        except ValueError:
            print('Digite um número de agência válida')
            return False

        if agencia_nome in self.agencias.keys():
            print('A nome de agência que você usou já foi cadastrado')
            return False

        elif int(agencia_numero) in self.agencias.values():
            print('O número de agência que você usou já foi cadastrado')
            return False

        else:
            return True


class MenuCliente(Menu):
    def __init__(self, cc=True, cp=False):
        while True:
            self.menu_principal()
            if self.validar_opcao(max=4):
                break
            else:
                continue

    def menu_principal(self):
        print('-'*50)
        print('1 - Ver Saldo')
        print('2 - Depositar')
        print('3 - Sacar')
        print('4 - Sair do sistema')
        print('-'*50)
        self.opcao = input('Digite a opção desejada: ')
