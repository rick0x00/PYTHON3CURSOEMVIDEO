# AULA 13
# LAÇOS DE REPETIÇÃO - Estrutura de repetição for

start = int(input("Informe o inicio: "))
fim = int(input("Informe um fim: "))
passo = int(input("Informe o passo: "))
MSG = str(input("Informe a mensagem: "))

for c in range(start , fim+1, passo):
    print(MSG)
print("FIM")
### 
#for c in range(0, 5) :
#    print("hello world")
#    print(c)

#for c in range(6, 1, -1) :
#    print("hello world")
#    print(c)

#for c in range(0, 10, 2) :
#    print("hello world")
#    print(c)
###

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056"


# Considerando os Conhecimentos da Aula 13

# DESAFIO 046 - Contagem regressiva
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0. com uma pausa de 1 segundo entre eles.

# DESAFIO 047 - Contagem de pares
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# DESAFIO 048 - Soma ímpares múltiplos de três
# Faça um programa que calcule a soma entre todos os números impares que SÃO múltiplos de três e que se encontram no intervalo de 1 até 500.

# DESAFIO 049 - Tabuada v.2.0
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# DESAFIO 050 - Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidera-o.

# DESAFIO 051 - Progressão Aritmética
# Desenvolva um programa que leia o primeiro termo & a razão de uma PA. No final, mostre os 10 primeiros termos dassa progressão.

# DESAFIO 052 - Números primos
# Faça um programa que leia um número inteiro a diga se ele é ou não um número primo.

# DESAFIO 053 -
# Crie um programa que leia uma frase qualquer a diga se ela é um palíndromo, desconsiderando os aspaços.

# DESAFIO 054 -
# Crie um programa que leia o ano da nascimento de sete pessoas. No final, mostra quantas pessoas ainda não atingiram a maioridade < quantas já sÃO maiores.

# DESAFIO 055 -
# Faça um programa que leia o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lidos.

# DESAFIO 056 -
# Desenvolva um programa que leia o noma, idade e sexo de 4 pessoas. No final do programa, mostre: 
# - A média da idade do grupo.
# - Qual é o nome do homem mais velho. 
# - Quantas mulheres tem menos de 20 anos.