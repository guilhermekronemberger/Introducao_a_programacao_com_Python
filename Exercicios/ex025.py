salario = float(input('Qual o seu salário atual ? R$'))

if salario > 1250:
    novosalario = salario + (salario * 10 / 100)

else:
    novosalario = salario + (salario * 15 / 100)

print(f'Com o aumento, seu salário será: R${novosalario:.2f}')
