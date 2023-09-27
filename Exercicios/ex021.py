anos_fumando = float(input('Quantos anos você fuma? '))
cigarros_por_dia = int(input('Quantos cigarros você fuma por dia: '))

reducao_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
reducao_em_dias = reducao_em_minutos / (24 * 60)

print(f'Redução de vida em {reducao_em_dias:.0f} dias.')
