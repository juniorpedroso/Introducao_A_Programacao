# Exercício 6.17 - Exemplo de dicionário com estoque e operação de venda
# Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a
# quantidade vendida. Verifique se o nome do produto digitado existe no dicionário,
# e só então efetue a baixa em estoque.

# Define o estoque de produtos
estoque = {'tomate': [1000, 2.30],
           'alface': [ 500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [ 100, 1.50]}

# cria uma lista para as vendas
venda = []

# Função para imprimir estoque atual
def printEstoque():
    print('<<     Estoque      >>')
    print('Produto    Qtd   Valor')
    for produto, dados in estoque.items():
        print(f'{produto:11s}', end='')
        print(f'{dados[0]:4d}', end='')
        print(f'{dados[1]:7.2f}')
    print('-=-=-=-=-=-=-=-=-=-=-=-')


printEstoque()

# Laço para solicitar produtos da venda
while True:
    prodVend = input('Digite o produto (fim para sair): ')
    if prodVend == 'fim':
        print('Saindo...')
        break
    elif prodVend in estoque:
        if estoque[prodVend][0] == 0:
            print('Produto acabou, sem estoque.')
        else:
            qtdVend = int(input('Digite a quantidade: '))
            # Se a quantidade digitada for maior que a existente
            if qtdVend > estoque[prodVend][0]:
                print(f'Quantidade superior ao estoque que é {estoque[prodVend][0]}')
            else:
                estoque[prodVend][0] -= qtdVend
                dadosVend = [prodVend, qtdVend]
                venda.append(dadosVend)
                print('Produto adicionado ao seu carrinho')
    else:
        print('Produto não encontrado.')


print('<<<<<<<  Venda efetuada   >>>>>>>')
print('Produto      qtd   valor  subtot.')

total = 0
for item in venda:
    subTotal = item[1] * estoque[item[0]][1]
    total += subTotal    
    print(f'{item[0]:12s}{item[1]:4d} {estoque[item[0]][1]:7.2f} {subTotal:7.2f}')
print(f'..................Total: {total:7.2f}\n')

printEstoque()

# total = 0
# print('Vendas\n')
# for operacao in venda:
#     produto, quantidade = operacao
#     preco = estoque[produto][1]
#     custo = preco * quantidade
#     print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
#     estoque[produto][0] -= quantidade
#     total += custo
# print(f' Custo total: {total:21.2f}\n')
# print('Estoque:\n')
# for chave, dados in estoque.items():
#     print('Descrição: ', chave)
#     print('Quantidade: ', dados[0])
#     print(f'Preço: {dados[1]:6.2f}\n')