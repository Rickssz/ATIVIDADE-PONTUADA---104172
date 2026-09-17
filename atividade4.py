import os
os.system('cls')

#Entrada de dados
kg_morango = float(input('Digite a quantidade de morangos (em Kg): '))
kg_maca = float(input('Digite a quantidade de maçãs (em Kg): '))

#processamento
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total_kg = kg_morango + kg_maca
total_compra = preco_morango + preco_maca

if total_kg >= 10 or total_compra > 15.00:
    desconto = total_compra * 0.10
    total_final = total_compra - desconto
    print('\nParabéns! Você recebeu 10% de desconto')
else:
    total_final = total_compra

# saida
print('--- RESUMO DA COMPRA ---')
print(f'Total de frutas: {total_kg:.2f} Kg')
print(f'Valor a ser pago: R$ {total_final:.2f}')
    print(f'valor do desconto: R$ {desconto:.2f}.')
