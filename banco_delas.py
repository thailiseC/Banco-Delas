import random
import string


class Cliente:
    def __init__(self, nome, telefone, renda_mensal: float):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
        self._cheque_especial = renda_mensal
        self._mulher = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, valor: float):
        self._renda_mensal = valor

    @property
    def mulher(self):
        return self._mulher

    @property
    def cheque_especial(self):
        return self._cheque_especial

    @cheque_especial.setter
    def cheque_especial(self):
        self._cheque_especial = self.renda_mensal

    def __str__(self):
        return (
            f'Cliente: {self.nome}, ' +
            f'telefone: {self.telefone}, ' +
            f'renda mensal: {self.renda_mensal}, ' +
            f'cheque especial: {self.cheque_especial}, ' +
            f'se considera mulher? {self.mulher} '
        )


class Mulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal: float):
        super().__init__(nome, telefone, renda_mensal)
        self._mulher = True

    @property
    def mulher(self):
        return self._mulher


class Not_mulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self._cheque_especial = 0.0

    @property
    def cheque_especial(self):
        return self._cheque_especial


class Conta_corrente:
    def __init__(self, numero_da_conta: str):
        self._titular = []
        self._numero_da_conta = numero_da_conta
        self._saldo = 0.0
        self._cheque_especial_total = 0.0
        self.status = False

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular.append(valor)

    @property
    def numero_da_conta(self):
        return self._numero_da_conta

    @numero_da_conta.setter
    def numero_da_conta(self, valor):
        self._numero_da_conta = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        self._saldo = valor

    def cheque_especial_total(self):
        for i in range(0, len(self._titular)):
            self._cheque_especial_total += float(self.titular[i].cheque_especial)
        return self._cheque_especial_total

    def depositar(self, valor):
        if self.status:
            self._saldo += valor
        else:
            print('Operação não realizada. Conta inativa.')

    def sacar(self, valor):
        if self.status:
            if (self.saldo - valor) >= 0.0:
                self.saldo -= valor
            elif abs(self.saldo - valor) <= self._cheque_especial_total:
                self.saldo -= self.cheque_especial_total - valor
            else:
                print('Operação não realizada. Saldo insuficiente.')
        else:
            print('Operação não realizada. Conta inativa.')

    def apresenta_titulares(self):
        nomes = ''
        for i in range(0, len(self.titular)):
            nomes = nomes + f'{i + 1}: {self.titular[i].nome}, '
        return nomes

    def __str__(self):
        return (
            f'Conta {self.numero_da_conta}, ' + 
            f'Titular(es): {self.apresenta_titulares()}, ' + 
            f'Saldo: {self.saldo}, ' + 
            f'Cheque especial disponível: {self.cheque_especial_total()}, ' + 
            f'Ativa: {self.status}'
        )


