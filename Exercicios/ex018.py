distancia = float(input("Digite a distância em km: "))
velocidade = float(input("Digite a velocidade média em km/h: "))

tempo = distancia / velocidade
tempo_s = int(tempo * 3600) 
horas = int(tempo_s / 3600) 
tempo_s = int(tempo_s % 3600) 
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print(f'O tempo estimado é de: {horas}h{minutos}m{segundos}s')
