'''Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e
retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada
palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário. '''

def contar_palavras(texto):

    contagem_palavras = {}
    
    palavras = texto.lower().split()
    
    for palavra in palavras:
        palavra = ''.join(char for char in palavra if char.isalnum())
        if palavra:
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1
                
    return contagem_palavras


texto = input("Digite um texto: ")
    
contagem = contar_palavras(texto)
    
print("\nContagem de palavras:")
for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")