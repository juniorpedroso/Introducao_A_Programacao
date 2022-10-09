ultimo = 10
fila = list(range(1, ultimo + 1))
continua = True

def atend():
    if len(fila) > 0:
        atendido = fila.pop(0)
        print(f'Cliente {atendido} atendido')
    else:
        print('Fila vazia! Ninguém para atender.')

def novo(qtd):
    qtd += 1 # incrementa o ticket do novo cliente
    fila.append(qtd)
    return qtd


while continua:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    # operacao = input('Operação (F, A ou S): ').upper()
    option = input('Operação (F, A ou S): ').upper()
    for i in range(len(option)):
        if option[i] == 'A':
            atend()
        elif option[i] == 'F':
            ultimo = novo(ultimo)
        elif option[i] == 'S':
            print('Saindo....\n')
            continua = False
            break
        else:
            print('Operação inválida! Digite apenas F, A ou S!')
