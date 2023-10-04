ano_carro = int(input('Digite o ano do seu carro: '))

ano_atual = 2023
tempo_uso = ano_atual - ano_carro

if tempo_uso <= 3:
    print('Seu carro é novo!')

else:
    print('Seu carro é velho!')
