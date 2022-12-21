# Considerando os Conhecimentos da Aula 21

# DESAFIO 101 - Funções para votação
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


from datetime import datetime


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("101","Funções para votação")



def voto(idade):
    if idade < 16:
        return "NEGADO"
    elif idade < 18 or idade >= 70:
        return "OPCIONAL"
    elif idade >= 18 or idade < 70:
        return "OBRIGATÓRIO"

print("-" * 30)
anonascimento = int(input("Em que Ano voce nasceu?"))

print (f" Com {datetime.now().year - anonascimento} Anos: ", end="")
if voto(datetime.now().year - anonascimento) == "NEGADO":
    print(" NÃO VOTA")
if voto(datetime.now().year - anonascimento) == "OPCIONAL":
    print(" VOTO OPCIONAL")
if voto(datetime.now().year - anonascimento) == "OBRIGATÓRIO" :
    print(" VOTO OBRIGATÓRIO")