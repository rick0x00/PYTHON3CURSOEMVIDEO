# Considerando os Conhecimentos da Aula 20
# DESAFIO 097 - Um print especial
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


N_desafio = "097"
nome_desafio = "Um print especial"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


def escreva(txt):
    print("-" * (len(txt) + 4))
    print(f"{txt:^{(len(txt) + 4)}}")
    print("-" * (len(txt) + 4))

escreva("teste de mensagem")

escreva("a função escreve e cria linhas adaptáveis")