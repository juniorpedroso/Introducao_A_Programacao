# Programa 6.21 - Obtenção do preço com um dicionário
tabela = {'Alface': 0.45,
          'Batata': 1.20,
          'Tomate': 2.30,
          'Feijão': 1.50}
while True:
    produto = input('Digite o nome do produto (fim para terminar): ')
    if produto == 'fim':
        print('Saindo...')
        break
    if produto in tabela:
        print(f'Preço {tabela[produto]:5.2f}')
    else:
        print('Produto não encontrado!')
        