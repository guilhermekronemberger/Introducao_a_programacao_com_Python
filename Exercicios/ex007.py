numeros = [5, 5.0, 4.3, -2, 100, 1.333]

print(f'{"Número":<10} {"Tipo numérico":<15}')
for n in numeros:
    print(f'{n:<10} ', end="")
    if isinstance(n, int):
        print(f'{"Inteiro":<15}')
    else:
        print(f'{"Ponto flutuante":<15}')
