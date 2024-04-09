'''Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente.
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.'''

import random


num = random.randint(1, 100)

chute = int(input('Adivinhe um número inteiro entre 1 e 100: '))

def adivinha_maior(chute, num):
    if chute < num:
        chute = int(input('Tente um número maior: '))
    
def adivinha_menor(chute, num):
    if chute > num:
        chute = int(input('Tente um número menor: '))

def numero_fora(chute, num):
    if chute > 100 or chute < 1:
        return'Sua tentativa foi para fora da área'

def numero_correto(chute, num):
    if chute == num:
        return 'parabéns você acertou o número'

while chute != num:

    if num > chute:
        print(adivinha_maior(chute, num))

    if num < chute:
        print(adivinha_menor(chute, num))

    print(numero_fora(chute, num))
    print(numero_correto(chute, num))





