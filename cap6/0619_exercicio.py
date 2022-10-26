# Exercício 6.19 - Escreva um programa que compare duas listas. Utilizando operações
# com conjuntos, imprima:
# - os valores comuns às duas lista
# - os valores que só existem na primeira
# - os valores que existem apenas na segunda
# - uma lista com os elementos não repetidos nas duas listas
# - a primeira lista sem os elementos repetidos na segunda

lista1 = [1, 2, 3, 4, 'a', 'b', 'c']
lista2 = ['a', 'b', 'c', 'd', 'e']

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

print('os valores comuns às duas lista')
for i in range(lista1):
    if i == len(lista1)
    if lista1[i] in lista2:
        print(f'{lista1[i]}, 'end='')