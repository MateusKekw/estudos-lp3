from pac01 import  calcVolume, calcTermo, calcFiltragem

altu = float(input('Digite a altura do seu aquário: '))
comp = float(input('Digite o comprimento do seu aquário: '))
larg = float(input('Digite o largura do seu aquário: '))

volume = calcVolume(altu, comp, larg)

print(f'O Volume do seu aquário é equivalente a: {volume} litros')
print('')

tempDese = float(input('Digite a temperatura desejada: '))
tempAmbi = float(input('Digite a temperatura ambiente: '))

potencia = calcTermo(volume, tempDese, tempAmbi)

print(f'A Potência necessária para manter seu aquário em {tempDese}Cº é de {potencia}')
print('')

litros = calcFiltragem(volume)

print(f'A Quantidade de litros por hora na filtragem do seu aquário é de {litros}')