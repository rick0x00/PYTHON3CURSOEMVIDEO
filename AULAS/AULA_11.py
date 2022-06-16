# Aula 11
# cores no terminal

#ANSI Escape Sequence
# \033[style;text;back m
# style: 0 none, 1 bold, 4 underline, 7 negative
# text: 30 preto, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 magenta, 36 ciano, 37 cinza, 97 branco
# back: 40 preto, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 magenta, 46 ciano, 47 cinza, 107 branco
from turtle import delay


print("\033[1;31;43m Olá,mundo \033[m")
# print(f'{"\033[7;31;43m"}Olá,mundo{"\033[m"}') ERROR 
print('{}Olá,mundo{}'.format('\033[7;43;31m','\033[m')) 

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'033[33m', 'pretoebranco':'033[7;30m'}

print(f"{cores['azul']}olá mundo{cores['limpa']}")
print("{}olá mundo{}".format(cores['azul'],cores['limpa']))

# RETORNE EM TODOS OS DESAFIOS E COLOQUE CORES NELES

# criando um dicionário de cores
# fonte: https://en.wikipedia.org/wiki/ANSI_escape_code
# fonte: https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python

cli_style = {'Normal':'\033[0m', 'Bold':'\033[1m', 'Faint':'\033[2m', 'Italic':'\033[3m','Underline':'\033[4m', 'Slow_Blink':'\033[5m', 'Rapid_Blink':'\033[6m', 'Invert':'\033[7m', 'Hide':'\033[8m', 'Strike':'\033[9m'}

cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}

cli_color_BackGround = { 'Black':'\033[40m', 'Red':'\033[41m', 'Green':'\033[42m', 'Yellow':'\033[43m', 'Blue':'\033[44m', 'Magenta':'\033[45m', 'Cyan':'\033[46m', 'White':'\033[47m', 'Bright_White':'\033[107m'}

print(f"{cli_color_BackGround['Bright_White']}{cli_style['Italic']}olá mundo{cli_color_BackGround['Black']}")

