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