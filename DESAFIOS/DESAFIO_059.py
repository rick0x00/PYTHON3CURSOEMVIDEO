# Considerando os Conhecimentos da Aula 14
# DESAFIO 059 - Criando um Menu de Opções
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

N_desafio = "059"
nome_desafio = "Criando um Menu de Opções"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

loopon = 1

while loopon == 1 :
    loopon = 0
    n1 = float(input("Informe o primeiro valor: "))
    n2 = float(input("Informe o Segmento valor: "))

    print(""" Qual Operação deseja Executar
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    """)
    opc = int(input("Informe a Opção Desejada: "))

    if opc == 1 :
        print("opção: SOMA")
        print(f"A SOMA entre {n1} e {n2} é {n1 + n2}")
        exit();
    elif opc == 2 :
        print("opção: MULTIPLICAÇÃO")
        print(f"A MULTIPLICAÇÃO entre {n1} e {n2} é {n1 * n2}")
        exit();
    elif opc == 3 :
        print("opção: MAIOR")
        if n1 > n2 :
            maior = n1
        if n2 > n1 :
            maior = n2
        if n1 == n2 :
            print ("OS NÚMEROS SÃO IGUAIS")
        else: print(f"O MAIOR NUMERO entre {n1} e {n2} é {maior}")
        exit();
    elif opc == 4 :
        print("opção: NOVOS NÚMEROS")
        loopon = 1
    elif opc == 5 :
        print("opção: SAIR DO PROGRAMA")
        exit();
    else :
        print("opção invalida")
        loopon = 1

