from Banco.Conta import ContaCorrente, ContaPoupanca
import json
from random import randint
from modulo_data import validar_datanasc


class Banco:
    def __init__(self, agencias, agencia_atual):
        self.agencias = agencias
        self.__agencia_atual = agencia_atual
        print('-'*50)
        print(f'{"BEM VINDO AO BANCO - Ag " + str(self.agencia_atual):^50}')

    @property
    def agencia_atual(self):
        return self.__agencia_atual

    def atualizar_idade(self):
        pass

    def cadastrar_agencia(self, agencia_nome, agencia_numero):
        self.agencias[agencia_nome] = agencia_numero
        with open('agencias.json', mode='w') as arquivo:
            arquivo.write(json.dumps(self.agencias))

        print('Agência criada com sucesso.')

    def validar_cliente(self, conta_cliente, agencia_cliente):
        with open('contas_corrente.json', 'r') as arq:
            arquivo_cc = arq.read()
            arquivo_cc = json.loads(arquivo_cc)

        with open('contas_poupanca.json', 'r') as arq:
            arquivo_cp = arq.read()
            arquivo_cp = json.loads(arquivo_cp)

        if conta_cliente in arquivo_cc:
            if arquivo_cc[conta_cliente]['agencia'] == agencia_cliente:
                cc_cliente = True
            else:
                cc_cliente = False
        else:
            cc_cliente = False

        if conta_cliente in arquivo_cp:
            if arquivo_cp[conta_cliente]['agencia'] == agencia_cliente:
                cp_cliente = True
            else:
                cp_cliente = False
        else:
            cp_cliente = False

        return (cc_cliente, cp_cliente)

    def conectar_cliente(self, conta_cliente, tipo_conta):
        if tipo_conta == 'corrente':
            with open('contas_corrente.json', 'r') as arq:
                arquivo = arq.read()
                arquivo = json.loads(arquivo)

            cliente = arquivo[conta_cliente]

        if tipo_conta == 'poupanca':
            with open('contas_poupanca.json', 'r') as arq:
                arquivo = arq.read()
                arquivo = json.loads(arquivo)

            cliente = arquivo[conta_cliente]

        return cliente

    @staticmethod
    def credito_preaprovado(renda_mensal):
        if renda_mensal < 1500:
            credito = 0
            return (False, credito)

        else:
            credito = renda_mensal * 0.25
            return (True, credito)

    def atualizar_contas(self, dados_cliente, tipo_conta):
        if tipo_conta == 'corrente':
            try:
                with open('contas_corrente.json', 'r') as arq:
                    arquivo = arq.read()
                    arquivo = json.loads(arquivo)

                for k in dados_cliente:
                    conta = str(k)

                if conta in arquivo:
                    print('encontrado')
                    dados_cliente[conta] = dados_cliente.pop(int(conta))
                    arquivo[conta] = dados_cliente[conta]
                    print(arquivo)
                else:
                    print('Não encontrado')
                    arquivo.update(dados_cliente)

                with open('contas_corrente.json', 'w') as arq:
                    arq.write(json.dumps(arquivo))

            except json.decoder.JSONDecodeError:
                print('Json Decode Error')

                arquivo = dados_cliente

                with open('contas_corrente.json', 'w') as arq:
                    arq.write(json.dumps(arquivo))

            with open('contas_corrente.json', 'w') as arq:
                arq.write(json.dumps(arquivo))

        if tipo_conta == 'poupanca':
            try:
                with open('contas_poupanca.json', 'r') as arq:
                    arquivo = arq.read()
                    arquivo = json.loads(arquivo)

                for k in dados_cliente:
                    conta = str(k)

                if conta in arquivo:
                    print('encontrado')
                    dados_cliente[conta] = dados_cliente.pop(int(conta))
                    arquivo[conta] = dados_cliente[conta]
                    print(arquivo)
                else:
                    print('Não encontrado')
                    arquivo.update(dados_cliente)

                with open('contas_poupanca.json', 'w') as arq:
                    arq.write(json.dumps(arquivo))

            except json.decoder.JSONDecodeError:
                print('Json Decode Error')

                arquivo = dados_cliente

                with open('contas_poupanca.json', 'w') as arq:
                    arq.write(json.dumps(arquivo))

            with open('contas_poupanca.json', 'w') as arq:
                arq.write(json.dumps(arquivo))

    def abrir_conta(self):
        print('='*50)
        print('DADOS DO CLIENTE')
        nome = input('Nome do cliente: ').strip().title()

        while True:
            data_nasc = input('Data de Nascimento (DD/MM/AAAA): ').strip()

            if validar_datanasc(data_nasc):
                break
            else:
                print('Digite uma data de nascimento válida')
                continue

        while True:
            renda_mensal = input('Renda Mensal: ').strip()
            renda_mensal = renda_mensal.replace('R$', '')
            renda_mensal = renda_mensal.replace(',', '.')

            try:
                renda_mensal = int(renda_mensal)
                break
            except ValueError:
                print('Digite um valor válido')
                continue

        if self.credito_preaprovado(renda_mensal)[0]:
            print(
                f'O cliente tem um crédito pré-aprovado de R$ {self.credito_preaprovado(renda_mensal)[1]}')

            resposta_credito = input(
                'Gostaria de adquirir a função crédito? [S - SIM; N - NÃO] ').upper()

            if resposta_credito == 'S' or resposta_credito == 'SIM':
                credito = self.credito_preaprovado(renda_mensal)[1]
            else:
                credito = 0
        else:
            credito = 0

        while True:
            tipo_de_conta = input(
                'Tipo de conta [1-CC; 2-CP; 3-CC+CP]: ').strip()

            try:
                tipo_de_conta = int(tipo_de_conta)
            except ValueError:
                print('Digite um valor válido.')
                continue

            if tipo_de_conta in [1, 2, 3]:
                break
            else:
                print('Digite um valor válido')
                continue

        while True:
            conta = int(str(randint(0, 9)) + str(randint(0, 9)) +
                        str(randint(0, 9)) + str(randint(0, 9)) +
                        str(randint(0, 9)))

            try:
                with open('contas_corrente.json', 'r') as arq:
                    arquivo_cc = arq.read()
                    arquivo_cc = json.loads(arquivo_cc)
            except FileNotFoundError:
                print('Banco de dados de conta corrente não encontrado.')
                arq = open('contas_corrente.json', 'w')
                arq.close()
                print('Um novo banco de dados foi criado.')
                try:
                    with open('contas_corrente.json', 'r') as arq:
                        arquivo_cc = arq.read()
                        arquivo_cc = json.loads(arquivo_cc)
                except json.decoder.JSONDecodeError:
                    print('Json Decode Eror line 202')

            except json.decoder.JSONDecodeError:
                print('Json Decode Eror line 205')

            try:
                with open('contas_poupanca.json', 'r') as arq:
                    arquivo_pp = arq.read()
                    arquivo_pp = json.loads(arquivo_pp)
            except FileNotFoundError:
                print('Banco de dados de conta poupança não encontrado.')
                arq = open('contas_poupanca.json', 'w')
                arq.close()
                print('Um novo banco de dados foi criado.')
                try:
                    with open('contas_corrente.json', 'r') as arq:
                        arquivo_pp = arq.read()
                        arquivo_pp = json.loads(arquivo_pp)
                except json.decoder.JSONDecodeError:
                    print('Json Decode Eror line 221')

            except json.decoder.JSONDecodeError:
                print('Json Decode Eror line 223')

            if str(conta) not in arquivo_cc and str(conta) not in arquivo_pp:
                break
            else:
                continue

        agencia = self.agencia_atual

        limite = renda_mensal * 0.1

        if tipo_de_conta in [1, 2]:
            while True:
                saldo = input('Saldo inicial: ').strip()
                saldo.replace('R$', '')
                saldo.replace(',', '.')

                try:
                    saldo = int(saldo)
                    break
                except ValueError:
                    print('Digite um valor válido.')
                    continue

        if tipo_de_conta == 3:
            while True:
                saldo = input('Saldo inicial na conta corrente: ').strip()
                saldo.replace('R$', '')
                saldo.replace(',', '.')

                try:
                    saldo_corrente = int(saldo)
                    break
                except ValueError:
                    print('Digite um valor válido.')
                    continue

            while True:
                saldo = input('Saldo inicial na conta poupança: ').strip()
                saldo.replace('R$', '')
                saldo.replace(',', '.')

                try:
                    saldo_poupanca = int(saldo)
                    break
                except ValueError:
                    print('Digite um valor válido.')
                    continue

        if tipo_de_conta == 1:
            cliente = ContaCorrente(nome,
                                    data_nasc,
                                    renda_mensal,
                                    tipo_de_conta,
                                    conta,
                                    agencia,
                                    saldo,
                                    credito,
                                    limite)

            cliente_dados = cliente.retorna_cliente_dados()

            self.atualizar_contas(cliente_dados, 'corrente')

        if tipo_de_conta == 2:
            cliente = ContaPoupanca(nome,
                                    data_nasc,
                                    renda_mensal,
                                    tipo_de_conta,
                                    conta,
                                    agencia,
                                    saldo,
                                    credito)
            cliente_dados = cliente.retorna_cliente_dados()

            self.atualizar_contas(cliente_dados, 'poupanca')

        if tipo_de_conta == 3:

            cliente = ContaCorrente(nome,
                                    data_nasc,
                                    renda_mensal,
                                    tipo_de_conta,
                                    conta, agencia,
                                    saldo_corrente,
                                    credito,
                                    limite)
            cliente_dados = cliente.retorna_cliente_dados()

            self.atualizar_contas(cliente_dados, 'corrente')

            cliente2 = ContaPoupanca(nome,
                                     data_nasc,
                                     renda_mensal,
                                     tipo_de_conta,
                                     conta,
                                     agencia,
                                     saldo_poupanca,
                                     credito)

            cliente_dados2 = cliente2.retorna_cliente_dados()

            self.atualizar_contas(cliente_dados2, 'poupanca')
