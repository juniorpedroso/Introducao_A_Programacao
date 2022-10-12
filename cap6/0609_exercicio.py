# Exercício 6.9 - pequisa sequencial
lista = [15, 7, 27, 39]
pesq1 = int(input('Digite um número para procurar: '))
pesq2 = int(input('Digite outro número para procurar: '))
pesq1_achou = ''
pesq2_achou = ''
x = 0

while x < len(lista):
    if pesq1_achou == '':
        if pesq1 == lista[x]:
            pesq1_achou = x
    if pesq2_achou == '':
        if pesq2 == lista[x]:
            pesq2_achou = x
    x += 1

if pesq1_achou == '' and pesq2_achou == '':
    print(f'A pesquisa 1: {pesq1} e a pesquisa 2: {pesq2} não foram encontrados.')
else:
    if pesq1_achou != '' and pesq2_achou != '':
        if pesq1_achou < pesq2_achou:
            print(f'A pesquisa 1: {pesq1} foi encontrado na posição {pesq1_achou}.')
            print(f'A pesquisa 2: {pesq2} foi encontrado na posição {pesq2_achou}.')
        else:
            print(f'A pesquisa 2: {pesq2} foi encontrado na posição {pesq2_achou}.')
            print(f'A pesquisa 1: {pesq1} foi encontrado na posição {pesq1_achou}.')

    else:
        if pesq1_achou:
            print(f'A pesquisa 1: {pesq1} foi encontrado na posição {pesq1_achou}.')
        if pesq2_achou:
            print(f'A pesquisa 2: {pesq2} foi encontrado na posição {pesq2_achou}.')

