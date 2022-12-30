# considerando os conhecimentos da aula 22

# DESAFIO 111 - Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("111", "Transformando módulos em pacotes")


from utilidadescev import moeda

num = float(input("Digite o Preço: R$ "))

moeda.resumo(num, 20, 12)