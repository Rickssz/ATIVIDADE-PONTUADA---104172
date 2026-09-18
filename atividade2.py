import os
os.system('cls')

#Entrada de ddos
nome = input("Digite seu nome: ")
genero = input("Digite seu Gênero: F para Feminino | M para Masculino ").upper()
estado_civil = input("Digite seu estado civil: S para Solteiro(a) | C para Casado(a) ").upper()

#processamento
match genero:
    case "F":
        print("\nFeminino")
    case "M":
        print("\nMasculino")
    case _:
        print("\nGênero inválido")

match estado_civil:
    case "C":
        print("Casado(a)")
    case "S":
        print("Solteiro(a)")
    case _:
        print("Não identificado")

if genero == 'F' and estado_civil == 'C':
    casamento = int(input('Quantos anos de casada? '))

#saida
print('\n---RESUMO---')
print(f'Seu genero é: {genero}')
print(f'Seu estado civil é: {estado_civil}')
print(f'anos de casada é: {casamento}')
