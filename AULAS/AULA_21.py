# aula 21 - Funções (Parte 2)

# Antes de começar vamos aprender sobre o HELP no python

# voce pode abrir python no modo interativo, ou executar a função help()

# ou podemos executar o comando hel sem estar no modo interativo, passando a função ou método que queremos ver a DOCSTRINGS

#help(input)

#help(print)

#help(datetime)

# ou também podemos abri o doc do comando usando a função print() com os parâmetros .__doc__

print(input.__doc__)

# Podemos criar a nossa DOCSTRIGNS usanod """""" (aspas duplas três vezes) logo apos definir a função

def funcao():
    """
    essa é minha DOCSTRING
    """

help(funcao)

def contador(i, f, p):
    """
        faz uma contagem e mostra na tela
        :param i: inicio da contagem
        :param f: fim da contagem
        :param f: passo da contagem
        :return: sem retorno
        Função criada pelo henrique durante estudos
    """
    c = i
    while c <= f:
        print(c, end=" ")
        c += p
    print("FIM !")

help(contador)

contador(5, 30, 4)


# AGORA VAMOS FALAR SOBRE PARÊMETROS ESSPECIAIS

def somar(a , b=0, c=0):
    s = a + b  + c
    print(f"A soma vale {s}")

# deste modo temos uma função que não precisa ter todos os seus valores informados, somente os que n tem valor opcional, seriam os valores obrigatórios, e assim a função funciona normalmente mesmo que não seja informado todos os parâmetros

somar(7, 3)

# um conceito importante são o de variáveis globais e variáveis locais, isso se refere a variáveis utilizadas comente em certas funções(locais) e variáveis globais, as que são utilizadas em qualquer lugar do programa. sendo assim voce pode utilizar variáveis globais dentro de uma função, mas n pode utilizar variáveis de função no modo global. um detalhe, se vc reespecificar uma variável global dentro de uma função, você terá uma variável local, mesmo que tenham mesmo nome.

# retorno de função, agora voce pode retornar um valor de uma função, sem escrever na tela aquele valor.

def somarreturn(a , b=0, c=0):
    s = a + b  + c
    return s

print(somarreturn(7, 8))


def par(a=0):
    if a % 2 == 0:
        return True
    else:
        return False

print(par(5))

print(par(8))