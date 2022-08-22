import random
import string


class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
        self._cheque_especial = 0.0
        self.mulher = False

    @property
    def nome(self):
        return self._nome.title()

    @property
    def cheque_especial(self):
        if self.mulher:
            return self.renda_mensal
        else:
            return 0.0

    def __str__(self):
        return (
            f'Cliente: {self._nome}, ' +
            f'telefone: {self.telefone}, ' +
            f'renda mensal: {self.renda_mensal}, ' +
            f'cheque especial: {self.cheque_especial}, ' +
            f'se considera mulher? {self.mulher} '
        )


class Mulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal: float):
        super().__init__(nome, telefone, renda_mensal)
        self.mulher = True

    def __str__(self):
        return (
            f'Cliente: {self._nome}, '
            f'telefone: {self.telefone}, '
            f'renda mensal: {self.renda_mensal}, '
            f'cheque especial: {self.cheque_especial}, '
            f'se considera mulher? {self.mulher}.'
        )


class Not_mulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.mulher = False

    def __str__(self):
        return (
            f'Cliente: {self._nome}, ' +
            f'telefone: {self.telefone}, ' +
            f'renda mensal: {self.renda_mensal}, ' +
            f'cheque especial: {self.cheque_especial}, ' +
            f'se considera mulher? {self.mulher} '
        )


class Conta_corrente:
    def __init__(self, numero_da_conta: str):
        self._titular = []
        self.numero_da_conta = numero_da_conta
        self.saldo = 0.0
        self.status = False
        self.cheque_especial_total = 0.0
        self.cheque_especial_inicial = 0.0

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor: Cliente):
        self._titular.append(valor)
        self.atualiza_cheque_especial()

    def atualiza_cheque_especial(self):
        self.cheque_especial_total = 0.0
        for i in range(0, len(self.titular)):
            self.cheque_especial_total += float(self.titular[i].cheque_especial)
        self.cheque_especial_inicial = self.cheque_especial_total
        if self.saldo < 0.0:
            self.cheque_especial_total += self.saldo

    def depositar(self, valor):
        if self.status:
            if self.saldo < 0.0:
                if (self.saldo + valor) <= 0.0:
                    self.cheque_especial_total += valor
                    self.saldo += valor
                else:
                    self.cheque_especial_total = self.cheque_especial_inicial
                    self.saldo += valor
            else:
                self.saldo += valor
        else:
            print('Operação não realizada. Conta inativa. ')

    def sacar(self, valor):
        if self.status:
            if (self.saldo - valor) >= 0.0:
                self.saldo -= valor
            elif abs(self.saldo - valor) <= self.cheque_especial_total:
                if self.saldo <= 0.0:
                    self.saldo -= valor
                    self.cheque_especial_total -= valor
                else:
                    self.saldo -= valor
                    self.cheque_especial_total += self.saldo
            else:
                print('Operação não realizada. Saldo insuficiente.')
        else:
            print('Operação não realizada. Conta inativa.')

    def apresenta_titulares(self):
        nomes = ''
        for i in range(0, len(self.titular)):
            nomes = nomes + f'{i + 1}: {self.titular[i].nome} '
        return nomes

    def __str__(self):
        return (
            f'Conta {self.numero_da_conta}, '
            f'Titular(es): {self.apresenta_titulares()}, '
            f'Saldo: {self.saldo}, '
            f'Cheque especial disponível: {self.cheque_especial_total}, '
            f'Ativa: {self.status}'
        )


