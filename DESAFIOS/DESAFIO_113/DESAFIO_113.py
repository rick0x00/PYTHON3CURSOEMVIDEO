# considerando os conhecimentos da aula 23

# DESAFIO 113 - Funções aprofundadas em Python
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("103", "Funções aprofundadas em Python")

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(cli_color_ForeGround['Red'],"ERRO! Digite um numero inteiro válido", cli_color_ForeGround['White'])
            continue
        except Exception as error:
            print(f"Ocorreu um problema <{error}>")
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(cli_color_ForeGround['Red'],"ERRO! Digite um numero real válido", cli_color_ForeGround['White'])
            continue
        except Exception as error:
            print(f"Ocorreu um problema <{error}>")
            continue
        else:
            return n


numint = leiaint("digite um valor inteiro ")
numfloat = leiafloat("digite um valor real ")
print(f"o valor INTEIRO digitado foi {numint} e o valor REAL digitado foi {numfloat}")
