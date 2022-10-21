# Exercício 6.18 Escreva um programa que gere um dicionário, em que cada chave seja
# um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.

import fractions

letras = {}
frase = input('Digite uma frase: ')
for l in range(len(frase)):
    if frase[l] != ' ':
        if frase[l] in letras:
            letras[frase[l]] += 1
        else:
            letras[frase[l]] = 1

print(letras)
for k, v in letras.items():
    print(f'Letra {k} - qtd: {v}')
    