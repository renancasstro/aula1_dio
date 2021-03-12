#Definição de algumas funções para a aula 8

def contador_letras(lista_palavras):
    cont = []
    for x in lista_palavras:
        quant = len(x)
        cont.append(quant)
    return cont

def teste():
    return "teste"

if __name__ == "__main__":
    lista = ["cachorro", "gato"]
    print(contador_letras(lista))