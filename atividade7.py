import os
os.system('cls')

#Entrada de dados
produto = "doritos"
preco_unid = 5.00
quantidade = (int(input("Digite a quantidade de doritos: ")))
total = preco_unid * quantidade

#processamento
if quantidade<= 5:
    desconto = 0.02
    total = total - (total * desconto)
elif quantidade > 5 and quantidade <= 10:
    desconto = 0.03
    total = total - (total * desconto)
elif quantidade > 10:
    desconto = 0.05
    total = total - (total * desconto)

#saida
print('\n---RESUMO---')
print(f'Produto: {produto}')
print(f'Quantidade do produto: {quantidade}')
print(f'Preço do produto: R$ {preco_unid:.2f}')
print(f'desconto: R$ {desconto:.2f}')
print(f'total a pagar: R$ {total:.2f}')
