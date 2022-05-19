# primitives types

# inteiros
# int()
# flutuantes
# float()
# booleanos
# bool()
# string
# str()

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
total = n1 + n2
print('A soma entre {} e {} vale {}.' .format(n1, n2, total))

# informaçõies complementares, tipo das variáveis
print(type(n1))
print(type(n2))
print(type(total))


# tetes de tipo
txt = "CompanyX"
print(txt.isalpha())