""" 
    Objetivos da Aula:

    1. Aprender a utilização de métodos e funções no Python
    2. Aprender a utilização de classes
    3. Entender os motivos para se usar métodos, funções e classes
"""
#Criar uma classe com funções simples de calculadora
class Math:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

#Condição inserida na aula 8 para executar apenas se o mesmo arquivo no qual está contido que rodou o programa

if __name__ == "__main__":
    calc = Math(10,2)
    print(calc.valor_a)
    print(calc.soma())
    print(calc.subtracao())
    print(calc.multiplicao())
    print(calc.divisao())
