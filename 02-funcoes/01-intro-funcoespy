#funcoes

# Funcao sem retorno sem parâmetros
def saudar():
    print('Bom Dia, Maria')

saudar()

# Funcao sem retorno com parâmetros
# Parâmetros x Argumentos
# Argumento é o valor (Literal)
# ou referência enviada a um parametro
def imprimir_nome(nome):
    print(f'nome: {nome}')

nome = 'Mateus'
imprimir_nome(nome)

# Funcao com retorno sem parâmetros
def gerar_saudacao():
    return "Bom Dia"

saudacao = gerar_saudacao()
print(saudacao)


# Função com retorno e com parâmetros
def gerar_saudacao_para(nome):
    return f'Bom Dia {nome}'

saudacao_cleide = gerar_saudacao_para('Cleide')
print(saudacao_cleide)

print(gerar_saudacao_para('José'))

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






