while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        print('ERRO! Digite apenas números positivos.')
    if n >= 0:
        break

if n >= 1:
    if n == 1:
        print(f'O primeiro número primo é:')
    else:
        print(f'Os {n} primeiros números primos são: ')
    print('2')
    contador = 1
    y = 3
    while contador < n:
        x = 3
        while x < y:
            if y % x == 0:
                break
            x += 2
        if x == y:
            print(x)
            contador += 1
        y = y + 2
