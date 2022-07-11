# DESAFIO 083 - Validando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


N_desafio = "083"
nome_desafio = "Validando expressões matemáticas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

expression = str()
abre = fecha = int()

expression = input("Informe uma expressão: ").strip()
pilha = list()
for count, val in enumerate(expression) :
    if '(' in val :
        abre = count
        pilha.append("(")
    if ')' in val :
        fecha = count
        if len(pilha) > 0 :
            pilha.pop()
        else :
            pilha.append(")")
            break

# de ua forma
if len(pilha) == 0 :
    print("Sua expressão está válida!")
else :
    print("sua expressão está errada!")

# de outra forma
if '(' in expression or ')' in expression :
    if '(' in expression and ')' in expression :
        if abre < fecha :
            print("A posição dos parenteses está correta")
        elif fecha < abre :
            print("A posição dos parenteses está errada")
        else :
            print("Erro de posição")
    else :
        print("Parenteses incompletos")
else :
    print("parenteses não encontrados")
