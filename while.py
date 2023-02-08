numero_sorteado = 15
numero_escolhido = int(input('Escolha m numero entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('você errou, tente novamente...')
    
    numero_escolhido = int(input('Escolha m numero entre 1 e 20: '))
    
print('você acertou ')