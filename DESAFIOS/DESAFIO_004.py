algo = input("Digite Algo: ")
print("Segue abaixo informações sobre o que você digitou")

print("O tipo primitivo desse valor é: {}".format(type(algo)))
print("É alfa-numérico: {}".format(algo.isalnum()))
print(f"É alfabético: {algo.isalpha()}")
print(f"ASCII: {algo.isascii()}")
print(f"É Decimal: {algo.isdecimal()}")
print(f"Digito string: {algo.isdigit()}")
print(f"Identificador: {algo.isidentifier()}")
print(f"Numerico: {algo.isnumeric()}")
print(f"É Writespace: {algo.isspace()}")
print(f"Está Title-cased: {algo.istitle()}")
print(f"Está uppercase: {algo.isupper()}")
print(f"Está lowercase: {algo.islower()}")
