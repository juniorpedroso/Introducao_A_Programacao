l = [1, 2, 3, 4, 5]
fim = 5
print(l)
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] > l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
            print(l)
        x += 1
    if not trocou:
        break
    fim -= 1