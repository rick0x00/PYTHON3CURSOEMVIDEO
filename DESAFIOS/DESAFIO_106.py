# Considerando os Conhecimentos da Aula 21

# DESAFIO 106 -  Sistema interativo de ajuda em Python
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep

cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}

cli_color_BackGround = { 'Black':'\033[40m', 'Red':'\033[41m', 'Green':'\033[42m', 'Yellow':'\033[43m', 'Blue':'\033[44m', 'Magenta':'\033[45m', 'Cyan':'\033[46m', 'White':'\033[47m', 'Bright_White':'\033[107m'}


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("106", "Sistema interativo de ajuda em Python")


def msg(mensagem):
    print("~" * (len(mensagem) + 4) )
    print(f"{(mensagem):^{(len(mensagem) + 4)}}")
    print("~" * (len(mensagem) + 4) )


while True:
    search = str(input("função ou biblioteca > "))
    if search == "fim":
        print(cli_color_BackGround['Red'], cli_color_ForeGround['White'])
        msg("até logo")
        print(cli_color_BackGround['Black'], cli_color_ForeGround['White'])
        break
    else:
        print(cli_color_BackGround['Blue'], cli_color_ForeGround['White'])
        msg(f"Acessado manual do comando {search}")
        print(cli_color_BackGround['Black'], cli_color_ForeGround['White'])
        sleep(1)
        print(cli_color_BackGround['White'], cli_color_ForeGround['Black'])
        help(search)
        print(cli_color_BackGround['Black'], cli_color_ForeGround['White'])
