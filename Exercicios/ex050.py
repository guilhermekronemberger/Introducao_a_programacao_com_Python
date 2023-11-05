while True:
    print('=' * 30)
    print('MENU' .center(30))
    print('=' * 30)
    print(' 1 - Adição')
    print(' 2 - Subtração')
    print(' 3 - Divisão')
    print(' 4 - Multiplicação')
    print(' 5 - Sair')
    print('=' * 30)
    option = int(input('Escolha uma opção: '))

    if option == 5:
        break

    elif 1 <= option < 5:
        n = int(input('Tabuada de: '))
        x = 1
        
        while x <= 10:
            if option == 1:
                print(f'{n} + {x:2} = {n + x}')
            elif option == 2:
                print(f'{n} - {x:2} = {n - x}')
            elif option == 3:
                print(f'{n} / {x:2} = {n / x:.2f}')
            elif option == 4:
                print(f'{n} x {x:2} = {n * x}')
            x += 1
    else:
        print('ERRO! Opção inválida.')
