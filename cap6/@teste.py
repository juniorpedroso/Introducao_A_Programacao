import enum


l = [5, 9, 13]
x = 0
for e in l:
    print(f'{x} {e}')
    x += 1

for x, e in enumerate(l):
    print(f'{x} -> {e}')
