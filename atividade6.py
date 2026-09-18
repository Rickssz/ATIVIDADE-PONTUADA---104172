import os
os.system('cls')

#Entrada de dados
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

# saida
if media >= 6:
    print('Parabens aluno aprovado.')
    print(f'Sua media foi: {media:.1f}')
elif media >= 4.1 and 5.9:
    print('Aluno esta de recuperação.')
    print(f'Sua media foi: {media:.1f}')
else:
    print('aluno reprovado.')
    print(f'Sua media foi: {media:.1f}')
