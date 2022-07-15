# AULA 18
# VARIÁVEIS COMPOSTAS - LISTAS - PARTE 2

# LISTAS COMPOSTAS, LISTAS DENTRO DE LISTAS

# voce pode cira uma variável definindo sua classe ou com colchetes fechados vazios
dados = list()
dados.append("Henrique")
dados.append("21")

print(dados[0])
print(dados[1])

pessoas = list()

# colocando listas dentro de outras listas
pessoas.append(dados[:])
# abaixo percebe que existe diferença em uma temos uma lista dentro de uma lista e na outra temos uma variável simples dentro de uma lista
pessoas.append(['teste11'])
pessoas.append('teste12')
# adicionando uma lista dentro de outra lista de forma mais manual
pessoas.append(["teste21","teste22"]) 

# observe os retornos
print(pessoas)
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])

# com dois indices podemos extrair informações especificas de um índice dentro de outro índice
print(pessoas[0][0])
print(pessoas[0][1])

# outra forma de criar listas compostas
galera = [['pedro', 20], ['henrique', 21], ['maria', 22], ['carlos', 23]]

print(galera)
print(galera[2])
print(galera[2][1])
print(galera[3][0])

for p in galera :
    print(f"{p[0]} tem {p[1]} anos de idade")

################

dado = list()
info = list()

for c in range(0, 3) :
    dado.append(str(input("Informe seu nome: ")))
    dado.append(int(input("Informe sua idade: ")))
    info.append(dado[:])
    dado.clear()

totmai = totmen = int()

for c in info :
    if c[1] >= 21 :
        print(f"{c[0]} é maior de idade")
        totmai += 1
    else :
        print(f"{c[0]} é menor de idade")
        totmen += 1

print(f"temos {totmai} maiores de idade, e temos {totmen} menores de idade")
print(info)

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 084, 085, 086, 087, 088, 089"

# Considerando os Conhecimentos da Aula 18

# DESAFIO 084 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# DESAFIO 085 - Listas com pares e ímpares
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


# DESAFIO 086 - Matriz em Python
#  Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# DESAFIO 087 - Mais sobre Matriz em Python
# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# DESAFIO 088 - Palpites para a Mega Sena
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# DESAFIO 089 - Boletim com listas compostas
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

