salario = float(input('Salário: R$'))
aumento = float(input('Porcentagem de aumento? '))

novo_salario = salario + (salario * aumento / 100)
print(f'O salário de R${salario:.2f}, com {aumento}% de aumento, passa a ser: R${novo_salario}')
