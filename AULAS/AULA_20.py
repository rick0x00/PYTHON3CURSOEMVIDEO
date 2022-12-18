# AULA 20 
# FUNÇÕES - PARTE 1

# com funções podemos simplificar rotinas, processo que são executados frequentemente

# para criar uma função fazemos

def nome_funcao():
    print("Este print está dentro de uma função")

# para invocar a função fazemos

nome_funcao()
nome_funcao()

#####################

def mostralinha() :
    print("-" * 30)


mostralinha()

# agora iremos implementar parâmetros nas funções

def mensagem(msg):
    mostralinha()
    print(f"{msg}")
    mostralinha()


mensagem("Esta mensagem está funcionando dentro de uma função")


def soma(a, b):
    print(f"A = {a} e B ={b}")
    s = a + b
    print(f"A soma de A + B = {s}")


soma(5, 7)
soma(9, 25)
soma(a=9, b=25)
soma(b=9, a=25)
# acima especificamos os parâmetros de entrada, podemos inclusive mudar a sequencia dos parâmetros, mas um detalhe, ou especifica parâmetro de todos os valores ou não especifica de nenhum
# soma(a=9, 25) # essa invocação aqui não funciona


# Acima percebemos que o editor de texto está sublinhando certas coisas, iss está acontecendo por conta de eu não concentrar funções e o programa principal de forma organizada, função deve vir antes, o programa principal vem depois, e também muito importante, SEPARAR as funções 


# agora vamos estudar sobre EMPACOTAMENTO

def contador(*num):
    print(f"{num}")
    s = 0
    for v in num:
        print(f"{v}")
        s += v
    print(f"A soma de Todos os Valores é {s}")

contador(1, 2, 4, 7, 9)

contador(8, 5, 7, 7, 9)

# Podemos perceber que foram criadas tuplas durante o empacotamento, e assim podenmos fazer tudo que aprendemos com tuplas


# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 096, 097, 098, 099, 100"

# Considerando os Conhecimentos da Aula 20


# DESAFIO 096 - Função que calcula área
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# DESAFIO 097 - Um print especial
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# DESAFIO 098 - Função de Contador
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

# DESAFIO 099 - Função que descobre o maior
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# DESAFIO 100 - Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
