class Error(Exception):
    pass

class InputError(Error):
    def __init__ (self, message):
            self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)

        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas numeros.')
    except InputError as ex:
        print(ex)
        