# AULA 19
# DICIONÁRIOS

# com dicionários nos evoluímos os indices das listas, agora teremos indices LITERAIS, não mais numéricos

# DECLARAÇÕES

tupla = ()

lista = []
lista = list()

dicionario = {}
dicionario = dict()

# exemplos de uso

dicionario = { 'nome':'Henrique', 'idade':'21' }
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario)

# adicioando novos indices
dicionario['sexo'] = 'M'
print(dicionario)

# removendo indices
del dicionario['idade']
print(dicionario)

# um pouco mais sobre dicionários
# dicionários são constituídos de items, os items possuem keys e values

print (dicionario.values())
print (dicionario.keys())
print (dicionario.items())


for k,v in dicionario.items():
    print (f"a key {k} tem valor {v}")

# para finalizar vale lembrar que também podemos ter dicionários dentro de listas, assim começamos a criar estruturas de dados

# vamos para um exemplo um pouco elaborado para entender um problema comum envolvendo dicionários e listas

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    #brasil.append(estado()) # assim já sabemos que não funcionaria, OK ?
    #brasil.append(estado[:]) # Agora sim deveria funcionar, mas infelizmente não funciona, essa relação de dicionário com lista não funciona!
    brasil.append(estado.copy()) # agora sim, utilizando o método copy tudo deve funcionar!

for e in brasil :
    for k, v in e.items():
        print (f"a key {k} tem valor {v}")

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 090, 091, 092, 093, 094, 095"

# Considerando os Conhecimentos da Aula 19

# DESAFIO 090 - Dicionário em Python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# DESAFIO 091 - Jogo de Dados em Python 
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# DESAFIO 092 - Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# DESAFIO 093 - Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# DESAFIO 094 - Unindo dicionários e listas
# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# DESAFIO 095 - Aprimorando os Dicionários
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.