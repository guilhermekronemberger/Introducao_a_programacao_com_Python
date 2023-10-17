n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

c = 1
r = 0

while c <= n1:
    r += n2
    c += 1
print(f'{n1} x {n2} = {r}')
