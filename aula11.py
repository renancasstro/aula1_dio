lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
    print('Fechando o arquivo')
except ZeroDivisionError:
    print('Não é possível realizar a divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError:
    print('Erro ao acessar o índice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}:'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()