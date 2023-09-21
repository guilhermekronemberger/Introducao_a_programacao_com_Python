salario = float(input('Digite o seu salário: R$'))
porcentagem = int(input('Digite a porcentagem de aumento: '))

total = salario + (salario * porcentagem / 100) 

print(f'O seu salário atual R${salario:.2f}\n'
      f'Com aumento de {porcentagem}% passará a ser R${total:.2f}')
