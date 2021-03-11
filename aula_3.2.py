# Calculadora de média escolar

print("Insira notas de 0 a 10!")
a = int(input("Primeiro bimestre: "))
while a > 10 or a < 0:
    a = int(input("Você digitou errado. Primeiro bimestre: "))
b = int(input("Segundo bimestre: "))
while b > 10 or b < 0:
    b = int(input("Você digitou errado. Segundo bimestre: "))
c = int(input("Terceiro bimestre: "))
while  c > 10 or c < 0:
    c = int(input("Você digitou errado. Terceiro bimestre: "))
d = int(input("Quarto bimestre: "))
while d > 10 or d < 0:
    d = int(input("Você digitou errado. Quarto bimestre: "))
media = (a + b + c + d) / 4
print("Media {}".format(media))
print("Final do programa")