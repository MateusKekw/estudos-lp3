#Ex01: Escreva um programa em Python que solicite ao usuário um número inteiro e apresenta seu antecessor e sucessor

numero = int (input("Digite um número:")) 
#Converte a entrada do usuario de String pra Int

print(type(numero))

print("Antecessor do número digitado:", numero-1)
print("Sucessor do número digitado:", numero+1)