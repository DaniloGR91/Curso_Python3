from Login import SistemaLogin
from Banco.Banco import Banco
from Banco.Menu import Menu, MenuCliente
from Banco.Conta import ContaCorrente, ContaPoupanca
import sys


def init():

    login = SistemaLogin()
    while True:
        login.agencia_atual = input('Digite o número da sua agência: ').strip()
        validacao_agencia = login.validar_agencia()
        if validacao_agencia:
            global banco
            banco = Banco(login.agencias, login.agencia_atual)
            menu()

        else:
            continue


def menu():
    while True:
        menu = Menu(banco.agencias, banco.agencia_atual)
        if menu.opcao == 1:
            banco.abrir_conta()

        if menu.opcao == 3:
            while True:
                agencia_cliente = input('Digite sua agência: ').strip()
                try:
                    agencia_cliente = int(agencia_cliente)
                except ValueError:
                    print('Digite uma agência válida')
                    continue

                if agencia_cliente in banco.agencias.values():
                    break
                else:
                    print('A agência que você digitou não é válida')
                    continue

            while True:
                numero_conta_cliente = input('Digite a sua conta: ').strip()
                try:
                    numero_conta_cliente = int(numero_conta_cliente)
                    break
                except ValueError:
                    print('Digite uma conta válida.')

            validar_cliente = banco.validar_cliente(
                str(numero_conta_cliente), agencia_cliente)

            global conta_cliente
            if validar_cliente[0] and not validar_cliente[1]:
                cliente = banco.conectar_cliente(
                    str(numero_conta_cliente), 'corrente')

                conta_cliente = ContaCorrente(nome=cliente['nome'],
                                              data_nasc=cliente['datanasc'],
                                              renda_mensal=cliente['renda_mensal'],
                                              tipo_conta=1,
                                              conta=int(numero_conta_cliente),
                                              agencia=cliente['agencia'],
                                              saldo=cliente['saldo'],
                                              credito=cliente['credito'],
                                              limite=cliente['limite'])

                menu_cliente(cc=True, cp=False)

            elif not validar_cliente[0] and validar_cliente[1]:
                cliente = banco.conectar_cliente(
                    str(numero_conta_cliente), 'poupanca')

                conta_cliente = ContaPoupanca(nome=cliente['nome'],
                                              data_nasc=cliente['datanasc'],
                                              renda_mensal=cliente['renda_mensal'],
                                              tipo_conta=1,
                                              conta=int(numero_conta_cliente),
                                              agencia=cliente['agencia'],
                                              saldo=cliente['saldo'],
                                              credito=cliente['credito'])

                menu_cliente(cc=False, cp=True)

            elif validar_cliente[0] and validar_cliente[1]:
                while True:
                    conta_escolhida = input(
                        'Você deseja acessar qual conta? [1 - Conta Corrente; 2 - Conta Poupança] ').strip()
                    if conta_escolhida == '1' or conta_escolhida == '2':
                        conta_escolhida = int(conta_escolhida)
                        break
                    else:
                        print('Escolha uma opção válida')
                        continue

                if conta_escolhida == 1:
                    cliente = banco.conectar_cliente(
                        str(numero_conta_cliente), 'corrente')

                    conta_cliente = ContaCorrente(nome=cliente['nome'],
                                                  data_nasc=cliente['datanasc'],
                                                  renda_mensal=cliente['renda_mensal'],
                                                  tipo_conta=1,
                                                  conta=int(
                                                      numero_conta_cliente),
                                                  agencia=cliente['agencia'],
                                                  saldo=cliente['saldo'],
                                                  credito=cliente['credito'],
                                                  limite=cliente['limite'])
                    menu_cliente(cc=True, cp=False)

                if conta_escolhida == 2:
                    cliente = banco.conectar_cliente(
                        str(numero_conta_cliente), 'poupanca')

                    conta_cliente = ContaPoupanca(nome=cliente['nome'],
                                                  data_nasc=cliente['datanasc'],
                                                  renda_mensal=cliente['renda_mensal'],
                                                  tipo_conta=1,
                                                  conta=int(
                                                      numero_conta_cliente),
                                                  agencia=cliente['agencia'],
                                                  saldo=cliente['saldo'],
                                                  credito=cliente['credito'])
                    menu_cliente(cc=False, cp=True)
            else:
                print('ERRO')


def menu_cliente(cc=True, cp=False):
    while True:
        print(conta_cliente.nome, conta_cliente.idade, conta_cliente.saldo)
        menu = MenuCliente(cc, cp)
        print(f'opcao foi {menu.opcao}')
        if menu.opcao == 1:
            conta_cliente.ver_saldo()
        elif menu.opcao == 2:
            conta_cliente.depositar()
            cliente_dados = conta_cliente.retorna_cliente_dados()

            if cc:
                banco.atualizar_contas(cliente_dados, 'corrente')

            if cp:
                banco.atualizar_contas(cliente_dados, 'poupanca')

        elif menu.opcao == 3:
            conta_cliente.sacar()
            cliente_dados = conta_cliente.retorna_cliente_dados()
            if cc:
                banco.atualizar_contas(cliente_dados, 'corrente')

            if cp:
                banco.atualizar_contas(cliente_dados, 'poupanca')

        elif menu.opcao == 4:
            pass
        elif menu.opcao == 5:
            print('Obrigado e volte sempre.')
            sys.exit()


if __name__ == '__main__':
    init()
