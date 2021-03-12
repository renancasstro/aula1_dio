#Aprendizado de lambda e Set

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ["cachorro", "gato", "elefante"]
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5,10))
print(subtracao(60,70))

calculadora = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

soma = calculadora["sum"]
multiplicacao = calculadora["mult"]
print("A soma é: {}" .format(soma(10, 8)))
print("A multiplicação é: {}" .format(multiplicacao(10, 2)))

listacodigos = {
    "RJ" : 21,
    "SP" : 11,
}

RJ = listacodigos["RJ"]
print(RJ)