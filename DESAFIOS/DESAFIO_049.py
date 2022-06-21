# Considerando os Conhecimentos da Aula 13

# DESAFIO 049 - Tabuada v.2.0
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

N_desafio = "049"
nome_desafio = " Tabuada v.2.0 "
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


n = int(input("Informe um numero: "))

print("A Tabuada do {} é.".format(n))

print(f"||{'MULTIPLICAÇÃO':=^15}||")
for count in range (1 , 11, 1) :
    print(f'||{f"{n} x {count} = {n * count}":^15}||')


print(f"||{'DIVISÃO':=^15}||")
for count in range (1 , 11, 1) :
    print(f'||{f"{n} / {count} = {(n / count):.3f}":^15}||')


print(f"||{'ADIÇÃO':=^15}||")
for count in range (1 , 11, 1) :
    print(f'||{f"{n} + {count} = {n + count}":^15}||')


print(f"||{'SUBTRAÇÃO':=^15}||")
for count in range (1 , 11, 1) :
    print(f'||{f"{n} - {count} = {n - count}":^15}||')

