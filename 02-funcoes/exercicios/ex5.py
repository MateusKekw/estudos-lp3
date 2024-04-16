'''Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e
verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).'''


def verificar_palindromo(texto):
   
    # Remove espaços e pontuações, e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    
    # Verifica se o texto limpo é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

texto = input("Digite uma palavra ou frase: ")
    
    # Verifica se é um palíndromo
if verificar_palindromo(texto):
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')