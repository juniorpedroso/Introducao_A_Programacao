ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
continua = True

def atend(fila, nameFila):
    if len(fila) > 0:
        atendido = fila.pop(0)
        print(f'Cliente {atendido} atendido na {nameFila}')
    else:
        print(f'{nameFila} vazia! Ninguém para atender.')

def novo(fila, qtd, nameFila):
    qtd += 1 # incrementa o ticket do novo cliente
    fila.append(qtd)
    print(f'Acrescentado o cliente {qtd} na fila {nameFila}')
    return qtd

def showInfo():
    print('-='*10)
    print(f'\nExistem {len(fila1)} clientes na fila 1 e')
    print(f'Existem {len(fila2)} clientes na fila 2')
    print(f'Fila 1 atual: {fila1}')
    print(f'Fila 2 atual: {fila2}')
    print('-='*10)


while continua:
    showInfo()
    print('Digite (F) ou (G) para adicionar um cliente ao fim da fila,')
    print('ou (A) ou (B) para realizar o atendimento. S para sair.')
    option = input('Operação (F, G, A, B ou S): ').upper()
    for i in range(len(option)):
        if option[i] == 'A':
            atend(fila1, 'Fila 1')
        elif option[i] == 'B':
            atend(fila2, 'Fila 2')
        elif option[i] == 'F':
            ultimo1 = novo(fila1, ultimo1, 'Fila 1')
        elif option[i] == 'G':
            ultimo2 = novo(fila2, ultimo2, 'Fila 2')
        elif option[i] == 'S':
            print('Saindo....\n')
            continua = False
            break
        else:
            print('Operação inválida! Digite apenas F, A ou S!')
