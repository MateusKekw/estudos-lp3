#Operadores aritmédicos
# +, - , / , % , **

nota1 = 10.0
nota2 = 7.1
nota3 = 5.3

media = (nota1 + nota2 + nota3) / 3

#10 elevado ao quadrado (2)

numero = 10
elevado_quadrado = numero * numero
elevado_quadrado = numero ** 2 

#Operadores lógicos
# and, or, not

print(2 + 3)

print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false


#"Quero um celucar preto E que rode"

verdade = True and True  # pode fazer, e será armazenado o valor booleano na var verdade

print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false

#"Quero um celucar preto OU que rode"

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 16   #Horario comercial
usuario_admin = False

funcionario_ativo = usuario_funcionario and not usuario_bloqueado
horario_comercial = hora_atual >= 8 and hora_atual <=19 #false

if (funcionario_ativo and horario_comercial) or usuario_admin:
    print("Acesso liberado")
else:
    print("Acesso negado")



# Outro arquivo

def dentro_horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual <=19

horario_comercial = hora_atual >= 8 and hora_atual <=19

# Operadores de comparação
# ==, != , > , < , >= , <=
#sera um booleano

Nota1 = 10.0
Nota2 = 7.1

if Nota1 > Nota2:
    print("Aluno foi melhor na Nota1")
else:
    print("Aluno foi melhor na Nota2 ou teve a mesma nota +9")


a = [1,2,3]
b = [1,2,3]

print(a == b)# mesmos valores, True
print(a is b)# Mesmo espaço de memoria False


#operador 

opcoes = {
        'sim': ['sim','s','y','yes'],   
        'nao': ['nao', 'n', 'no']
}


opcoes = ('sim', 'nao', 'talvez')
opcao = input('Digite uma opção')
opcao = opcao.lower()#deixar tudo minusculo
opcao = opcao.strip()#deixar sem espaço



if  opcao in opcoes:
    print('ok')
else:
    print('invalido')