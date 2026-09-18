import os
os.system('cls')

#entrada
mensal = float(input("Digite a sua renda mensal: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

#processamento e saida
valor_max_emprestimo = mensal * 10
valor_max_parcelas = mensal * 0.3
valor_prestacao= emprestimo / parcelas

if emprestimo > valor_max_emprestimo:
    print('Empréstimo não concedido')
elif parcelas > valor_max_parcelas:
    print("Empréstimo não concedido")
elif valor_prestacao > mensal * 0.3:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
    print(f"Valor da prestação: R${valor_prestacao:.2f}")
