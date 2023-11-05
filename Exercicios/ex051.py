n = int(input('Digite um número inteiro: '))

if n < 0:
    print('Opção inválida! Digite apenas números positivos.')
if n == 0 or n == 1:
    print(f'{n} não é número primo! 0 e 1 são casos especiais.')

else:
    if n == 2:
        print(f'{n} é o único número par que é primo.')
    elif n % 2 == 0:
        print(f'{n} não é primo. O número 2 é o único número par primo.')
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
            x += 2
        if x == n:
            print(f'{n} é um número primo!')
        else:
            print(f'{n} não é número primo!')
