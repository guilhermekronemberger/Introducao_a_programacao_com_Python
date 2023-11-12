dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))

n = dividendo

while n >= divisor:
    n -= divisor
resto = n

print(f'O resto de {dividendo} / {divisor} é {resto}')
