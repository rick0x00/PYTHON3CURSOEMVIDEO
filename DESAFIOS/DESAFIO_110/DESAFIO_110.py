# considerando os conhecimentos da aula 22
# DESAFIO 110 - Reduzindo ainda mais seu programa
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("110", "Reduzindo ainda mais seu programa")


import moeda

num = float(input("Digite o Preço: R$ "))

moeda.resumo(num, 20, 12)