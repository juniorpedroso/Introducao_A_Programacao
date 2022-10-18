t_Mons = [-10, -8, 0, 1, 2, 5, -2, -4]
max_temp = t_Mons[0]
min_temp = t_Mons[0]

for t in t_Mons:
    if t > max_temp:
        max_temp = t
    if t < min_temp:
        min_temp = t

print(f'Temp maior -> {max_temp}')
print(f'Temp menor -> {min_temp}')