class Banco_Delas:
    def __init__(self):
        self.contas_abertas = []

    def menu(self):
        print('Sistema Banco Delas. Qual operação que deseja realizar? \n')
        print('Contas abertas:')
        for conta in self.contas_abertas:
            print(conta)
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
            if self.buscar_conta(numero) is not False:
                print(self.buscar_conta(numero))
                print('Detalhes sobre titular(res):')
                for titular in self.buscar_conta(numero).titular:
                    print(titular)
            else:
                self.buscar_conta(numero)
            self.menu()
        elif opcao_menu == '3':
            numero = input('Digite o número da conta: ')
            if self.buscar_conta(numero) is not False:
                print(self.buscar_conta(numero))
                valor = self.pedir_valor('Valor que deseja sacar: ')
                self.buscar_conta(numero).sacar(valor)
                print(f'Saldo atual: {self.buscar_conta(numero).saldo}')
                print(f'Cheque especial disponível: {self.buscar_conta(numero).cheque_especial_total}')
            else:
                self.buscar_conta(numero)
            self.menu()
        elif opcao_menu == '4':
            numero = input('Digite o número da conta: ')
            if self.buscar_conta(numero) is not False:
                print(self.buscar_conta(numero))
                valor = self.pedir_valor('Valor que deseja depositar: ')
                self.buscar_conta(numero).depositar(valor)
                print(f'Saldo atual: {self.buscar_conta(numero).saldo}')
                print(f'Cheque especial disponível: {self.buscar_conta(numero).cheque_especial_total}')
            else:
                self.buscar_conta(numero)
            self.menu()
        elif opcao_menu == '5':
            self.alterar_dados()
        elif opcao_menu == '6':
            self.fechar_conta()
        elif opcao_menu == '7':
            print('Finalizando...')
            exit
        else:
            print('Opção Inválida.')
            self.menu()

    def pedir_valor(self, mensagem: str):
        while True:
            try:
                valor = float(input(mensagem))
                if valor < 0.0:
                    raise ValueError('Insira um número positivo.')
            except ValueError as e:
                print('Valor inválido: ', e)
            else:
                return valor

    def buscar_conta(self, numero: str):
        for i in range(0, len(self.contas_abertas)):
            if (self.contas_abertas[i]).numero_da_conta == numero:
                return self.contas_abertas[i]
            else:
                if i == (len(self.contas_abertas) - 1):
                    print('Conta não encontrada')
                    return False

    def abrir_conta(self):
        numero = f'{self.random_generator(6)}-{self.random_generator(1)}'
        conta = Conta_corrente(numero)
        conta.status = True
        print(f'Criação da conta número {conta.numero_da_conta} em andamento.')
        self.adicionar_titular(conta)
        self.contas_abertas.append(conta)
        self.menu()

    def adicionar_titular(self, conta: Conta_corrente):
        opcao_cadastrar = '1'
        while opcao_cadastrar != '2':
            nome = input("Nome completo da titular: ")
            telefone = input("Telefone da titular: ")
            renda = self.pedir_valor('Renda mensal da titular: ')
            opcao_mulher = self.valida_confirmacao(f'{nome} se autodeclara mulher?')
            if opcao_mulher == '1':
                conta.titular = Mulher(nome, telefone, renda)
            else:
                conta.titular = Not_mulher(nome, telefone, renda)
            opcao_cadastrar = self.valida_confirmacao(
                'Deseja cadastrar mais titulares para essa conta?'
            )

    def fechar_conta(self):
        numero = input('Número da conta a ser desativada: ')
        if self.buscar_conta(numero).saldo != 0.0:
            print(
                    'Operação não realizada. ' +
                    'Conta com saldo ou utilizando limite do cheque especial.'
            )
        else:
            if self.buscar_conta(numero) is not False:
                if self.buscar_conta(numero).status:
                    mensagem = f'Tem certeza que deseja desativar a conta {numero}?'
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        self.buscar_conta(numero).status = False
                    else:
                        print('Operação abortada. Voltando ao menu principal...')
                else:
                    print('Operação não realizada. Conta já está inativa.')
            else:
                self.buscar_conta(numero)
        self.menu()

    def alterar_dados(self):
        numero = input('Número da conta a ser alterada: ')
        if self.buscar_conta(numero) is not False:
            while True:
                try:
                    escolha = int(
                        input(
                            f'O que deseja realizar na conta {numero}? \n'
                            '1 - Adicionar titular \n'
                            '2 - Remover titular \n'
                            '3 - Alterar dados de titular \n'
                            '4 - Voltar \n'
                            'Opção número: '
                        )
                    )
                    if not(1 <= escolha <= 4):
                        raise ValueError('Escolha uma das opções de 1 a 4.')
                except ValueError as e:
                    print('Opção inválida: ', e)
                else:
                    break

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
                    titular = self.buscar_conta(numero).titular[escolha_remove - 1]
                    mensagem = f'Tem certeza que deseja remover a titular {titular}?'
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        del self.buscar_conta(numero).titular[escolha_remove - 1]
                        self.buscar_conta(numero).atualiza_cheque_especial()
                    else:
                        print('Operação abortada. voltando ao menu principal...')
                self.menu()

            def opcao3():
                while True:
                    try:
                        escolha_alterar = int(
                            input(
                                'O que deseja alterar? \n' +
                                '1 - Nome de um titular \n' +
                                '2 - Telefone de um titular \n' +
                                '3 - Renda mensal de um titular \n' +
                                '4 - Identidade de gênero \n' +
                                '5 - Voltar \n' +
                                'Opção número: '
                            )
                        )
                        if not(1 <= escolha_alterar <= 5):
                            raise ValueError('Escolha uma das opções de 1 a 5.')
                    except ValueError as e:
                        print('Opção inválida: ', e)
                    else:
                        break

                def opcao31():
                    print(f'De qual titular deseja alterar o nome?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_nome = int(input('Titular número: '))
                    nome_antigo = self.buscar_conta(numero).titular[escolha_nome - 1].nome
                    novo_nome = input('Escreva o novo nome: ')
                    mensagem = f'Confirma a alteração do nome {nome_antigo} para {novo_nome}?'
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_nome - 1]._nome = novo_nome
                    else:
                        print('Operação abortada. Nada foi alterado')
                    self.menu()

                def opcao32():
                    print(f'De qual titular deseja alterar o telefone?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_telefone = int(input('Titular número: '))
                    nome = f'{self.buscar_conta(numero).titular[escolha_telefone - 1].nome}:'
                    telefone_antigo = self.buscar_conta(numero).titular[escolha_telefone - 1].telefone
                    telefone = input(f'Escreva o novo número de telefone do titular {nome}')
                    mensagem = f'Confirma a alteração do telefone {telefone_antigo} para {telefone}?'
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_telefone - 1].telefone = telefone
                    else:
                        print('Operação abortada. Nada foi alterado')
                    self.menu()

                def opcao33():
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
                    mensagem = (
                        f'Confirma a alteração da renda mensal do titular {titular} ' +
                        f'de {renda_antiga} para {renda}?'
                    )
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_renda - 1].renda_mensal = renda
                        self.buscar_conta(numero).atualiza_cheque_especial()
                    else:
                        print('Operação abortada. Nada foi alterado')
                    self.menu()

                def opcao34():
                    print(f'De qual titular deseja alterar a identidade de gênero?')
                    print(self.buscar_conta(numero).apresenta_titulares())
                    escolha_genero = int(input('Titular número: '))
                    titular = self.buscar_conta(numero).titular[escolha_genero - 1].nome
                    genero_antigo = self.buscar_conta(numero).titular[escolha_genero - 1].mulher
                    mensagem = (
                        f'Confirma a alteração da identidade de gênero de {titular} para mulher: ' +
                        f'{not(genero_antigo)}?'
                    )
                    confirmacao = self.valida_confirmacao(mensagem)
                    if confirmacao == '1':
                        self.buscar_conta(numero).titular[escolha_genero - 1].mulher = not(genero_antigo)
                        self.buscar_conta(numero).atualiza_cheque_especial()
                    else:
                        print('Operação abortada. Nada foi alterado')
                    self.menu()

                def opcao35():
                    self.menu()

                opcoes_alteracao = {1: opcao31, 2: opcao32, 3: opcao33, 4: opcao34, 5: opcao35}
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

    def valida_confirmacao(self, mensagem: str):
        while True:
            try:
                valor = input(mensagem + '\n(1 - Sim | 2 - Não): ')
                if not (valor == '1' or valor == '2'):
                    raise ValueError('Opção inválida.')
            except ValueError as e:
                print(e)
            else:
                return valor

    def __str__(self):
        return f'Contas abertas: {self.contas_abertas}'


banco = Banco_Delas()
banco.menu()
