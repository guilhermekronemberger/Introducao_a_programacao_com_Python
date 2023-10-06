n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operacao = str(input('Digite a operação desejada (+,-,* ou /): '))

if operacao == '+':
    resultado = n1 + n2

elif operacao == '-':
    resultado = n1 - n2

elif operacao == '*':
    resultado = n1 * n2

elif operacao == '/':
    resultado = n1 / n2

else:
    print('ERRO! Opção inválida!')
    resultado = 0

print(f'Resultado: {resultado:.1f}')
