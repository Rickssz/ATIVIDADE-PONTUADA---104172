import os
os.system('cls || clear')

print('--- TABELA DE COMBUSTÍVEL ---')
print('(A) para Álcool')
print('(G) para Gasolina\n')

# Entrada
combustivel = input('Digite qual o tipo de combustível: ').upper()

preco_litro_alcool = 3.79
preco_litro_gasolina = 6.59

# Processamento
if combustivel == "A":
    litros = float(input("Digite a quantidade de litros: "))
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
    
    preco_final_litro = preco_litro_alcool * (1 - desconto)
    total = litros * preco_final_litro

elif combustivel == "G":
    litros = float(input("Digite a quantidade de litros: "))
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
    
    preco_final_litro = preco_litro_gasolina * (1 - desconto)
    total = litros * preco_final_litro

else:
    total = None
    print("\nOpção de combustível inválida!")

# Saída
if total is not None:
    print(f"\nCombustível selecionado: {combustivel}")
    print(f"Total a pagar: R$ {total:.2f}")