n = float(input('Digite um número para achar a raiz quadrada: '))

b = 2
p = 0

while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f'A raiz quadrada de {n} é aproximadamente {p:.4f}')
