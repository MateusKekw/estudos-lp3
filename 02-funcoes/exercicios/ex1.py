'''Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente.
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.'''

import random

def jogo_adivinhar_numero():
    
    numero_secreto = random.randint(1, 100)
    
    print("Adivinhe o número secreto entre 1 e 100!")
    
    while True:
        # Pede ao usuário para digitar um palpite
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        # Verifica se o palpite está correto, muito alto ou muito baixo
        if palpite < numero_secreto:
            print("Seu palpite está muito baixo.")
        elif palpite > numero_secreto:
            print("Seu palpite está muito alto.")
        else:
            print(f"Parabéns! Você adivinhou o número secreto: {numero_secreto}")
            break


jogo_adivinhar_numero()