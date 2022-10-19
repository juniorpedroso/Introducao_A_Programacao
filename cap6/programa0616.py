# Programa 6.16 - Listas com elementos de tipos diferentes
produto1 = ['maçã', 10, 0.30]
produto2 = ['pera', 5, 0.75]
produto3 = ['kiwi', 4, 0.98]

def imprimePro(pro):
    print(f'{pro[0]:6} - ', end='')
    print(f'{pro[1]:3} - ', end='')
    print(f'{pro[2]:5.2f}')

print('---------------------')
print('prod     qtd    valor')
print('---------------------')
imprimePro(produto1)
imprimePro(produto2)
imprimePro(produto3)