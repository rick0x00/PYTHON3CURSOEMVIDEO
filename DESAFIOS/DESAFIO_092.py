# DESAFIO 092 - Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

N_desafio = "092"
nome_desafio = "Cadastro de Trabalhador em Python"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

from datetime import datetime

print (f"{('-+' * 10):=^30}")

nome = str(input("Nome: "))
anonascimento = int(input("Ano de nascimento: "))
ctps = int(input("Carteira de trabalho: "))
if ctps > 0 :
    anocontratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: "))
    dados = {"nome": nome, "Idade": ((datetime.now().year)-anonascimento), "ctps": ctps, "Contratação": anocontratacao, "salario": salario}
    dados['Aposentadoria'] = ((anocontratacao + 35 ) - (anonascimento))
else :
    dados = {"nome": nome, "Idade": ((datetime.now().year)-anonascimento), "ctps": ctps}

print (f"{('#' * 20):-^30}")
print(dados.items())

for k, v in dados.items():
    print(f" - {k} tem o valor {v}")