'''Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100),
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.'''

def converter_pontuacao_para_nota(pontuacao):

    if pontuacao < 0 or pontuacao > 100:
        return "Pontuação fora do intervalo válido (0 a 100)."
    
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'
    
def main():
    try:
        pontuacao = float(input("Digite sua pontuação: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return
    
    nota = converter_pontuacao_para_nota(pontuacao)

    print(f"A pontuação de {pontuacao} corresponde à nota: {nota}")

main()