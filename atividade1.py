import os
os.system ('cls')

#Entrada de dados
valorA = (input("Digite o valor de A: "))
valorB = (input("Digite o valor de B: "))
valorC = (input("Digite o valor de C: "))

#processamento
soma = valorA + valorB

#saida
if soma < valorC:
    print("a soma de A e B é menor do que o valor C")
else:
    print("a soma de A e B é maior que o valor C")
