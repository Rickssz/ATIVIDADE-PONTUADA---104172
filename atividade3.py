import os
os.system('cls')

#entrada de dados
valor_A=int(input("Digite o valor de A: "))
valor_B=int(input("Digite o valor de B: "))
valor_C: int

#processamento
if valor_A == valor_B:
    valor_C = valor_A + valor_B
    print(f"O valor de A e B são iguais, então serão somados ")
else:
    valor_C = valor_A * valor_B
    print(f"O valor de A e B são diferentes, então serão multiplicados")
#saida
print(f"Valor de C: {valor_C}")
