# Considerando os Conhecimentos da Aula 12
# DESAFIO 042 - Analisando Triângulos v2.0
# Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

cli_style = {'Normal':'\033[0m', 'Bold':'\033[1m', 'Faint':'\033[2m', 'Italic':'\033[3m','Underline':'\033[4m', 'Slow_Blink':'\033[5m', 'Rapid_Blink':'\033[6m', 'Invert':'\033[7m', 'Hide':'\033[8m', 'Strike':'\033[9m'}

cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}

cli_color_BackGround = { 'Black':'\033[40m', 'Red':'\033[41m', 'Green':'\033[42m', 'Yellow':'\033[43m', 'Blue':'\033[44m', 'Magenta':'\033[45m', 'Cyan':'\033[46m', 'White':'\033[47m', 'Bright_White':'\033[107m'}

N_desafio = "042"
nome_desafio = "Analisando Triângulo v2.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str("Analisador de Triângulos")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))


a = float(input(f"{cli_color_ForeGround['Bright_White']}Primeiro Segmento:{cli_color_ForeGround['Cyan']} "))
b = float(input(f"{cli_color_ForeGround['Bright_White']}Segundo Segmento:{cli_color_ForeGround['Cyan']} "))
c = float(input(f"{cli_color_ForeGround['Bright_White']}Terceiro Segmento:{cli_color_ForeGround['Cyan']} "))

if a < b + c and b < a + c and c < a + b :
    print(f"{cli_color_ForeGround['Bright_White']}Os segmentos Acima {cli_color_ForeGround['Green']}{cli_style['Underline']}PODEM{cli_color_ForeGround['Bright_White']}{cli_style['Normal']} formar um triângulo")
    if a != b != c != a :
        print(f"Todos os lados são são diferentes!")
        print(f"Temos um triangulo {cli_color_ForeGround['Black']}{cli_color_BackGround['Cyan']}ESCALENO{cli_color_ForeGround['Bright_White']}{cli_color_BackGround['Black']}")
    elif a == b == c :
        print(f"Todos os lados iguais!")
        print(f"Temos um triangulo {cli_color_ForeGround['Black']}{cli_color_BackGround['Cyan']}EQUILÁTERO{cli_color_ForeGround['Bright_White']}{cli_color_BackGround['Black']}")
    else :
        print(f"Dois lados iguais!")
        print(f"Temos um triangulo {cli_color_ForeGround['Black']}{cli_color_BackGround['Cyan']}ISÓSCELES{cli_color_ForeGround['Bright_White']}{cli_color_BackGround['Black']}")
else :
    print(f"{cli_color_ForeGround['Bright_White']}Os segmentos Acima {cli_color_ForeGround['Red']}{cli_style['Underline']}NÃO PODEM{cli_color_ForeGround['Bright_White']}{cli_style['Normal']} formar um triângulo")