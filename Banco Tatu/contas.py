class Conta():
    """[Definição de uma conta de banco]"""

    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        """[Exibe o número da conta e o saldo atual,
        além dos nomes dos clientes e telefones]
        """
        print(f'\nCC número: {self.numero} Saldo: {self.saldo:10.2f}')
        for cliente in self.clientes:
            print(f'Cliente: {cliente.nome} telefone: {cliente.telefone}')

    def pode_sacar(self, valor):
        """[Verifica se o saldo é maior que o valor]

        Args:
            valor ([float]): [valor a sacar]

        Returns:
            [bol]: [True ou False]
        """
        return self.saldo >= valor

    def saque(self, valor):
        """[Efetua um saque no valor recebido como parâmetro,
        se a função pode_sacar permitir]

        Args:
            valor ([float]): [Valor a ser sacado do saldo]
        """
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            return True
        else:
            print(f'Saldo insuficiente!')
            return False

    def deposito(self, valor):
        """[Efetua um depósito na conta no valor passado pelo parâmetro]

        Args:
            valor ([type]): [Valor a ser depositado]
        """
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])

    def extrato(self):
        print(f'\nExtrato CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n    Saldo: {self.saldo:10.2f}\n')


class ContaEspecial(Conta):
    """[Uma classe-filha tendo como base a classe Conta]

    Args:
        Conta ([type]): [description]
    """

    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo=saldo)
        self.limite = limite

    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def extrato(self):
        print(f'\nExtrato CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n   Limite: {self.limite:10.2f}')
        print(f'    Saldo: {self.saldo:10.2f}')
        print(f'Sld Disp.: {(self.saldo + self.limite):10.2f}\n')
