# Exercício 6.18 Escreva um programa que gere um dicionário, em que cada chave seja
# um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.

import fractions

letras = {}
frase = input('Digite uma frase: ')
for letra in frase:
    if letra != ' ':
        # if letra in letras:
        #     letras[letra] += 1
        # else:
        #     letras[letra] = 1
        letras[letra] = letras.get(letra, 0) + 1

print(letras)
for k, v in letras.items():
    print(f'Letra {k} - qtd: {v}')