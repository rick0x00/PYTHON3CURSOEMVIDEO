# AULA 17
# VARIÁVEIS COMPOSTAS - LISTAS - PARTE 1 

# TUPLAS SÃO DEFINIDAS USANDO parenteses, AS LISTAS SÃO DEFINIDAS COM COLCHETES

# AS LISTAS SÃO MUTÁVEIS.

lanche = ['sanduíche', 'suco', 'pizza', 'pudim']
lanche[3] = 'picole'

print(lanche)

### adicionando novos elementos na lista
# adiciona elementos no final da lista
lanche.append('cookie')

print(lanche)

# adicionando elementos em uma posição especifica

lanche.insert(1,'coxinha')

print(lanche)

### apagando elementos
# apagando elemento em posição especifica
del lanche[3]
print(lanche)

# apagando elemento do final da lista, utilizamos o método pop
lanche.pop()
print(lanche)
# utilizando o método pop também podemos apagar um elemento especifico
lanche.pop(2)
print(lanche)

# também podemos apagar referenciando o valor do conteúdo e nao somente o índice do elemento
lanche.remove('coxinha')
print(lanche)

### CRIANDO LISTA COM NUMEROS

lista_numeros = list(range(4, 11))

print(lista_numeros)

### lista numérica manual

valores = [4, 8, 2, 5, 6]

# ordenando valores
print(sorted(valores))
# ordem reversa
valores.sort(reverse=True)
print(valores)

# o ato de copiar uma lista cria links entre elas
a = [2, 4, 8, 7]
b = a
b[2] = 5
print(f"Lista A: {a}")
print(f"Lista B: {b}")

# assim você consegue de fato copiar os valores sem criar links entre elas
c = [9, 3, 6, 1]
d = c[:]
d[2] = 5
print(f"Lista A: {c}")
print(f"Lista B: {d}")

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS:"

# Considerando os Conhecimentos da Aula 17

# DESAFIO 078 - Maior e Menor valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

# DESAFIO 079 - Valores únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

# DESAFIO 080 - Lista ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

# DESAFIO 081 - Extraindo dados de uma Lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# DESAFIO 082 - Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# DESAFIO 083 - Validando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.



