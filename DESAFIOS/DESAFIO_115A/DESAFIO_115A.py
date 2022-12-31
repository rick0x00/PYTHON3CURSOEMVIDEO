# considerando os conhecimentos da aula 23

# DESAFIO 115A - Criando um menu em Python
# Vamos criar um menu em Python, usando modularização.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("115A", " Criando um menu em Python")

from lib.interface import *


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho("Opção 1")
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção invalida")
