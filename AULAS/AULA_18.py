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
galera = [['josé', 20], ['henrique', 21], ['barbosa', 22], ['silva', 23]]

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