class Banco_Delas:
    def __init__(self):
        self.contas_abertas = []

    def menu(self):
        print('Sistema Banco Delas. Qual operação que deseja realizar? \n')
        print(*self.contas_abertas)
        print('1 - Abrir conta')
        print('2 - Consultar dados de uma conta')
        print('3 - Fazer um saque')
        print('4 - Fazer um depósito')
        print('5 - Alterar dados de uma conta')
        print('6 - Desativar uma conta')
        print('7 - Sair')
        opcao_menu = input('Opção número: ')

        if opcao_menu == '1':
            self.abrir_conta()
        elif opcao_menu == '2':
            numero = input('Digite o número da conta: ')
            if self.buscar_conta(numero) != False:
                print(self.buscar_conta(numero))
            else:
                print('Conta não encontrada.')
            self.menu()
        elif opcao_menu == '3':
            numero = input('Digite o número da conta: ')
            if self.buscar_conta(numero) != False:
                print(self.buscar_conta(numero))
                valor = float(input('Digite o valor a ser sacado: '))
                self.buscar_conta(numero).sacar(valor)
                print(f'Saldo atual: {self.buscar_conta(numero).saldo}')
            else:
                self.buscar_conta(numero)
            self.menu()
        elif opcao_menu == '4':
            numero = input('Digite o número da conta: ')
            if self.buscar_conta(numero) != False:
                print(self.buscar_conta(numero))
                valor = float(input('Digite o valor a ser depositado: '))
                self.buscar_conta(numero).depositar(valor)
                print(f'Saldo atual: {self.buscar_conta(numero).saldo}')
            else:
                self.buscar_conta(numero)
            self.menu()
        elif opcao_menu == '5':
            self.alterar_dados()
        elif opcao_menu == '6':
            self.fechar_conta()
        elif opcao_menu =='7':
            print('Finalizando...')
            exit
        else:
            print('Opção Inválida.')
            self.menu()

    def buscar_conta(self, numero: str):
        for i in range(0, len(self.contas_abertas)):
            if self.contas_abertas[i].numero_da_conta == numero:
                return self.contas_abertas[i]
            else:
                print('Conta não encontrada')
                return False

    def abrir_conta(self):
        numero = f'{self.random_generator(6)}-{self.random_generator(1)}'
        conta = Conta_corrente(numero)
        conta.status = True
        print(f'Criação da conta número {conta.numero_da_conta} em andamento.')
        self.adicionar_titular(conta)
        self.contas_abertas.append(conta)
        print(conta)
        self.menu()

    def adicionar_titular(self, conta: Conta_corrente):
        opcao_cadastrar = '1'
        while opcao_cadastrar != '2':
            nome = input("Nome completo da titular: ")
            telefone = input("Telefone da titular: ")
            renda = input("Renda mensal da titular: ")
            opcao_mulher = input(f'{nome} se autodeclara mulher? (1 - Sim | 2 - Não): ')
            if opcao_mulher == '1':
                conta.titular = Mulher(nome, telefone, renda)
            elif opcao_mulher == '2':
                conta.titular = Not_mulher(nome, telefone, renda)
            else:
                conta.titular = Not_mulher(nome, telefone, renda)

            opcao_cadastrar = input(
                'Deseja cadastrar mais titulares para essa conta?'
                '(1 - Sim | 2 - Não): ')

    def fechar_conta(self):
        numero = input('Número da conta a ser desativada: ')
        if self.buscar_conta(numero).saldo != 0.0:
            print(
                    'Operação não realizada. ' +
                    'Conta com saldo ou utilizando limite do cheque especial.'
            )
        else:
            if self.buscar_conta(numero):
                if self.buscar_conta(numero).status:
                    self.buscar_conta(numero).status = False
                else:
                    print('Operação não realizada. Conta já está inativa.')
            else:
                self.buscar_conta(numero)
        self.menu()

    def alterar_dados(self):
        numero = input('Número da conta a ser alterada: ')
        if self.buscar_conta(numero) != False:
            escolha = int(
                input(
                    f'O que deseja realizar na conta {numero}? \n'
                    '1 - Adicionar titular \n'
                    '2 - Remover titular \n'
                    '3 - Alterar dados de titular \n'
                    '4 - Voltar'
                )
            )

            def opcao1():
                self.adicionar_titular(self.buscar_conta(numero))

            def opcao2():
                if len(self.buscar_conta(numero).titular) == 1:
                    print(
                        'A conta possui somente um titular. ' +
                        'Não é possível remover mais titulares.'
                    )
                else:
                    print(f'Qual titular deseja remover?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_remove = int(input('Titular número: '))
                    del self.buscar_conta(numero).titular[escolha_remove - 1]

            def opcao3():
                escolha_alterar = int(
                    input(
                        'O que deseja alterar? \n' +
                        '1 - Nome de um titular \n' +
                        '2 - Telefone de um titular \n' +
                        '3 - Renda mensal de um titular \n' +
                        '4 - Autodeclaração de gênero \n' +
                        '5 - Voltar'
                    )
                )

                def opcao3_1():
                    print(f'De qual titular deseja alterar o nome?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_nome = int(input('Titular número: '))
                    nome_antigo = self.buscar_conta(numero).titular[escolha_nome - 1].nome
                    nome = input('Escreva o novo nome: ')
                    confirmacao = input(
                        f'Confirma a alteração do nome {nome_antigo} para {nome}? \n' +
                        '1 - Sim | 2 - Não'
                    )
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_nome - 1].nome = nome
                    else:
                        print('Operação abortada. voltando ao menu principal...')
                        opcoes.get(4)()

                def opcao3_2():
                    print(f'De qual titular deseja alterar o telefone?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_telefone = int(input('Titular número: '))
                    telefone_antigo = self.buscar_conta(numero).titular[escolha_telefone - 1].telefone
                    telefone = input(
                        f'Escreva o novo número de telefone do titular' +
                        f'{self.buscar_conta(numero).titular[escolha_telefone - 1].nome}:'
                    )
                    confirmacao = input(
                        f'Confirma a alteração do telefone {telefone_antigo} para {telefone}?\n' +
                        '1 - Sim | 2 - Não'
                    )
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_telefone - 1].telefone = telefone
                    else:
                        print('Operação abortada. voltando ao menu principal...')
                        opcoes.get(4)()

                def opcao3_3():
                    print(f'De qual titular deseja alterar a renda mensal?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_renda = int(input('Titular número: '))
                    titular = self.buscar_conta(numero).titular[escolha_renda - 1].nome
                    renda_antiga = self.buscar_conta(numero).titular[escolha_renda - 1].renda_mensal
                    renda = float(
                        input(
                            f'Escreva a nova renda mensal do titular {titular}: '
                        )
                    )
                    confirmacao = input(
                        f'Confirma a alteração da renda mensal do titular {titular}' +
                        f'de {renda_antiga} para {renda}? \n' +
                        '1 - Sim | 2 - Não'
                    )
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_renda - 1].renda_mensal = renda
                    else:
                        print('Operação abortada. voltando ao menu principal...')
                        opcoes.get(4)()

                def opcao3_4():
                    opcoes.get(4)()

                opcoes_alteracao = {1: opcao3_1, 2: opcao3_2, 3: opcao3_3, 4: opcao3_4}
                opcoes_alteracao.get(escolha_alterar)()

            def opcao4():
                self.menu()

            opcoes = {1: opcao1, 2: opcao2, 3: opcao3, 4: opcao4}
            opcoes.get(escolha)()
        else:
            self.buscar_conta(numero)
        self.menu()

    def random_generator(self, size):
        chars = string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def __str__(self):
        return f'Contas abertas: {self.contas_abertas}'


banco = Banco_Delas()
# banco.menu()
