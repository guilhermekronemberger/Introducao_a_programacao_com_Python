ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))

while True:
    print(f'Total de {len(fila1)} clientes na FILA 1')
    print(f'Fila atual: {fila1}')
    print(f'Total de {len(fila2)} clientes na FILA 2')
    print(f'Fila atual: {fila2}')
    print('Digite (F) para adicionar na fila 1, e (G) para adicionar na fila 2')
    print('Digite (A) para atender da fila 1, e (B) para atender da fila 2')
    print('Digite (S) para sair do programa:')
    operacao = str(input('\nOperação (F, G, A, B ou S): ')).strip().upper()

    contador = 0
    sair = False
    while contador < len(operacao):
        if operacao[contador] == 'A':
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f'Cliente {atendido} da FILA 1 atendido')

            else:
                print(f'Fila 1 vazia! Ninguém para atender.')

        elif operacao[contador] == 'B':
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f'\nCliente {atendido} da FILA 2 atendido.')

            else:
                print(f'Fila 2 vazia! Ninguém para atender.')

        elif operacao[contador] == 'F':
            ultimo = len(fila1) + 1
            fila1.append(ultimo)
            print('Chegou um cliente ao final da fila 1.')
            print(f'Existem {len(fila1)} clientes na fila 1.')
            print(f'Fila atual: {fila1}')

        elif operacao[contador] == 'G':
            ultimo = len(fila2) + 1
            fila2.append(ultimo)
            print('\nChegou um cliente ao final da fila 2.')
            print(f'Existem {len(fila2)} clientes na fila 2.')
            print(f'Fila atual: {fila2}')

        elif operacao[contador] == 'S':
            sair = True
            break
        
        else:
            print('Operação inválida! Digite apenas F, A ou S!')
        contador += 1

    if sair:
        break

print('Fim da execução!')
