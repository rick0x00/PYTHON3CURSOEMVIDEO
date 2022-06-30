# Considerando os Conhecimentos da Aula 15
# DESAFIO 071 - Simulador de Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


from calendar import c


N_desafio = "071"
nome_desafio = "Simulador de Caixa Eletrônico"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

print('-' * len(nome_desafio))
print(f"{'BANCO':^{len(nome_desafio)}}")
print('-' * len(nome_desafio))

cedulas50 = cedulas20 = cedulas10 = cedulas1 = int(0)

valor_solicitado_sacar = float(input("Que valor você que sacar? R$: "))

# while True :
if valor_solicitado_sacar // 50 >= 1 :
    cedulas50 = (valor_solicitado_sacar // 50)
if ((valor_solicitado_sacar - (50 * cedulas50)) // 20)  >= 1 :
    cedulas20 = ((valor_solicitado_sacar - 50 * cedulas50) // 20)
if ((valor_solicitado_sacar - (50 * cedulas50 + 20 * cedulas20)) // 10)  >= 1 :
    cedulas10 = ((valor_solicitado_sacar - (50 * cedulas50 + 20 * cedulas20)) // 10)
if ((valor_solicitado_sacar - (50 * cedulas50 + 20 * cedulas20 + 10 * cedulas10)) // 1) >= 1 :
    cedulas1 = ((valor_solicitado_sacar - (50 * cedulas50 + 20 * cedulas20 + 10 * cedulas10)) // 1)

if cedulas50 >= 1 :
    print(f"Total de {cedulas50:.0f} cedulas  de R$: 50 , totalizando R$: {cedulas50 * 50} ")

if cedulas20 >= 1 :
    print(f"Total de {cedulas20:.0f} cedulas  de R$: 20 , totalizando R$: {cedulas20 * 20}")

if cedulas10 >= 1 :
    print(f"Total de {cedulas10:.0f} cedulas  de R$: 10 , totalizando R$: {cedulas10 * 10}")

if cedulas1 >= 1 :
    print(f"Total de {cedulas1:.0f} cedulas  de R$: 1 , totalizando R$: {cedulas1 * 1}")

print("Volte sempre ao BANCO")