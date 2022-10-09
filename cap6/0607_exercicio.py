expressao = input('Digite uma expressão com parênteses: ')
pilha = []
for i in range(len(expressao)):
    print(f'Pilha Atual: {pilha}')
    if expressao[i] not in '()':
        print('Erro! Digite somente ( ou ).')
        break
    else:
        if i == 0 and expressao[i] == ')':
            print('Erro! Expressão não pode ser iniciada com )')
            break
        elif expressao[i] == '(':
            pilha.append(expressao[i])
        elif expressao[i] == ')':
            if len(pilha) == 0:
                print('Erro! Não é possível fechar um parênteses que não foi aberto.')
                break
            else:
                if pilha[-1] == '(':
                    pilha.pop(-1)
                else:
                    pilha.append(expressao[i])


print(f'Pilha Final: {pilha}')
print('FIM')
