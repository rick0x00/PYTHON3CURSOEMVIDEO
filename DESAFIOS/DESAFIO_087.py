# Considerando os Conhecimentos da Aula 18
# DESAFIO 087 - Mais sobre Matriz em Python
# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


N_desafio = "087"
nome_desafio = "Mais sobre Matriz em Python"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = 0
somac3 = 0
maior2c = 0

for l in range(0, 3) :
    for c in range(0, 3) :
        matriz[l][c]  = int(input(f"Informe o valor [{l},{c}] : "))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0 :
            somapar += matriz[l][c]
        if c == 2 :
            somac3 += matriz[l][c]
        if l == 1 :
            if c == 0 :
                maior2c = matriz[l][c]
            else :
                if matriz[l][c] > maior2c :
                    maior2c = matriz[l][c]
    print("")
print('-=' * 30)
print (f"A soma dos valores Pares é {somapar}")
print (f"A soma dos valores da terceira coluna {somac3}")
print (f"O maior numero da segunda coluna é {maior2c}")
print('-=' * 30)
