dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f'Convertido em segundos é igual a {total} segundos')
