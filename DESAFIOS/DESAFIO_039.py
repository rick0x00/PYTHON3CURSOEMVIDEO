# Considerando os Conhecimentos da Aula 12
# DESAFIO 039 - Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço Militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

N_desafio = "039"
nome_desafio = "Alistamento Militar"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

ano_nascimento = int(input("{}Informe o Ano de Nascimento:{} ".format('\033[m','\033[32m')))
print('{}'.format('\033[m'))

from datetime import date

if (date.today().year - ano_nascimento) == 18 :
    print(f"Quem nasceu em {ano_nascimento} tem {date.today().year - ano_nascimento} anos em {date.today().year}")
    print("É seu Ano de alistamento")
elif (date.today().year - ano_nascimento) > 18 :
    print(f"Quem nasceu em {ano_nascimento} tem {date.today().year - ano_nascimento} anos em {date.today().year}")
    print(f"Você já deveria ter se alistado há {(date.today().year - ano_nascimento) - 18} anos")
    print(f"O ano do seu alistamento foi em {ano_nascimento + 18}")
elif (date.today().year - ano_nascimento) < 18 :
    print(f"Quem nasceu em {ano_nascimento} tem {date.today().year - ano_nascimento} anos em {date.today().year}")
    print(f"Ainda faltam {(ano_nascimento + 18) - (date.today().year)} anos para o Alistamento")
    print(f"O ano do seu alistamento será em {ano_nascimento + 18}")