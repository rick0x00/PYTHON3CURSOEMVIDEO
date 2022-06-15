# Aula 11
# cores no terminal

#ANSI Escape Sequence
# \033[style;text;back m
# style: 0 none, 1 bold, 4 underline, 7 negative
# text: 30 preto, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 magenta, 36 ciano, 37 cinza, 97 branco
# back: 40 preto, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 magenta, 46 ciano, 47 cinza, 107 branco
print("\033[1;31;43m Olá,mundo \033[m")
# print(f'{"\033[7;31;43m"}Olá,mundo{"\033[m"}') ERROR 
print('{}Olá,mundo{}'.format('\033[7;31;43m','\033[m')) 

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'033[33m', 'pretoebranco':'033[7;30m'}

print(f"{cores['azul']}olá mundo{cores['limpa']}")
print("{}olá mundo{}".format(cores['azul'],cores['limpa']))

# RETORNE EM TODOS OS DESAFIOS E COLOQUE CORES NELES