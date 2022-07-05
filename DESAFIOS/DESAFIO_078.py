# Considerando os Conhecimentos da Aula 17

# DESAFIO 078 - Maior e Menor valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista = []

for count in range(0, 5):
    while True :
        lista.insert(count ,int(input(f"Digite um valor para a posição [{count}]: ")))
        if lista[count] > 0 :
            break
        else:
            print("Valor inválido!")

print(lista)
print(f"O maior valor foi {max(lista)}, e está na posição ", end = '')
for pos, c in enumerate(lista) :
    if max(lista) == c :
        print(f"{pos}", end=' ')
print(f"\nO menor valor foi {min(lista)}, e está na posição ", end = '')
for pos, c in enumerate(lista) :
    if min(lista) == c:
        print(f"{pos}", end=' ')
