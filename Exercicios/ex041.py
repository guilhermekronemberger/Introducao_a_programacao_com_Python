deposito = float(input('Depósito inicial: R$'))
taxa = float(input('Taxa de juros da poupança: '))

mes = 1
saldo = deposito

while mes <= 24:
    saldo += saldo * (taxa / 100)
    print(f'{mes:2}º mês = R${saldo:.2f}')
    mes += 1

print(f'O total ganho com juros no período foi de R${saldo - deposito:.2f}')
