import os
os.system('cls')

#tabela
print('---TABELA DE COR')
print('1. VERDE')
print('2. AZUL')
print('3. AMARELO')
print('4. VERMELHO')

#entrada
print('\nPra saber o preço digite a cor desejada.')
cor = input(('digite a cor que deseja: ')).upper()

#processamento e saida
match cor:
    case 'VERDE':
        print('Valor do verde é de: R$ 10.00')
    case 'AZUL':
        print('Valor do verde é de: R$ 20.00')
    case 'AMARELO':
        print('Valor do verde é de: R$ 30.00')
    case 'VERMELHO':
        print('Valor do verde é de: R$ 40.00')
