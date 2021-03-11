# Aula de conjuntos

#Criar conjuntos para testar union, difference e intersection
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

#
conjunto_uniao = conjunto.union(conjunto2)
print("União: {}" .format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print("Intersecção: {}" .format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print("Difenreça entre 1 e 2: {}" .format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print("Diferença entre 2 e 1: {}" .format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença Simétrica: {}" .format(conjunto_diff_simetrica))

#Criar conjuntos para testar subset e superset
conjunto_a = {1, 2, 3}
print("Conjunto A = {}" .format(conjunto_a))
conjunto_b = {1, 2, 3, 4, 5}
print("Conjunto B = {}" .format(conjunto_b))

#Teste subset
conjunto_subset = conjunto_a.issubset(conjunto_b)
print("É {} que o Conjunto A é Subset do Conjunto B".format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print("É {} que o Conjunto B é Subset do Conjunto A".format(conjunto_subset))

#Teste superset
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print("É {} que o Conjunto A é Superset do Conjunto B".format(conjunto_superset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("É {} que o Conjunto B é Superset do Conjunto A".format(conjunto_superset))

#Criar listas para retirar duplicidade
lista = ["cachorro", "cachorro", "gato", "gato", "elefante"]
print(lista)

#Após converter para Set, a duplicidade não existirá mais
conjunto_animais = set(lista)
print(conjunto_animais)

#Após voltar para o formato lista, a duplicidade continua não existindo
lista_animais = list(conjunto_animais)
print(lista_animais)
