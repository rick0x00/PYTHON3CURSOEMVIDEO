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
print(valores.sort(reverse=True))