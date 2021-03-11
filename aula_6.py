# Aula de conjuntos

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
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
conjunto = {1, 2, 3, 4, 4, 2}
conjunto.add(5)
conjunto.discard(2)
print((conjunto))

