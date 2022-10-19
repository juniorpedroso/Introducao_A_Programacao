l = [1, 2, 3, 4, 5]
fim = 5
print(l)
while fim > 1:
    trocou = False
    cont = 0
    while cont < (fim - 1):
        if l[cont] < l[cont + 1]:
            trocou = True
            l[cont], l[cont + 1] = l[cont + 1], l[cont]
        cont += 1
        print(l)
    if not trocou:
        break
    fim -= 1
