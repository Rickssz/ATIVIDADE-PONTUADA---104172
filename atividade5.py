import os
os.system('cls')

#Entrada de dados
a = int(input('digite o valor de A: '))
b = int(input('digite o valor de B: '))
operacao = input('Digite a operação escolhida: ')

#saida
if operacao == '*':
    print(a * b)
elif operacao == '+':
    print(a + b)
elif operacao == '-':
    print(a - b)
elif operacao == '/':
    if b == 0:
        print('Nenhum numero pode ser divido por 0')
    else:
        print(a / b)
else:
    print('operação invalida')
