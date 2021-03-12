"""
    Objetivos da aula:

    1. Aprender a ler e escrever arquivos
    2. Manipular informações dos arquivos
    3. Copiar e remover arquivos
""" 
import shutil

def escrever_arquivo(texto):
    diretorio = "C:/Users/Renan Castro/Desktop/teste.txt"
    arquivo = open(diretorio, "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open("teste.txt","a")
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split("\n")
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(",")
        aluno = lista_notas[0]
        notas = lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/len(lista_notas)
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "C:/Users/Renan Castro/Desktop/notas_alunos.txt" )

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, "C:/Users/Renan Castro/Desktop/Python/")

if __name__ == "__main__":
    # move_arquivo("teste.txt")
    # lista_media = media_notas("teste.txt")
    # print(lista_media)
    # escrever_arquivo("Primeira Linha.")
    # aluno = "\nRob, 10, 10, 5, 8"
    # atualizar_arquivo("notas.txt", aluno)
    # ler_arquivo("teste.txt")

