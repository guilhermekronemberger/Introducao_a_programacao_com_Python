total = 0
quantidade = 0

while True:
    n = int(input('Digite um número: '))

    if n == 0:
        break

    else:
        quantidade += 1
        total += n

print(f'A quantidade de números digitados foi: {quantidade}')
print(f'A soma dos números foi: {total}')
print(f'A média é: { total / quantidade:.2f}')
