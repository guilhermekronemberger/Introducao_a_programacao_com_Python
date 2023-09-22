preco = float(input('Digite o preco do produto: R$'))
porcentagem = float(input('Digite a porcentagem de desconto: '))

desconto = preco * porcentagem / 100
novo_preco = preco - desconto

print(f'O valor atual do produto é de R${preco:.2f}\n'
      f'Um desconto de {porcentagem}%, representa um desconto de R${desconto:.2f}\n'
      f'Com este desconto, o produto passa a custar R${novo_preco:.2f}')
