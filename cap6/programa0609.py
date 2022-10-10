# Programa 06 09 - pequisa sequencial
lista = [15, 7, 27, 39]
pesq = int(input('Digite um número para procurar: '))
achou = False
x = 0
while x < len(lista):
    if pesq == lista[x]:
        achou = True
        break
    x += 1

if achou:
    print(f'O número {pesq} foi encontrado na posição {x}.')
else:
    print(f'O número {pesq} não foi encontrado.')
