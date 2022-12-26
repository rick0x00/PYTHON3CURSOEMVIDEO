# Considerando os Conhecimentos da Aula 21

# DESAFIO 105 - Analisando e gerando Dicionários
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("105", "Analisando e gerando Dicionários")

def notas(*num, sit=False):
    """
    Função para analisar nota de vários alunos
    :param num: uma ou mais notas de alunos
    :param sit: Indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    turma = dict()
    maior = 0
    total = 0
    menor = 0 
    media = 0
    soma = 0
    for c in num:
        total += 1
        soma += c
        if c == 1:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    media = soma / total
    turma = {'total': total, 'soma': soma, 'menor': menor, 'media': media}
    if sit == True:
        if media < 6:
            turma['situação'] = "RUIM"
        elif media >= 6  and media < 7 :
            turma['situação'] = "RAZOÁVEL"
        elif media >= 7 :
            turma['situação'] = "BOA"
    elif sit != False :
        print("Error! Situação inválida")
        return "ERROR!"
    return turma


print(notas(5, 6, 7, 7.3, 9, sit=True))

help(notas)