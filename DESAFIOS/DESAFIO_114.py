# considerando os conhecimentos da aula 23

# DESAFIO 114 - Site está acessível?
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("114", "Site está acessível?")

import urllib
import urllib.request



try: 
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print("O site está inacessível")
else:
    print("Tudo OK")
