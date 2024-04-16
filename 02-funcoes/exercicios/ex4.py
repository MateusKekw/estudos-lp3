'''Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. '''

votos = {
        1: 0,  
        2: 0,  #inicializa os votos para os candidatos A,B e C
        3: 0   
    }

def votar():
  
    print("\nEscolha um candidato para votar:")
    print("1. LaTorre")
    print("2. Quirino")
    print("3. Motta")
    
    # Recebe a escolha do usuário
    while True:
        try:
            escolha = int(input("Digite o número do candidato (1, 2 ou 3): "))
            if escolha in [1, 2, 3]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def main():
    try:
        num_votos = int(input("Quantas vezes você gostaria de votar? "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return
    
    # Coleta os votos
    for _ in range(num_votos):
        escolha = votar()
        votos[escolha] += 1
    
    # Exibe o número de votos de cada candidato
    print("\nResultado da votação:")
    print(f"LaTorre: {votos[1]} votos")
    print(f"Quirino: {votos[2]} votos")
    print(f"Motta: {votos[3]} votos")
    
    # Determina o vencedor com base no maior número de votos
    vencedor = max(votos, key=votos.get)
    
    # Exibe o vencedor
    print(f"\nO vencedor é o Candidato {'ABC'[vencedor - 1]} com {votos[vencedor]} votos!")

main()