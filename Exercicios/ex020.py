km = int(input("Digite a quantidade de KM percorridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))

valor_km = km * 0.15
valor_dias = dias * 60
total = valor_km + valor_dias

print(f'O total a pagar é de R${total}')
