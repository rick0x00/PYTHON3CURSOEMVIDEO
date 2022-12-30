# considerando os conhecimentos da aula 22

# DESAFIO 112 - Entrada de dados monetários
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("112", "Entrada de dados monetários")


from utilidadescev import moeda
from utilidadescev import dados


num = dados.leiadinheiro("Digite o Preço: R$ ")

moeda.resumo(num, 20, 12)