
cli_color_ForeGround = { 'Black':'\033[30m', 'Red':'\033[31m', 'Green':'\033[32m', 'Yellow':'\033[33m', 'Blue':'\033[34m', 'Magenta':'\033[35m', 'Cyan':'\033[36m', 'White':'\033[37m', 'Bright_White':'\033[97m'}

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(cli_color_ForeGround['Red'],"ERRO! Digite um numero inteiro válido", cli_color_ForeGround['White'])
            continue
        except Exception as error:
            print(f"Ocorreu um problema <{error}>")
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaint("Sua Opção: ")
    return opc