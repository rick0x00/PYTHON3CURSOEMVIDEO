# Trabalhando com Módulos

# módulos são bibliotecas que podem ser incluídas no algoritmo

# a biblioteca "math" inclui as funções: ceil, floor, trunc, pow, sqrt, factorial ...

# é possível importar a biblioteca inteira

import math

# é possível importar uma única função da biblioteca

from math import sqrt

# ou podemos importar mais de uma função

from math import sqrt, trunc

num = int(input("Digite um Numero: "))

raiz = math.sqrt(num)

print(f"A raiz de {num} é igual a {(raiz):.2f}")


# "PASSÍVEL DE RESOLUÇÃO DOS DESAFIOS: 016, 017, 018, 019, 020, 021"
