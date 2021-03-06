# Manipulação de Texto

separador = str("###############################################################")
frase = str("Curso em Video Python")

# Observe que cada caractere possui um índice
# C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

###############################################################
# Fatiamento de strings
print(separador)
print("Fatiamento de strings")
print(separador)

print(f"O caracteres de índice 9 da frase '{frase}' é '{frase[9]}'")
print(f"Os caracteres de índice 9 até 13 da frase '{frase}' são '{frase[9:13+1]}'")
# é 13 + 1(pode ser 14) pois é ATÉ, ou seja, não inclui o índice referido

# outro exemplo
print(f"Os caracteres de índice 9 até 20 da frase '{frase}' são '{frase[9:20+1]}'")

# saltando indices
print(f"Os caracteres de índice 9 até 20, pulando de 2 em 2, da frase '{frase}' são '{frase[9:21:2]}'")

# omissão de referência de índice 
print(f"Os caracteres até o índice 14, da frase '{frase}' são '{frase[:14]}'")
print(f"Os caracteres iniciando no índice 9, da frase '{frase}' são '{frase[9:]}'")

# compostos
print(frase[:14:3])

# ###############################################################
# Análise de Strings
print(separador)
print("Análise de Strings")
print(separador)

# comprimento da string da variável
print(f"A Frase '{frase}' possui '{len(frase)}' caracteres(20 indices, pois contamos o '0')")

# contagem de valor dentro de variável
print(f"A Frase '{frase}' possui '{frase.count('o')}' caracteres 'o'")

# contagem de valor dentro de variável + fatiamento
print(f"A Frase '{frase}' possui '{frase.count('o',0,13)}' caracteres 'o', até o índice 13")

# Pesquisa de Valor dentro de variável
print(f"A sequência 'deo' inicia no índice '{frase.find('deo')}' na frase '{frase}'")
print(f"A sequência 'o' inicia no índice '{frase.find('o')}' na frase '{frase}'")
print(f"A sequência 'O' inicia no índice '{frase.find('O')}' na frase '{frase}'")
print(f"A sequência 'Android' inicia no índice '{frase.find('Android')}' na frase '{frase}'")

# Confirmação de Existência dentro de variável
print(f"A sequência 'Curso' existe na frase '{frase}'? '{'Curso' in frase}'")
print(f"A sequência 'Android' existe na frase '{frase}'? '{'Android' in frase}'")

# ###############################################################
# Transformação de String
print(separador)
print("Transformação de String")
print(separador)

# Substituição pontual de sequencia
print(f"substituindo pontualmente a palavra 'Python' por 'Android' da frase '{frase}', resultando em '{frase.replace('Python','Android')}'")

print(f"A sequência 'Android' inicia no índice '{frase.replace('Python','Android').find('Android')}' na frase '{frase.replace('Python','Android')}'")
print(f"A sequência 'Android' existe na frase '{frase.replace('Python','Android')}'? '{'Android' in frase.replace('Python','Android')}'")
print(f"A Frase '{frase.replace('Python','Android')}' possui '{len(frase.replace('Python','Android'))}' caracteres(21 indices, pois contamos o '0', e foi adicionado 1 índice automaticamente)")

print(f"A sequência 'Android' inicia no índice '{frase.replace('python','Android').find('Android')}' na frase '{frase.replace('python','Android')}'")
print(f"A sequência 'Android' existe na frase '{frase.replace('python','Android')}'? '{'Android' in frase.replace('python','Android')}'")
print(f"A Frase '{frase.replace('python','Android')}' possui '{len(frase.replace('python','Android'))}' caracteres(20 indices, pois contamos o '0', e A frase não foi encontrada para poder ser susbtituída)")

# Transformação completa
print(f"Tornando pontualmente toda a String '{frase}' em Maiúscula '{frase.upper()}'")
print(f"Tornando pontualmente toda a String '{frase}' em Minuscula '{frase.lower()}'")
print(f"Tornando pontualmente toda a String '{frase}' em Capitalizado '{frase.capitalize()}'")
print(f"Tornando pontualmente toda a String '{frase}' em Titulo '{frase.title()}'")
fraseruim = str("   Aprenda Python  ")
print(f"Tornando pontualmente toda a String '{fraseruim}' sem espaços desnecessários '{fraseruim.strip()}'")
print(f"Tornando pontualmente toda a String '{fraseruim}' sem espaços desnecessários no lado direito '{fraseruim.rstrip()}'")
print(f"Tornando pontualmente toda a String '{fraseruim}' sem espaços desnecessários no lado Esquerdo '{fraseruim.lstrip()}'")

# divisão
print(f"A frase '{frase}' pode ser ''esplitada'' {frase.split()}")
print(f"A frase '{frase}' tem primeira palavra '{frase.split()[0]}'")
# Usando [] eu determino o índice que quero usar da array criada

# junção
print(f"A frase '{frase}' pode ser ''juntada'' {''.join(frase.split())}")


# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 022, 023, 024, 025, 026, 027"

# DESAFIO 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar Espaços).
# Quantas letras tem o primeiro nome.

# DESAFIO 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# DESAFIO 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# DESAFIO 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# DESAFIO 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira.
# Em que posição ela aparece a última vez.

# DESAFIO 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro a o último nome separadamente.
# Ex: Ana Maria de Souza 
# primeiro = Ana 
# último=Souza