# Considerando os Conhecimentos da Aula 21

# DESAFIO 102 - Função para Fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.



def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("102","Função para Fatorial")

def fatorial(num, show=True):
    """
    Faz calculo de fatorial
    :param num: numero para calculo fatorial.
    :param show: (Opcional, True or False), mostra processo de calculo de fatorial.
    :return: O valor da fatorial de um numero num.
    """
    s = 1
    if show == True:
        for c in range(num, 0 , -1):
            print (c, end=" ")
            if c != 1:
                print("x ", end="")
            s *= c
        print("= ", end="")
    elif show == False:
        for c in range(num, 0 , -1):
            s *= c
    else:
        print(f"Erro {show} is unrecorded")
    print(s)



# main
fatorial(4, False)

help(fatorial)