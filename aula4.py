# Uso do comando For pra identificar se o número é primo

print("Após digitar um número, o programa irá informar se o número é primo!")
a = int(input("Digite um número: "))
for a in range (0, a + 1):
    div = 0
    for x in range(1, a + 1):
        resto = a % x
        if resto == 0:
            div += 1
if div == 2:
    print("{} é um número primo.".format(a))
else:
    print("{} não é um número primo.".format(a))
print("Final do Programa")
