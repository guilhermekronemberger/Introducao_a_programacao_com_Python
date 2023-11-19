notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
contador = 0


while contador < len(notas):
    notas[contador] = float(input(f'Nota {contador}: '))
    soma += notas[contador]
    contador += 1

contador = 0

while contador < len(notas):
    print(f'Nota {contador}: {notas[contador]:.1f}')
    contador += 1

print(f'Média: {soma / len(notas):.1f}')
