# considerando os conhecimentos da aula 23

# DESAFIO 115C - Finalizando o projeto
# Vamos finalizar o projeto de acesso a arquivos em Python.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("115C", "Arquivos com Python")

from lib.interface import *
from lib.arquivo import *
arq = "pessoas.txt"

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho("Opção 1")
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção invalida")
