def IMC (kg, m):
    m = m/100
    result = kg / (m*m)
    return result

def classi(imc):
    if imc < 18.5 :
        return 'Baixo Peso'
    elif imc >= 18.5 and imc <= 24.9 :
        return 'Peso Normal'
    elif imc >= 25.0 and imc <= 29.9:
        return 'Excesso de Peso'
    elif imc >= 30.0 and imc <= 34.9:
        return 'Obesidade Classe 1'
    elif imc >= 35.0 and imc <= 39.9:
        return 'Obessidade Classe 2'
    else:
        return 'Obesidade Classe 3'
    
def ajuste(imc):
    if imc < 18.5:
        return 'Você deve ganhar peso para atingir o peso saudável e normal'
    elif imc >= 18.5 and imc <= 24.9 :
        return 'Você está em um peso saudável e normal'
    elif imc >= 25.0 and imc <= 29.9:
        return 'Você deve perder peso, mas isso não afeta sua saúde ainda'
    elif imc >= 30.0 and imc <= 34.9:
        return 'Você deve perder peso, está começando a ficar perigoso para você'
    else:
        return 'Você tem que perder peso imediatamente, sua vida está em um risco enorme agora'





