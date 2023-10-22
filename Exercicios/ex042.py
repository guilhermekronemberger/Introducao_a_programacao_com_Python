deposito_inicial = float(input('Depósito inicial: R$'))
deposito_mensal = float(input('Depósito mensal: R$'))
taxa_juros = float(input('Taxa de juros da poupança (%): '))

mes = 1
saldo = deposito_inicial

while mes <= 24:
    saldo += (saldo * (taxa_juros / 100)) + deposito_mensal
    print(f'{mes:2}º mês = R${saldo:.2f}')
    mes += 1

print(f'O total ganho com juros no período foi de R${saldo - deposito_inicial:.2f}')
