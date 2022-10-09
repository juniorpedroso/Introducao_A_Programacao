from clientes import Cliente
from bancos import Banco
from contas import Conta

print()
joao = Cliente('joão da silva', '777-1234')
maria = Cliente('maria silva', '555-4321')
jose = Cliente('josé vargas', '9721-3040')
contaJM = Conta([joao, maria], 100)
contaJ = Conta([jose], 10)
tatu = Banco('Tatu')
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()
'''conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.resumo()
conta2.resumo()
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()'''
print()
