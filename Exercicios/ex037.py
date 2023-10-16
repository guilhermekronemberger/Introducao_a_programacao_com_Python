n = int(input('Digite a tabuada que deseja: '))
inicio = int(input('De: '))
fim = int(input('Até: '))

x = inicio

while x <= fim:
    print(f'{n}x{x} = {n * x}')
    x += 1
