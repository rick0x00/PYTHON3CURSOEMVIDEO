# Considerando os Conhecimentos da Aula 12
# DESAFIO 041 - Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SENIOR
# -Acima: MASTER

N_desafio = "041"
nome_desafio = "Classificando Atletas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

ano_nascimento = int(input("Informe o ano de nascimento: "))

from datetime import date

print(f"O atleta tem {(date.today().year - ano_nascimento)} anos.")
print("classificação: ", end='')
if (date.today().year - ano_nascimento) <= 9:
    print("MIRIM")
elif (date.today().year - ano_nascimento) > 9 and (date.today().year - ano_nascimento) <= 14 : 
    print("INFANTIL")
elif (date.today().year - ano_nascimento) > 14 and (date.today().year - ano_nascimento) <= 19 : 
    print("JUNIOR")
elif (date.today().year - ano_nascimento) > 19 and (date.today().year - ano_nascimento) <= 20 : 
    print("SENIOR")
elif (date.today().year - ano_nascimento) > 20 : 
    print("MASTER")
