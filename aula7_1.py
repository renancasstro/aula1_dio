# Mecanismo de ligar, desligar e trocar de canal
class Televisao:
    def __init__ (self):
        self.ligada = False
        self.canal = 5
    
    def power (self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal (self):
        #condicional para verificar se a Televisão está ligada
        if self.ligada:
            self.canal += 1
    
    def diminui_canal (self):
        #condicional para verificar se a Televisão está ligada
        if self.ligada:
            self.canal -= 1

#Condição inserida na aula 8 para executar apenas se o mesmo arquivo no qual está contido que rodou o programa

if __name__ == "__main__":
    tv = Televisao()
    print("Televisão está ligada: {}" .format(tv.ligada))
    tv.power()
    print("Televisão está ligada: {}" .format(tv.ligada))
    tv.power()
    print("Televisão está ligada: {}" .format(tv.ligada))
    tv.power()
    print("Televisão está ligada: {}" .format(tv.ligada))
    print("Canal: {}" .format(tv.canal))
    tv.aumenta_canal()
    tv.aumenta_canal()
    print("Canal: {}" .format(tv.canal))
    tv.diminui_canal()
    print("Canal: {}" .format(tv.canal))