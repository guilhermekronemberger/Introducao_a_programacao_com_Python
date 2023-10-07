valor = float(input('Digite o valor da casa: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
salario = float(input('Digite o salário: R$'))

prestacao = valor / (anos * 12) 
trinta_porcento = (salario / 100) * 30

if prestacao > trinta_porcento:
    print('Empréstimo Negado!')

else:
    print('Empréstimo Autorizado!\n'
        f'Valor da sua prestação será: R${prestacao:.2f}')
