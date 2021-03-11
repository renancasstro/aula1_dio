# Aula de funcionalidades de print

print("O programa irá calcular a soma, subtração, multiplicação e divisão de dois valores!")
a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
while b == 0:
    print("O segundo valor não pode ser 0")
    b = float(input("Entre com o segundo valor: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(soma, subtracao, multiplicacao, divisao, resto, end="\n\n")
print("soma " + str(soma), end="\n\n")
print("Soma {}, Subtracao {}, Multiplicacao {}, Divisao {}, Resto {}.\n"
      .format(soma,
              subtracao,
              multiplicacao,
              divisao,
              resto))
print("Print com valores trocados: \nSoma {q}, \nSubtracao {w}, \nMultiplicacao {e}, \nDivisao {r}, \nResto {t}."
      .format(t=soma,
              r=subtracao,
              e=multiplicacao,
              w=divisao,
              q=resto))
