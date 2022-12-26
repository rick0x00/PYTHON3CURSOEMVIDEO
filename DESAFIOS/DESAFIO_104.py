# Considerando os Conhecimentos da Aula 21

# DESAFIO 104 - Validando entrada de dados em Python
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("104", "Validando entrada de dados em Python")

def leiaint(n=0):
    if n.isnumeric() == True:
        print(f"Você acabou de digitar o numero {n}")
        return 0
    else:
        print(cli_color_ForeGround['Red'],"ERRO! Digite um numero inteiro válido", cli_color_ForeGround['White'])
        return "ERROR"



leiaint("K")

