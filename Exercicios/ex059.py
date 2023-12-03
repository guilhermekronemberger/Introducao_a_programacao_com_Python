ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'Existem {len(fila)} clientes na fila:')
    print(f'Fila atual: {fila}')
    print(f'Digite (F) para adicionar um cliente ao fim da fila,')
    print(f'(A) para realizar atendimento. (S) para sair: ')
    operacao = str(input('Operação (F, A ou S): ')).strip().upper()

    contador = 0
    sair = False

    while contador < len(operacao):
        if operacao[contador] == 'A':
            if len(fila) > 0:
                atendimento = fila.pop(0)
                print(f'\nCliente {atendimento} atendido')
            else:
                print(f'Fila vazia! Ninguém para atender')

        elif operacao[contador] == 'F':
            ultimo += 1
            fila.append(ultimo)
            print('\nChegou um cliente ao final da fila.')
            print(f'Existem {len(fila)} clientes na fila')
            print(f'Fila atual: {fila}')

        elif operacao[contador] == 'S':
            sair = True
            break

        else:
            print('Operação inválida! Digite apenas F, A ou S!')
        contador += 1

    if sair:
        break

print('Fim da execução!')
