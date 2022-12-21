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


# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 101, 102, 103, 104, 105, 106"

# Considerando os Conhecimentos da Aula 21


# DESAFIO 101 - Funções para votação
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# DESAFIO 102 - Função para Fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# DESAFIO 103 -  Ficha do Jogador
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# DESAFIO 104 - Validando entrada de dados em Python
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

# DESAFIO 105 - Analisando e gerando Dicionários
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

# DESAFIO 106 -  Sistema interativo de ajuda em Python
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.