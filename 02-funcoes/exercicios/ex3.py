'''Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.'''

frase = input('Digite uma frase para ser analisada:\n')

def cont_letras(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vogais = 0
    num_consoantes = 0

    for char in frase:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes +=1
    
    return num_vogais, num_consoantes

num_vogais, num_consoantes = cont_letras(frase)

print(f"Na frase, há {num_vogais} vogais e {num_consoantes} consoantes.")