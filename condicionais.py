from ast import If


media= float(input('Informe sua media: '))

if media >= 7:
    print('Você foi aprovado')
    
elif media >= 5:
    print("Recuperaçâo")
    
else:
    print("Você foi reprovado")