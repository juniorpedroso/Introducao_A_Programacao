# Programa 6.15 Impressão de uma lista de compras letra a letra
l = ['maçãs', 'peras', 'kiwis', 'abacate']

for s in l:
    for letra in s:
        if letra == s[-1]:
            print(letra)
        else:
            print(letra, end='')
        
    