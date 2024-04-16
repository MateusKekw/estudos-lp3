#funcoes
# programa que normalmente tem uma entrada, processamento e saída (vc manda algo, ela faz alguma coisa com a entrada e te manda algo)

# declaração:
# def nomeDaFunção (parâmetros):
#   algum comando etc
#   return 

# Funcao sem retorno sem parâmetros
def saudar():
    print('Bom Dia, Maria')

saudar()

# Funcao sem retorno com parâmetros(um ou mais)
def imprimir_nome(nome):
    print(f'nome: {nome}')

nome = 'Mateus'
imprimir_nome(nome)

# Funcao com retorno sem parâmetros
def gerar_saudacao():
    return "Bom Dia"

saudacao = gerar_saudacao()
print(saudacao)


# Função com retorno e com parâmetro(s)
def gerar_saudacao_para(nome):
    return f'Bom Dia {nome}'

saudacao_cleide = gerar_saudacao_para('Cleide')
print(saudacao_cleide)

print(gerar_saudacao_para('José'))

# Parâmetros x Argumentos
# parâmetro é a referência definida na assinatura da função (pq vc pode acessar nome em qualquer lugar dentro da função) --> 
# argumento é o valor (literal) ou a referência passada ou enviada para um parâmetro (pode passar um literal diretammente, ou o valor de uma variável (a referência))
# return não é obrigatório em funções, mas é "horrível" sem retorno
# em Python não tem sobrecarga



# Chamada da função:
print("Olá") # uma função já declarada em algum lugar, aqui é só a chamada dela 
saudar() # tem que ter o (), mesmo que seja vazio    
# não dá pra chamar a função antes de declarar ela
imprimir_nome("Clefairy") # Jô é o valor, o argumento que eu tô passando pro argumento nome

print(saudar()) # ou
saudacao = saudar() # assim é melhor (?)
print(saudacao)

print(gerar_saudacao_para("José")) # ou
saudacaoMa = gerar_saudacao_para("Matias")
print(saudacaoMa)



# FUNÇÕES
# return  parametros
#   0         0
#   0         1
#   1         0
#   1         1     (melhor caso)

# Imprimir saudação
# Gerar: Bom dia NOME (dinâmico)
# Imprimir

def saudacoes(nome):
    print(f'Bom Dia, {nome}')

# Função Pura 
# não possui efeito colateral
# sem acesso a estado
def saudades(nome):
    return f'Bom Dia, {nome}'

# Calcule a média de vários alunos e imprima
# entrada = [[10, 6], [5, 9], [9, 6]]
# calcular_media - lista de notas - médias
# calcular_medias - lista de lista de nota - lista de média
# imprimir - lista de media

notas_alunos = [
    [10.0, 6.0],
    [5.0, 9.0],
    [9.0, 6.0],
]

def calcular_media(notas):
    return sum(notas)/len(notas)

def calcular_medias(notas_alunos):
    return [calcular_media(notas) for notas in notas_alunos] 


def calcula_medias(notas_alunos):
    medias = []

    for notas in notas_alunos:
        medias.append(calcular_media(notas))

    return medias


print(calcular_media(notas_alunos[0]))

print(calcular_medias(notas_alunos))

print(calcula_medias(notas_alunos))



print('Olá ', ' Mundo', sep='PEWNEWNEW')

# Valores padrão para os parâmetros

def obter_saudacao(nome, saudacao='Bom Dia'):
    return f'{saudacao}, {nome}!'

print(obter_saudacao('Mateus'))
# *args (Non-Keyword Arguments)

def calcular_mediaaaa(notas):
    return sum(notas)/len(notas)

print(calcular_mediaaaa([10.0, 5.0, 2.0, 9.0]))

print(calcular_mediaaaa((10.0, 5.0, 2.0, 9.0)))

def calcular_mediaaaa2(*notas):
    return sum(notas)/len(notas)

print(calcular_mediaaaa2(10.0, 5.0, 2.0, 9.0, 10.0))

print(calcular_mediaaaa2(10.0, 5.0, 2.0, 9.0, 3.3, 6.2, 2.9, 10.0))

# Argumentos nomeados: quando se tem muitos parâmetrps, e você nomeia o0 argumneto na hora de chamar (esse valor vai pra esse param, esse pra outro...)
def nova_saudacao (nome, saudacao):
    return f'{saudacao}, {nome}'

print(nova_saudacao("Mathew", "Bom dia"))
print(nova_saudacao("Latorre", "Boa tarde"))
print(nova_saudacao("Igor", "Boa noite"))
# ou
print(nova_saudacao(nome = "Guilherme", saudacao ="Bodia")) #nomeou um , tem que nomear todos (no caso os prineiros não precisam ser nomeados obrigatoriamente se o 
# último tiver sido) --> se tirar a definição do nome, roda normal, se tirar a do último, não vai

print("Olá", "mundo!", sep=" qqr coisaaaa")
# sep eh acessado via argumento nomeado --> sep eh a separação

# Valores padrão para parâmetros:
def obter_saudacao(nome, saudacao = "Bom dia"):
    return f'{saudacao}, {nome}'

obtemSaudacao = obter_saudacao("Jojozita")
print(obtemSaudacao)

#sobrecarga:
obtemSaudacao2 = obter_saudacao("Cabron!", "Buenos días") # --> substituiu a saudação padrão pelo que eu coloquei
print(obtemSaudacao2)
# simula com parâmetros default

# *args (Non-Keywords Arguments)
''''
def calcular_media (notas):
    return sum(notas)/len(notas)
# nessa função, eu espero que entrem com uma lista ou um atupla de notas
'''
# calcular_media(10.0, 3.0) --> ele entende que são 2 valores
# calcular_media(7.0, 3.0, 2.0, 5.50) # --> ele entende que são 4 valores --> poderia colocar 4 param, mas:
# usa o Non-Keywords Arguments
def calcular_media (*notas):
    print(type(notas))
    return sum(notas)/len(notas)
# --> * fala que pode passar qqr número de valores nos args, e o python transforma isso em uma TUPLA (o type ali foi só pra comprovar)
# sempre que ver o *, vc sabe que vai receber uma TUPLA
print(calcular_media(10.0, 10.0, 10.0, 10.0))

