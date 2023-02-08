def saudacao():
    print('Seja Bem-Vindo')
    print('ola,é um prazer ter você fazendo parte desse curso')
    

saudacao()

#função com parametros

def saudacao(nome,curso):
    print(f'Seja Bem-Vindo,{nome}')
    print(f'ola,é um prazer ter você fazendo parte do curso de {curso}')
    
saudacao('jeferson','python')

#função com parametro default

def saudacao(nome,curso='python'):
    print(f'Seja Bem-Vindo,{nome}')
    print(f'ola,é um prazer ter você fazendo parte do curso de {curso}')
    
saudacao('jeferson',)

#funções com retorno

def soma(num1,num2):
    return num1+num2

resultado=soma(5,7)

print('O resultado da soma é ',soma)