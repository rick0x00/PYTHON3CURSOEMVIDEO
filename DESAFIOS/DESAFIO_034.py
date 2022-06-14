# desafio 034 
# Escreva um programa que pergunte o salário de um Funcionário e calcule o valor do seu aumento.
# Para salários superiores a RS1.250.00.calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

from calendar import SATURDAY


N_desafio = "034"
nome_desafio = "Aumentos múltiplos"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

salario_atual = float(input("Salário atual: "))

if salario_atual > 1250 :
    print(f"Quem ganhava R${salario_atual:.2f} passa a ganhar R${salario_atual * 1.1:.2f}")
else :
     print(f"Quem ganhava R${salario_atual:.2f} passa a ganhar R${salario_atual * 1.15:.2f}")