# Considerando os Conhecimentos da Aula 12
# DESAFIO 036 - Aprovando Empréstimo 
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

N_desafio = "036"
nome_desafio = "Aprovando Empréstimo"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


valor_casa = float(input("{}Informe o Valor da Casa: R${} ".format('\033[m','\033[36m')))
salario_comprador = float(input("{}Informe o Salário do Comprador: R${} ".format('\033[m','\033[36m')))
anos_pagamento = int(input("{}Informe o Tempo de pagamento em anos:{} ".format('\033[m','\033[36m')))
print("{}".format('\033[m'))

print(f"Para pagar a cada de R$:{valor_casa:.2f} em {anos_pagamento} anos a prestação será de R$:{valor_casa/anos_pagamento/12:.2f}")
if valor_casa/(anos_pagamento*12) > salario_comprador*0.3 :
    print("Empréstimo {}NEGADO{}!".format('\033[31;1m','\033[m'))
else :
    print("Empréstimo {}APROVADO{}!".format('\033[32;1m','\033[m'))
