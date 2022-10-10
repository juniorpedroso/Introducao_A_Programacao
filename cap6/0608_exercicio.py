# Exercício 6.8 - pequisa sequencial
lista = [15, 7, 27, 39]
pesq1 = int(input('Digite um número para procurar: '))
pesq2 = int(input('Digite outro número para procurar: '))
x = 0
while x < len(lista):
    if pesq == lista[x]:
        break
    x += 1

if x < len(lista):
    print(f'O número {pesq} foi encontrado na posição {x}.')
else:
    print(f'O número {pesq} não foi encontrado.')