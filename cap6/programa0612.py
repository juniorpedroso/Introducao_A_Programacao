# Programa 6.12 - Cópia de elementos para outras lista
v = [9, 8, 7, 12, 0, 13, 21]
p = []
i = []

for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)
print(f'Pares: {p}')
print(f'Impares: {i}')