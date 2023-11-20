lista1 = []
lista2 = []

while True:
    n = int(input('Escreva um valor para ser adicionado a lista1 (0 para sair): '))
    if n == 0:
        break
    lista1.append(n)

print('=' * 65)
while True:
    n = int(input('Escreva um valor para ser adicionado a lista2 (0 para sair): '))
    if n == 0:
        break
    lista2.append(n)

novalista = lista1 + lista2
contador = 0

while contador < len(novalista):
    print(f'{contador}: {novalista[contador]}')
    contador += 1
