# Aula de list e tuple

lista = [12, 3, 15, 7]
lista_animal = ["cachorro", "lobo", "elefante"]
print(lista_animal[1])
nova_lista = lista_animal * 3
print(nova_lista)
nova_lista = lista * 3
print(nova_lista)

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

lista_animal.reverse()
print(lista_animal)


soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

print(sum(lista))
print(max(lista))
print(min(lista))

print(min(lista_animal))
print(max(lista_animal))

if "gato" in lista_animal:
    print("Existe um gato na lista")
else:
    print("Gato? Que gato? Agora tem.")
    lista_animal.append("gato")
    print(lista_animal)

lista_animal.pop()
lista_animal.remove("lobo")
print(lista_animal)

tupla = (1, 10, 12, 7, 14)
print(tupla[0])
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista.insert(0, 5)
print(lista)
