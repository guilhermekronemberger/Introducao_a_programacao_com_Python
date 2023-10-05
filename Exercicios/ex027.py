km = float(input('Quantos KM deseja percorrer? '))

if km <= 200:
    valor = km * 0.50 

else:
    valor = km * 0.45

print(f'O preço da passagem será R${valor:.2f}')
