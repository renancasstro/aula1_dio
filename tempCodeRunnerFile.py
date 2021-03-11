a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
restoa = a % 2
restob = b % 2
if restoa == 0 and restob == 0:
    print("Ambos os números são pares")
elif restoa == 0:
    print("Foi digitado pelo menos um número par")
else:
    print("Não foi digitado número par")
print("Fim do programa")