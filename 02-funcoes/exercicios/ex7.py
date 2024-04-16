'''Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê)
e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.'''

import random

def escolher_palavra():

    palavras = ["python", "programacao", "latorre", "computador", "quirino", "ifsp", "java", "info", "dell", "vscode"]
    return random.choice(palavras)

def jogo_da_forca():
    palavra = escolher_palavra()
    
    tentativas_restantes = 6
    
    palavra_oculta = ['_' for _ in palavra]
    
    letras_adivinhadas = set()
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas_restantes > 0:
        print("\nPalavra: ", ' '.join(palavra_oculta))
        
        print("Letras já adivinhadas: ", ' '.join(sorted(letras_adivinhadas)))
        
        palpite = input("Digite uma letra para adivinhar: ").lower()
        
        if palpite in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.add(palpite)
        
        if palpite in palavra:
            print("Boa! A letra está na palavra.")
            
            for index, char in enumerate(palavra):
                if char == palpite:
                    palavra_oculta[index] = palpite
            
            if '_' not in palavra_oculta:
                print("\nParabéns! Você adivinhou a palavra: ", palavra)
                break
        else:
            tentativas_restantes -= 1
            print(f"Letra incorreta! Você tem {tentativas_restantes} tentativas restantes.")
        
        if tentativas_restantes == 0:
            print(f"\nVocê perdeu! A palavra era: {palavra}")



jogo_da_forca()