'''Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.'''

base = int(input('Digite um número inteiro para a tabuada:\n'))

def tabua(base):
    for cont in range(0,11):
        result = base * cont
        print(f'{base} x {cont} = {result}')

tabua(base)