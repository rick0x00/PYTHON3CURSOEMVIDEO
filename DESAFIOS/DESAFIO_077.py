# Considerando os Conhecimentos da Aula 16
# DESAFIO 077 - Contando vogais em Tupla
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


N_desafio = "077"
nome_desafio = "Contando vogais em Tupla"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras :
    print(f"\nNa palavra {p} temos: ", end = '')
    for letra in p:
        if letra in 'AEIOU' :
            print(letra, end=' ')