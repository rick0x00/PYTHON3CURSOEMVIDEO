# Considerando os Conhecimentos da Aula 21

# DESAFIO 103 -  Ficha do Jogador
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))


presentation("103", "Ficha do Jogador")

def ficha(nome="unnamed", gols="undefined"):
    print(f"O jogador {nome} fez {gols} gols")


ficha((input("Nome do Jogador: ")),(input("Numero de Gols: ")))
