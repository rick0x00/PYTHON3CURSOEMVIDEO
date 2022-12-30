
def leiadinheiro(info):
    loopon = True
    while loopon:    
        content = str(input(info).replace(",", "."))

        if content.isalpha() == True or content.strip() == '' :
            print(f"ERRO, "{content}" é um VALOR invalido!")    
        else:
            loopon = False
            return float(content)