kws = float(input('Qual a quantidade de kWh consumida? '))
print('Selecione o tipo de sua instalação')
instalacao = str(input('(R) para residências, (C) para comércios e (I) para indústrias: ')).upper()

preco = 0

if instalacao == 'R':
    if kws <= 500:
        preco = kws * 0.40
    else:
        preco = kws * 0.65

if instalacao == 'C':
    if kws <= 1000:
        preco = kws * 0.55
    else:
        preco = kws * 0.60

if instalacao == 'I':
    if kws <= 5000:
        preco = kws * 0.55
    else:
        preco = kws * 0.60

else:
    print('ERRO! Tipo de instalação inválida!')

print(f'O valor a pagar é R${preco:.2f}')
