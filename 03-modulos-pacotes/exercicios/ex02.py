from pac02 import *

kg = float(input('Digite seu peso em quilogramas: '))
m = float(input('Digite sua altura em cm: '))

imc = IMC(kg, m)

print(classi(imc))

print(ajuste(imc))

