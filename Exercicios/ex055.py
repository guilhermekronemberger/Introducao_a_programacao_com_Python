n = input('Digite o número a verificar, sem espaços: ')

i = 0
f = len(n) - 1

while f > i and n[i] == n[f]:
    f -= 1
    i += 1

if n[i] == n[f]:
    print(f'{n} é palíndromo')

else:
    print(f'{n} não é palíndromo')
