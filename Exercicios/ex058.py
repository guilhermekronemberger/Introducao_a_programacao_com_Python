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
lista3 = []

contador = 0

while contador < len(novalista):
    if novalista[contador] not in lista3:
        lista3.append(novalista[contador])
    contador += 1

contador = 0
while contador < len(lista3):
    print(f'{contador}: {lista3[contador]}')
    contador += 1
