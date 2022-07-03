# Considerando os Conhecimentos da Aula 16
# DESAFIO 072 - Número por Extenso 
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


from os import setegid, terminal_size


N_desafio = "072"
nome_desafio = "Número por Extenso "
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

numeros_extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')


while True :
    NUM = int(input("Indorme um Número inteiro entre 0 e 20: "))
    if NUM > 20 or NUM < 0:
        print('Numero Invalido')
    elif 0 <= NUM <= 20 :
        break
    else :
        print('ERROR 1')
print(f"Você digitou o numero {numeros_extenso[NUM]}")