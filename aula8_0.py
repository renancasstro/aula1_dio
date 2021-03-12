"""
    Objetivos da aula:

    1. Aprender a utilizar e interagir com módulos
    2. Entender a importância de se utilizar módulos
    3. Aprender sobre funções anônimas
"""
from aula7_1 import Televisao
from aula7_0 import Math
from aula8_1 import contador_letras, teste

if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Math(5, 10)
    print(calculadora.soma())
    lista = ["cachorro", "gato", "elefante"]
    print("Total de letras por palavra da lista: {}" .format(contador_letras(lista)))
    print(teste())