def verificar(string):
    frase = string.lower()
    indesejados = ' ,.;:@!?-' 
    novafrase = ''

    for letra in frase:   
        if letra in indesejados:
            letra.replace(letra, '') 
        else:
            novafrase += letra  
    
    frase_invertida = novafrase[::-1] 

    if frase_invertida != novafrase: 
        print('Está frase não é um Palíndromo!')

    else:
        print(f'A frase {novafrase} invertida é {frase_invertida}.\n' 
            f'Está frase é um Palíndromo!')


verificar(str(input('Digite sua frase: ')))
