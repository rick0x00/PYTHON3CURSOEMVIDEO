# Considerando os Conhecimentos da Aula 16
# DESAFIO 073 - Tuplas com Times de Futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.


from turtle import pos


N_desafio = "073"
nome_desafio = "Tuplas com Times de Futebol"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


cbf20_1 = ('nulo', 'PALMEIRAS', 'ATHLETICO-pr', 'ATLETICO-MG', 'CORINTHIANS', 'INTERNACIONAL', 'FLUMINENSE', 'FLAMENGO', 'SANTOS', 'SÃO PAULO', 'BOTAFOGO', 'AVAÍ', 'BRAGANTINO', 'CEARÁ SC', 'ATLÉTICO-GO', 'GOIÁS', 'CUIABÁ', 'CORITIBA', 'AMERICA-MG', 'JUVENTUDE', 'FORTALEZA')

print('-=' * len(cbf20_1))
print(f"Listra de times do Brasileirão: {cbf20_1[1:]}")
print('-=' * len(cbf20_1))
print(f"Os 5 primeiros são{cbf20_1[1:6]}")
print('-=' * len(cbf20_1))
print(f"Os 4 últimos são {cbf20_1[-4:]}")
print('-=' * len(cbf20_1))
print(f"Times em ordem alfabética {sorted(cbf20_1)}")

if 'Chapecoense' in cbf20_1 :
    #for pos, cont in enumerate(cbf20_1) :
    #    if cont == "Chapecoense" :
    #        print(f"O 'Chapecoense' está na {pos}ª posição")
    print(f"O 'Chapecoense' está na {cbf20_1.index('Chapecoense')}ª posição")    
else:
    print('Chapecoense não está classificado')
